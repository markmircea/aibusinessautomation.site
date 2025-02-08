<template>
  <AppLayout title="Upgrade Account">
      <template #header>
          <h2 class="font-semibold text-xl text-gray-800 dark:text-gray-200 leading-tight">
              Upgrade Account
          </h2>
      </template>

      <div class="py-12">
          <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">


              <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg">
                  <div class="p-6 lg:p-8 bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700">
                      <h1 class="text-2xl font-bold text-gray-900 dark:text-white mb-2">
                          Upgrade to Lifetime Access
                      </h1>
                      <div class="flex items-center mb-6">
                          <span class="text-3xl font-bold text-green-600 dark:text-green-400">$49.95</span>
                          <span class="ml-2 text-xl text-gray-500 dark:text-gray-400 line-through">$79.95</span>
                          <span class="ml-2 text-sm font-medium text-red-600 dark:text-red-400">TEMPORARY SALE</span>
                      </div>


                      <p class="mt-4 text-gray-600 dark:text-gray-400 text-lg">
                          Upgrade your account to get lifetime access to:
                      </p>

                      <ul class="mt-4 space-y-2">
                          <li v-for="(feature, index) in features" :key="index" class="flex items-start">
                              <svg class="h-6 w-6 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                              </svg>
                              <span class="text-gray-700 dark:text-gray-300">{{ feature }}</span>
                          </li>
                      </ul>

                      <p class="mt-6 text-gray-600 dark:text-gray-400">
                          More practice questions are added weekly.
                      </p>

                      <p class="mt-6 text-lg font-semibold text-gray-800 dark:text-gray-200">
                          98% of our users reported passing their exams using our prep solution.
                      </p>

                      <p class="mt-2 text-gray-600 dark:text-gray-400">
                          Latest Version CCAT {{ currentMonthYear }} Exams!
                      </p>

                      <div v-if="!$page.props.auth.user" class="mt-6 p-4 bg-yellow-50 dark:bg-yellow-900 text-yellow-800 dark:text-yellow-200 rounded-md">
                          Note: After successful payment, you'll be prompted to create an account to access your upgraded features.
                      </div>

                      <div v-if="error" class="mt-4 p-4 bg-red-100 dark:bg-red-900 text-red-700 dark:text-red-200 rounded-md">
                          {{ error }}
                      </div>

                      <div class="mt-8 flex justify-center">
  <div id="paypal-button-container" class="w-full max-w-md bg-gray-100 dark:bg-gray-600 p-4 rounded-md"></div>
</div>

                      <div v-if="loading" class="mt-4 text-center text-gray-600 dark:text-gray-400">
                          Processing your payment...
                      </div>
                  </div>
              </div>
              <sub-upgrade-account/>
          </div>
          </div>
      </div>
      <review/>
  </AppLayout>
</template>
<script setup>
import { onMounted, ref } from 'vue';
import AppLayout from '@/Layouts/AppLayout.vue';
import { useForm } from '@inertiajs/vue3';
import { usePage } from '@inertiajs/vue3';
import SubUpgradeAccount from './SubUpgradeAccount.vue';
import Review from '../Components/Review.vue';

const props = defineProps({
  paypalClientId: String,
});

const page = usePage();

const form = useForm({
  paypal_order_id: null,
});

const error = ref(null);
const loading = ref(false);

const features = [
"10 Full Practice tests with timers (500 Questions, Answers and Explanations) from the current CCAT",
"10 Additional Full PDF files with Questions and Answers (500 Questions and Answers)",

"Detailed Explanations for ALL Questions",
"Original Tests",
"Same Practice Conditions",
"Weekly updates with new questions",
"24/7 Support via E-mail or Chat!",

];

const currentMonthYear = ref(new Date().toLocaleString('default', { month: 'long', year: 'numeric' }));

const gtag_report_conversion = (url, transaction_id) => {
  var callback = function () {
      if (typeof(url) != 'undefined') {
          window.location = url;
      }
  };
  gtag('event', 'conversion', {
      'send_to': 'AW-1037877088/a1PlCPHcw94ZEOD-8u4D',
      'value': 49.99,
      'currency': 'USD',
      'transaction_id': transaction_id,
      'event_callback': callback
  });
  return false;
};



const initPayPalButton = () => {
  paypal.Buttons({
      createOrder: (data, actions) => {
          return actions.order.create({
              purchase_units: [{
                  amount: {
                      value: '49.95'
                  }
              }]
          });
      },
      onApprove: (data, actions) => {
          loading.value = true;
          error.value = null;
          return actions.order.capture().then(function(orderData) {
              if (orderData.status === 'COMPLETED') {
                  form.paypal_order_id = orderData.id;

                  form.post(route('upgrade.account.process'), {
                      preserveState: true,
                      preserveScroll: true,
                      onSuccess: (response) => {
                          gtag_report_conversion(undefined, orderData.id);
                          if (!page.props.auth.user) {
                              window.location.href = route('register');
                          } else {
                              window.location.href = route('dashboard');
                          }
                      },
                      onError: (errors) => {
                          loading.value = false;
                          error.value = "There was an error processing your upgrade. Please try again or contact support.";
                          console.error('Server-side error:', errors);
                      }
                  });
              } else {
                  loading.value = false;
                  error.value = "Payment was not completed. Please try again.";
                  console.error('Payment not completed:', orderData);
              }
          }).catch(function(err) {
              loading.value = false;
              error.value = "There was an error processing your payment. Please try again.";
              console.error('PayPal Capture Error:', err);
          });
      },
      onError: (err) => {
          loading.value = false;
          error.value = "There was an error setting up the payment. Please try again or use a different payment method.";
          console.error('PayPal Error:', err);
      },
      onCancel: (data) => {
          error.value = "Payment was cancelled. If this was unintentional, please try again.";
          console.log('Payment cancelled:', data);
      }
  }).render('#paypal-button-container');
}

onMounted(() => {
  const script = document.createElement('script');
  script.src = `https://www.paypal.com/sdk/js?client-id=${props.paypalClientId}`;
  script.addEventListener('load', initPayPalButton);
  script.addEventListener('error', () => {
      error.value = "There was an error loading the payment system. Please refresh the page or try again later.";
  });
  document.body.appendChild(script);
});
</script>
