<script setup>
import { ref, onMounted } from 'vue';
import LazyImage from './LazyImage.vue';

const isIntersecting = ref(false);

const steps = [
  {
    number: '1',
    title: 'Pass cognitive aptitude test.',
    description: "Accepting job applications from the entire world means every role on Crossover receives thousands of applications. We find that the most reliable way to shortlist the very best candidates is by objectively measuring problem solving skills. Crossover does this via a 15-minute Criteria Cognitive Aptitude Test (CCAT). Different roles require different scores. Candidates who don't make the grade can try again after six months."
  },
  {
    number: '2',
    title: 'Pass English proficiency test.',
    description: "Someday, technological advancements will make it possible for teams to collaborate without sharing a common language. Until then, English language skills are necessary for all positions advertised on Crossover. That's why candidates who pass the CCAT are next required to complete an English proficiency test which involves hearing and repeating English phrases."
  },
  {
    number: '3',
    title: 'Prove real-world job skills.',
    description: "Of course, there's much more to being a great worker than intelligence and language skills. The next step is to complete a real-world job assignment which has been curated specifically for the role – e.g. software engineers can expect a coding task, whereas marketing managers will need to show excellent copywriting skills. The result is graded blindly, to eliminate any potential for bias."
  },
  {
    number: '4',
    title: 'Ace an interview or two.',
    description: "Candidates who reach the interview stage have already proven objectively that they've got what it takes to succeed in the role. So, unlike traditional job interviews which focus on subjective questioning from hiring managers, this step at Crossover is primarily an opportunity for the candidate and hiring manager to assess a mutual team fit."
  },
  {
    number: '5',
    title: 'Accept job offer.',
    description: "And that's pretty much it! Crossover's turnaround from initial application to offer can happen in as little as three days. Once we've identified that someone truly is in the top 1% of the talent pool, we want to place them into a role ASAP. We're often recruiting for multiple roles at the same level, so it's not uncommon for all the best candidates to receive an offer."
  }
];

const visualSteps = [
  {
    title: 'Pass Cognitive Aptitude Test.',
    imageUrl: 'https://assets-us-01.kc-usercontent.com:443/7beb5311-75a4-0049-50f5-8f58fd55aba7/2df06207-56be-45d3-88c3-3380dae96bdb/pass-cognitive-aptitude-test.svg'
  },
  {
    title: 'Pass English Proficiency Test.',
    imageUrl: 'https://assets-us-01.kc-usercontent.com:443/7beb5311-75a4-0049-50f5-8f58fd55aba7/5215fe11-6e66-4249-8238-d9225443a36f/pass-english-proficiency-test.svg'
  },
  {
    title: 'Prove Real-World Job Skills.',
    imageUrl: 'https://assets-us-01.kc-usercontent.com:443/7beb5311-75a4-0049-50f5-8f58fd55aba7/1dfddffd-b2e8-4680-8c1d-02024553c264/prove-real-world-job-skills.svg'
  },
  {
    title: 'Ace An Interview Or Two.',
    imageUrl: 'https://assets-us-01.kc-usercontent.com:443/7beb5311-75a4-0049-50f5-8f58fd55aba7/4099cf43-e0fa-4021-98e4-43112b8a61c7/ace-an-interview-or-two.svg'
  },
  {
    title: 'Accept Job Offer.',
    imageUrl: 'https://assets-us-01.kc-usercontent.com:443/7beb5311-75a4-0049-50f5-8f58fd55aba7/cba8c1b8-c659-4cab-8bac-bb5acb216345/accept-job-offer.svg'
  },
  {
    title: 'Celebrate!',
    imageUrl: 'https://assets-us-01.kc-usercontent.com:443/7beb5311-75a4-0049-50f5-8f58fd55aba7/68913706-6901-4f27-93d8-b83df0261030/celebrate.svg'
  }
];

onMounted(() => {
  const observer = new IntersectionObserver(
    ([entry]) => {
      isIntersecting.value = entry.isIntersecting;
    },
    { threshold: 0.1 }
  );

  const section = document.getElementById('get-hired-at-crossover');
  if (section) {
    observer.observe(section);
  }

  return () => observer.disconnect();
});
</script>

<template>
    <section id="get-hired-at-crossover" class="mb-12 animate-on-scroll" :class="{ 'opacity-100 translate-y-0': isIntersecting }">
      <div class="relative overflow-hidden bg-gradient-to-br from-blue-50 to-white dark:from-gray-800 dark:to-gray-900 rounded-2xl shadow-xl p-8">
        <!-- Header Section -->
        <div class="relative z-10">
          <h2 class="text-4xl font-bold mb-2 bg-gradient-to-r from-blue-600 to-blue-800 dark:from-blue-400 dark:to-blue-600 bg-clip-text text-transparent">
            Get Hired at Crossover
          </h2>
          <h3 class="text-2xl font-bold mb-6 text-gray-700 dark:text-gray-300">HOW IT WORKS</h3>
        </div>

        <!-- Introduction Cards -->
        <div class="grid md:grid-cols-2 gap-6 mb-8">
          <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300">
            <div class="flex items-start space-x-4">
              <div class="bg-blue-100 dark:bg-blue-900 rounded-lg p-3">
                <svg class="w-6 h-6 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
              </div>
              <div>
                <p class="font-bold text-xl mb-2 text-gray-800 dark:text-gray-100">Score Requirements</p>
                <p class="text-gray-600 dark:text-gray-300">To get hired at Crossover for Work you need to score in the 85 percentile or top 15%. (MINIMUM 35 / 50 CORRECT)

Signing up for out paid exam will prepare you for ALL the questions on the test.</p>


              </div>
            </div>
          </div>
          <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300">
            <div class="flex items-start space-x-4">
              <div class="bg-green-100 dark:bg-green-900 rounded-lg p-3">
                <svg class="w-6 h-6 text-green-600 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <div>
                <p class="font-bold text-xl mb-2 text-gray-800 dark:text-gray-100">Time Requirements</p>
                <p class="text-gray-600 dark:text-gray-300"><strong>50 Questions in 15 minutes...</strong> We are the only test-prep platform offering tests in the same format as Criteria Corp. </p>
                <p class="mt-6 text-gray-600 dark:text-gray-300">

            <strong>It's not easy to qualify for a role on Crossover</strong> because the CCAT is designed to shortlist only the top 1% of applicants.


            <strong>But it's worth it...</strong> because qualifying on Crossover is the ticket to a world-class job (with matching pay).

          </p>

              </div>
            </div>
          </div>
        </div>

        <!-- Steps Section -->
        <div class="space-y-8">
          <div v-for="(step, index) in steps" :key="index" class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md hover:shadow-lg transition duration-300 border-l-4"
               :class="step.number === '5' ? 'border-green-500' : 'border-blue-500'">
            <div class="flex items-center mb-4">
              <span class="bg-blue-100 dark:bg-blue-900 text-blue-600 dark:text-blue-400 rounded-full w-8 h-8 flex items-center justify-center font-bold mr-3">
                {{ step.number }}
              </span>
              <h4 class="text-xl font-bold text-gray-800 dark:text-gray-100">{{ step.title }}</h4>
            </div>
            <p class="text-gray-600 dark:text-gray-300 leading-relaxed">
              {{ step.description }}
            </p>
          </div>

          <!-- Warning Card -->
          <div class="bg-red-50 dark:bg-red-900/20 rounded-xl p-6 border-l-4 border-red-500">
            <div class="flex items-center mb-4">
              <span class="bg-red-100 dark:bg-red-900 text-red-600 dark:text-red-400 rounded-full p-2 mr-3">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                </svg>
              </span>
              <h4 class="text-xl font-bold text-red-700 dark:text-red-400">One Last Thing</h4>
            </div>
            <p class="text-gray-600 dark:text-gray-300 leading-relaxed">
              If you pass the Crossover testing process and get a job offer, you'll be asked to complete a proctored version of the CCAT test (2 cameras, 1 web camera and 1 telephone camera while a live person watches). Provided you can repeat your score under these strict exam conditions, you're in!
            </p>
          </div>
        </div>

        <!-- Visual Steps -->
        <div class="mt-12 hidden md:block p-6">
          <div class="flex justify-between items-start w-full">
            <div v-for="(step, index) in visualSteps" :key="index"
                 class="flex-1 relative group">
              <div class="flex flex-col items-center text-center px-1 sm:px-2 hover:scale-105 transition duration-300">
                <div class="icon mb-2 md:mb-3 hidden md:block  p-3">
                  <img :src="step.imageUrl"
                       :alt="step.title"
                       class="w-12 h-12 lg:w-[50px] lg:h-[50px]"
                       loading="lazy" />
                </div>
                <div class="item-title">
                  <div class="heading text-uppercase text-[10px] md:text-xs bg-blue-100 dark:bg-blue-900 text-blue-600 dark:text-blue-400 rounded-full px-3 py-1 inline-block">
                    STEP {{ index + 1 }}
                  </div>
                  <h4 class="title text-xs sm:text-sm md:text-base mt-2 font-semibold text-gray-800 dark:text-gray-100">{{ step.title }}</h4>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
</template>

<style scoped>



.heading {
  @apply font-semibold mb-0.5;
}

@screen sm {
  .title {
    @apply max-w-[120px] mx-auto;
  }
}

@screen md {
  .title {
    @apply max-w-[140px];
  }
}

@screen lg {
  .title {
    @apply max-w-[160px];
  }
}

.bg-gradient-overlay {
  background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
}
</style>
