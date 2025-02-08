<script setup>
import { ref, computed } from 'vue';
import { Link } from '@inertiajs/vue3';

import AppLayout from '@/Layouts/AppLayout.vue';
import Timer from '@/Components/Timer.vue';
import Question from '@/Components/Question.vue';
import Review from '../Components/Review.vue';

const testStarted = ref(false);
const currentQuestionIndex = ref(0);
const userAnswers = ref([]);
const timeRemaining = ref(450); // 7:30 minutes in seconds
const testCompleted = ref(false);

const questions = ref([
    // Verbal Questions
    {
        id: 1,
        text: "Choose the word that is most nearly opposite in meaning to 'BENEVOLENT':",
        options: ["Malevolent", "Beneficent", "Munificent", "Magnanimous", "Benign"],
        correctAnswer: "Malevolent"
    },
    {
        id: 2,
        text: "FISH is to SCHOOL as WOLF is to ?",
        options: ["Pack", "Herd", "Flock", "Swarm", "Pride"],
        correctAnswer: "Pack"
    },
    {
        id: 3,
        text: "Which word does not belong with the others?",
        options: ["Trombone", "Flute", "Clarinet", "Oboe", "Violin"],
        correctAnswer: "Violin"
    },
    // Math and Logic Questions
    {
        id: 4,
        text: "If a columnist writes 19 articles per month, how many articles does she write in a year?",
        options: ["190", "209", "228", "247", "266"],
        correctAnswer: "228"
    },
    {
        id: 5,
        text: "What is the next number in the sequence: 2, 6, 12, 20, 30, ?",
        options: ["36", "40", "42", "48", "50"],
        correctAnswer: "42"
    },
    {
        id: 6,
        text: "If 5 cats can catch 5 mice in 5 minutes, how long will it take 1 cat to catch 1 mouse?",
        options: ["1 minute", "5 minutes", "25 minutes", "125 minutes", "Not enough information"],
        correctAnswer: "5 minutes"
    },
    // Spatial Reasoning Questions (with images)
    {
        id: 7,
        text: "Which of the following boxes should replace the question mark (?) to complete the pattern?",
        image: "/storage/img/box1.png",
        options: ["A", "B", "C", "D", "E"],
        correctAnswer: "B"
    },
    {
        id: 8,
        text: "Which of the following does not belong?",
        image: "/storage/img/doesntbelong1.png",
        options: ["A", "B", "C", "D", "E"],
        correctAnswer: "D"
    },
    {
        id: 9,
        text: "Which of the following boxes should replace the (?) to complete the pattern?",
        image: "/storage/img/triangles.png",
        options: ["A", "B", "C", "D", "E"],
        correctAnswer: "D"
    },
    {
        id: 10,
        text: "Which of the following boxes should replace the question mark (?) to complete the pattern?",
        image: "/storage/img/replace3.png",
        options: ["A", "B", "C", "D", "E"],
        correctAnswer: "E"
    },
    {
        id: 11,
        text: "Which of the following does not belong?",
        image: "/storage/img/doesntbelong3.png",
        options: ["A", "B", "C", "D", "E"],
        correctAnswer: "A"
    },
    {
        id: 12,
        text: "A hat stores sells 900 hats in its first year. If the number of hats it sells in the next year is 50% higher, how many hats will it sell in its second year?",
        options: ["1200", "1350", "1380", "1400", "1440"],
        correctAnswer: "1350"
    },
    {
        id: 13,
        text: "Which of the following boxes should replace the question mark (?) to complete the pattern?",
        image: "/storage/img/test5/9.png",
        options: ["A", "B", "C", "D", "E"],
        correctAnswer: "C"
    },
    {
        id: 14,
        text: "Choose the word that best completes the analogy: CANVAS is to PAINTER as STAGE is to ?",
        options: ["Director", "Actor", "Audience", "Curtain", "Script"],
        correctAnswer: "Actor"
    },
    {
        id: 15,
        text: "If a train travels at 60 mph, how many miles will it cover in 2.5 hours?",
        options: ["120", "140", "150", "160", "180"],
        correctAnswer: "150"
    },
    {
        id: 16,
        text: "Which word is the odd one out?",
        options: ["Swift", "Quick", "Rapid", "Slow", "Speedy"],
        correctAnswer: "Slow"
    },
    {
        id: 17,
        text: "If 3x + 7 = 22, what is the value of x?",
        options: ["3", "4", "5", "6", "7"],
        correctAnswer: "5"
    },
    {
        id: 18,
        text: "Complete the sequence: 2, 4, 8, 16, ?",
        options: ["24", "28", "30", "32", "36"],
        correctAnswer: "32"
    },
    {
        id: 19,
        text: "Which of the following is not a prime number?",
        options: ["2", "3", "5", "7", "9"],
        correctAnswer: "9"
    },
    {
        id: 20,
        text: "If all Zorks are Blips, and some Blips are Quuxes, which of the following must be true?",
        options: ["All Zorks are Quuxes", "All Blips are Zorks", "Some Zorks are Quuxes", "No Quuxes are Zorks", "All Quuxes are Blips"],
        correctAnswer: "Some Zorks are Quuxes"
    },
    {
        id: 21,
        text: "A piece of rope is cut into 5 equal pieces. If each piece is 15 inches long, how long was the original rope?",
        options: ["45 inches", "60 inches", "75 inches", "90 inches", "105 inches"],
        correctAnswer: "75 inches"
    },
    {
        id: 22,
        text: "Which word is closest in meaning to 'FRUGAL'?",
        options: ["Wasteful", "Extravagant", "Economical", "Generous", "Lavish"],
        correctAnswer: "Economical"
    },
    {
        id: 23,
        text: "If a clock shows 3:45, what is the angle between the hour and minute hands?",
        options: ["67.5°", "82.5°", "90°",  "157.5°", "180°"],
        correctAnswer: "157.5°"
    },
    {
        id: 24,
        text: "Which number should come next in this series? 25, 24, 22, 19, 15",
        options: ["10", "11", "12", "13", "14"],
        correctAnswer: "10"
    },
    {
        id: 25,
        text: "If 'VXJGL' stands for 'HOUSE' in a certain code, what does 'OVML' stand for?",
        options: ["DOOR", "ROOF", "ROOM", "WALL", "GATE"],
        correctAnswer: "ROOM"
    }

]);

const startTest = () => {
    testStarted.value = true;
    shuffleQuestions();
};

const shuffleQuestions = () => {
    for (let i = questions.value.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [questions.value[i], questions.value[j]] = [questions.value[j], questions.value[i]];
    }
};

const submitAnswer = (answer) => {
    userAnswers.value[currentQuestionIndex.value] = answer;
    if (currentQuestionIndex.value < questions.value.length - 1) {
        currentQuestionIndex.value++;
    } else {
        endTest();
    }
};

const endTest = () => {
    testCompleted.value = true;
    timeRemaining.value = 0;
};

const score = computed(() => {
    return userAnswers.value.filter((answer, index) => answer === questions.value[index].correctAnswer).length;
});

const onTimerExpired = () => {
    endTest();
};

const progressPercentage = computed(() => {
    return ((currentQuestionIndex.value + 1) / questions.value.length) * 100;
});

const getExplanation = (question, userAnswer) => {
    if (userAnswer === question.correctAnswer) {
        return "Correct! Well done.";
    }

    switch (question.id) {
        case 1:
            return "The word 'Malevolent' means wishing evil or harm to others, which is the opposite of 'Benevolent' (kind, generous).";
        case 2:
            return "A group of fish is called a 'school', while a group of wolves is called a 'pack'.";
        case 3:
            return "The violin is a string instrument, while all the others are wind instruments.";
        case 4:
            return "There are 12 months in a year, so 19 articles per month * 12 months = 228 articles per year.";
        case 5:
            return "The sequence is increasing by 4, then 6, then 8, then 10. So the next increase should be 12, making the next number 42.";
        case 6:
            return "If 5 cats can catch 5 mice in 5 minutes, then 1 cat can catch 1 mouse in 5 minutes. The ratio remains the same.";
        case 7:
            return "The pattern from top to bottom is Light, Gray, Dark, 1 units, 2 units, 3 units. Aplying this we find that the answer is B";
        case 8:
            return "All of the items have 3 points except for D";
        case 9:
            return "The pattern is Triangle, Circle, Triangle, Circle, so the answer would be D Triangle."
        case 10:
            return "Look at the images from Left to Right - Top to Bottom and you can see that they are rotating clockwise.";
        case 11:
            return "The bottom row is the same as the top row but offset to the right (with wrap around) 1 unit. Answer A is the only one thats offset to the left.";
        case 12:
            return "50% higher than 900 is calculated as: 900 + (50% of 900) = 900 + 450 = 1350";
        case 13:
            return "Study the progression of changes in the given sequence of images. Identify any consistent rules or transformations applied to the elements. The correct answer will be the option that follows these rules and best completes the pattern.";
        case 14:
            return "A painter uses a canvas to create art, just as an actor uses a stage to perform.";
        case 15:
            return "Distance = Speed * Time. So, 60 mph * 2.5 hours = 150 miles.";
        case 16:
            return "'Slow' is the opposite of the other words, which all mean 'fast' or 'quick'.";
        case 17:
            return "To solve 3x + 7 = 22, subtract 7 from both sides: 3x = 15. Then divide by 3: x = 5.";
        case 18:
            return "The sequence is doubling each time: 2 * 2 = 4, 4 * 2 = 8, 8 * 2 = 16, 16 * 2 = 32.";
        case 19:
            return "A prime number is only divisible by 1 and itself. 9 is divisible by 3, so it's not prime.";
        case 20:
            return "If all Zorks are Blips, and some Blips are Quuxes, then it's possible (but not certain) that some Zorks are Quuxes.";
        case 21:
            return "If each piece is 15 inches and there are 5 pieces, then 15 * 5 = 75 inches total.";
        case 22:
            return "'Frugal' means economical in use or expenditure; prudently saving or sparing; not wasteful.";
        case 23:
            return "The minute hand moves 360 degrees in 60 minutes. Each minute corresponds to 6 degrees (360° ÷ 60). The hour hand moves 360 degrees in 12 hours. Each hour corresponds to 30 degrees (360° ÷ 12). Since it's 3:45, the hour hand has moved 3/4 of the way between 3 and 4. The hour hand moves 0.5 degrees per minute (30° ÷ 60), so in 45 minutes, it has moved 45×0.5=22.5∘45×0.5=22.5 ∘ .Therefore, the hour hand is at 90+22.5=112.5∘90+22.5=112.5 ∘.Angle Between the Hands. The difference between the positions of the minute and hour hands is ∣270−112.5∣=157.5∘∣270−112.5∣=157.5 ∘ .";
        case 24:
            return "The sequence is decreasing by 1, then 2, then 3, then 4. So the next decrease should be 5, making the next number 10.";
        case 25:
            return "Given: 'VXJGL' stands for 'HOUSE' Let's match each letter: V = H | X = O | J = U |G = S |L = E The correct pattern is that each letter in the code is 4 alphabets after the actual letter. So to encode, we move 4 letters forward, and to decode, we move 4 letters backward. Now, let's decode 'OVML' by moving 4 letters backward for each: O - 4 = K | V - 4 = R | M - 4 = I (wrapping around from A to Z) L - 4 = H This gives us 'KRIH', which doesn't spell anything. But moving one more letter backward for each: K - 1 = J R - 1 = Q I - 1 = H H - 1 = G";
        default:
            return "Analyze the image properly to find the correct answer.";
    }
};
</script>

<template>
    <AppLayout title="Free Practice Test">
        <template #header>
            <h2 class="font-semibold text-xl text-gray-800 dark:text-gray-200 leading-tight">
                Free Practice Test
            </h2>
        </template>

        <div class="py-12">
            <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
                <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg">
                    <div class="p-6 sm:px-20 bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700">
                        <div v-if="!testStarted" class="text-left">
                            <h1 class="text-3xl font-bold mb-6 text-gray-900 dark:text-gray-100 text-center">Free
                                Practice Test:
                                25 Questions</h1>
                            <div class="space-y-4 text-gray-600 dark:text-gray-400">
                                <p class="mb-4">You will have <span
                                        class="font-semibold text-gray-800 dark:text-gray-200">7:30
                                        minutes</span> to complete the test. This free assessment measures your aptitude
                                    in
                                    areas such as critical thinking and problem-solving. It provides a glimpse into the
                                    full
                                    CCAT experience.</p>

                                <div class="bg-gray-100 dark:bg-gray-700 p-4 rounded-lg">
                                    <h2 class="text-xl font-semibold mb-2 text-gray-800 dark:text-gray-200">Test
                                        Instructions:
                                    </h2>
                                    <ul class="list-disc list-inside space-y-2">
                                        <li>Answer each question carefully, but do not spend too much time on any one
                                            question.
                                        </li>
                                        <li>If you can't determine the answer, select your best guess and move on.</li>
                                        <li>You will receive one point for each correct answer. No points are deducted
                                            for
                                            incorrect answers.</li>
                                        <li>The questions may increase in difficulty as the assessment progresses.</li>
                                        <li>Try to answer as many questions as you can within the time limit.</li>
                                    </ul>
                                </div>

                                <div class="bg-yellow-50 dark:bg-yellow-900 p-4 rounded-lg">
                                    <h2 class="text-xl font-semibold mb-2 text-yellow-800 dark:text-yellow-200">
                                        Important Notes:
                                    </h2>
                                    <ul class="list-disc list-inside space-y-2 text-yellow-700 dark:text-yellow-300">
                                        <li>You are NOT permitted to use calculators or any other problem-solving
                                            device.</li>
                                        <li>Please have a pen and paper with you when you take the assessment.</li>
                                        <li>Ensure your device has a reliable Internet connection.</li>
                                        <li>Avoid leaving the assessment window or switching your browser tab during the
                                            test.
                                        </li>
                                    </ul>
                                </div>

                                <p class="font-semibold text-gray-800 dark:text-gray-200">Your time will begin as soon
                                    as you
                                    click the "Begin Test" button.</p>
                            </div>
                            <div class="mt-8 text-center">
                                <button @click="startTest"
                                    class="inline-flex items-center px-6 py-3 bg-blue-600 border border-transparent rounded-md font-semibold text-base text-white uppercase tracking-widest hover:bg-blue-500 active:bg-blue-700 focus:outline-none focus:border-blue-700 focus:ring ring-blue-300 disabled:opacity-25 transition ease-in-out duration-150">
                                    Begin Test
                                </button>
                            </div>
                        </div>

                        <div v-else-if="testStarted && !testCompleted" class="text-center">
                            <div class="mb-4">
                                <Timer :initial-time="timeRemaining" @expired="onTimerExpired" />
                            </div>
                            <div class="mb-4">
                                <div class="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700">
                                    <div class="bg-blue-600 h-2.5 rounded-full"
                                        :style="{ width: progressPercentage + '%' }">
                                    </div>
                                </div>
                                <p class="text-sm text-gray-600 dark:text-gray-400 mt-1">
                                    Question {{ currentQuestionIndex + 1 }} of {{ questions.length }}
                                </p>
                            </div>
                            <Question :question="questions[currentQuestionIndex]"
                                :question-number="currentQuestionIndex + 1" :total-questions="questions.length"
                                @answer-submitted="submitAnswer" />
                        </div>

                        <div v-else class="text-center">
                            <h2 class="text-2xl font-bold mb-4 text-gray-900 dark:text-gray-100">Test Completed</h2>
                            <p class="mb-2 text-gray-600 dark:text-gray-400">Your score: {{ score }} / {{
                                questions.length }}
                            </p>
                            <div v-for="(question, index) in questions" :key="question.id" class="mb-8 text-left">
                                <p class="text-gray-900 dark:text-gray-100"><strong>Question {{ index + 1 }}:</strong>
                                    {{
                                    question.text }}</p>
                                <img v-if="question.image" :src="question.image"
                                    :alt="'Image for question ' + (index + 1)" class="my-2 max-w-full h-auto">
                                <p class="text-gray-600 dark:text-gray-400">Your answer: {{ userAnswers[index] || 'Not            answered'                       }}</p>
                                <p class="text-gray-600 dark:text-gray-400">Correct answer: {{ question.correctAnswer }}
                                </p>
                                <p v-if="userAnswers[index] !== question.correctAnswer"
                                    class="mt-2 text-red-600 dark:text-red-400">
                                    <strong>Explanation:</strong> {{ getExplanation(question, userAnswers[index]) }}
                                </p>
                            </div>

                            <!-- Upgrade Account Section for non-subscribed users -->
                            <div id="upgrade-account" class="mb-12 animate-on-scroll">
                                <div
                                    class="bg-gradient-to-r from-blue-500 to-indigo-600 rounded-lg shadow-lg p-8 text-white">
                                    <h2 class="text-3xl font-bold mb-4">Upgrade to Lifetime Access</h2>
                                    <p class="mb-4">Get unlimited access to all our practice tests and questions.
                                        Upgrade now to
                                        supercharge your CCAT preparation!</p>
                                    <ul class="list-disc list-inside mb-6 space-y-2">
                                        <li>10 Full Practice tests (500 Questions) from the CCAT</li>
                                        <li>380 Verbal practice questions from the CCAT</li>
                                        <li>326 Math & Logic practice questions from the CCAT</li>
                                        <li>260 Spatial Reasoning practice questions from the CCAT</li>
                                        <li>Weekly updates with new questions from the CCAT</li>
                                    </ul>
                                    <p class="mb-4">98% OF OUR CUSTOMERS REPORTED PASSING THEIR EXAMS USING OUR PREP
                                        SOLUTION -
                                        LATEST CCAT {{ currentMonthYear }} EXAMS!</p>
                                    <Link :href="route('upgrade.account')"
                                        class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-indigo-600 bg-white hover:bg-indigo-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-colors duration-200">
                                    Upgrade Now
                                    <svg class="ml-2 -mr-1 w-5 h-5" fill="currentColor" viewBox="0 0 20 20"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path fill-rule="evenodd"
                                            d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                                            clip-rule="evenodd"></path>
                                    </svg>
                                    </Link>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div id="reviews">
                <Review
    :test-completed="testCompleted"
    :test-started="testStarted"
/></div>
            </div>
        </div>
    </AppLayout>
</template>

<style scoped>
/* Add any additional styles here */
</style>
