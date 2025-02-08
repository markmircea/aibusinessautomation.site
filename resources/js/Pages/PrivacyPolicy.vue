<script setup>
import { Head } from '@inertiajs/vue3';
import AuthenticationCardLogo from '@/Components/AuthenticationCardLogo.vue';
import { ref } from 'vue';

defineProps({
    policy: String,
});

const activeAccordion = ref(null);

const goBack = () => {
    window.close();
};

const toggleAccordion = (index) => {
    activeAccordion.value = activeAccordion.value === index ? null : index;
};

const faqItems = [
    {
        question: "What information do we collect?",
        answer: `We collect information from you when you register on our site, place an order, subscribe to our newsletter, respond to a survey, fill out a form or click on links in email newsletters.

When ordering or registering on our site, as appropriate, you may be asked to enter your: name, e-mail address, mailing address, phone number or credit card information. You may, however, visit our site anonymously.`
    },
    {
        question: "What do we use your information for?",
        answer: `Any of the information we collect from you may be used in one of the following ways:

• To personalize your experience
• To improve our website
• To improve customer service
• To process transactions
• To send periodic emails

Your information, whether public or private, will not be sold, exchanged, transferred, or given to any other company for any reason whatsoever, without your consent, other than for the express purpose of delivering the purchased product or service requested.

The email address you provide for order processing, may be used to send you information and updates pertaining to your order, in addition to receiving occasional company news, updates, related product or service information, etc.

Note: If at any time you would like to unsubscribe from receiving future emails, we include detailed unsubscribe instructions at the bottom of each email.`
    },
    {
        question: "Do we use cookies?",
        answer: `Yes. Cookies are small files that a site or its service provider transfers to your computer's hard drive through your Web browser (if you allow) that enables the sites or service providers systems to recognize your browser and capture and remember certain information.

We use cookies to help us remember and process the items in your shopping cart, understand and save your preferences for future visits and compile aggregate data about site traffic and site interaction so that we can offer better site experiences and tools in the future. We may contract with third-party service providers to assist us in better understanding our site visitors. These service providers are not permitted to use the information collected on our behalf except to help us conduct and improve our business.`
    },
    {
        question: "Do we disclose any information to outside parties?",
        answer: `We do not sell, trade, or otherwise transfer to outside parties your personally identifiable information.`
    },
    {
        question: "Your consent",
        answer: `By using our site, you consent to our online privacy policy and the terms and conditions of this site.`
    },
    {
        question: "Do we disclose any information to outside parties?",
        answer: `We value the importance of data privacy and are committed to empowering our users with control over their personal information. You have the right to request the deletion of any Personal Information that we have collected and retained from you. You may delete your account and once we receive and verify your data deletion request, we will process and delete your Personal Information from our records.

Please note that if you request data deletion, your account will be permanently closed, and your access to current products will be revoked. If you wish to use our services again, you will need to create a new account.

However, if you have previously purchased any products on CCATtest.COM, we can restore your access to those products. To initiate the restoration process, we kindly ask you to provide proof of payment. This can be in the form of an email receipt issued by CCATtest.com or a payment receipt issued by PayPal.

To initiate a data deletion request, please contact our Support Team at support@ccattest.com In your request, please include the following information in the provided form:

• Full name
• Email address associated with your account
• A clear and explicit statement expressing your desire for personal data deletion
• Device Type
• Language of the website
• Web browser type
• Email (in hashed form)
• Our Support Team will guide you through the process and assist you with any additional information or verification requirements.`
    },

];
</script>

<template>

    <Head title="Privacy Policy" />

    <div class="min-h-screen bg-gray-100 dark:bg-gray-900 text-gray-800 dark:text-gray-200">
        <div class="pt-6 sm:pt-0">
            <div class="flex flex-col items-center">
                <div class="mt-4">
                    <AuthenticationCardLogo />
                </div>
                <h1 class="mt-6 text-3xl font-bold">Privacy Policy</h1>
            </div>

            <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-3xl">
                <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-md sm:rounded-lg p-6">
                    <div class="space-y-4">
                        <div v-for="(item, index) in faqItems" :key="index"
                            class="border-b border-gray-200 dark:border-gray-700">
                            <button @click="toggleAccordion(index)"
                                class="flex justify-between items-center w-full py-4 text-left">
                                <span class="text-lg font-medium">{{ item.question }}</span>
                                <svg class="w-5 h-5 transform transition-transform duration-200"
                                    :class="{ 'rotate-180': activeAccordion === index }" viewBox="0 0 20 20"
                                    fill="currentColor">
                                    <path fill-rule="evenodd"
                                        d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                                        clip-rule="evenodd" />
                                </svg>
                            </button>
                            <div v-show="activeAccordion === index" class="pb-4">
                                <p class="text-gray-600 dark:text-gray-400 whitespace-pre-line">
                                    {{ item.answer }}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                 <!-- Back Button -->
                 <div class="mt-6 flex justify-center">
                    <button
                        @click="goBack"
                        class="inline-flex items-center px-4 py-2 bg-gray-800 dark:bg-gray-200 border border-transparent rounded-md font-semibold text-xs text-white dark:text-gray-800 uppercase tracking-widest hover:bg-gray-700 dark:hover:bg-white focus:bg-gray-700 dark:focus:bg-white active:bg-gray-900 dark:active:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 dark:focus:ring-offset-gray-800 transition ease-in-out duration-150"
                    >
                        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
                        </svg>
                        Close Tab
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.prose {
    max-width: 100%;
}
</style>
