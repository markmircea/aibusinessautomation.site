<script setup>
import { ref, onMounted } from 'vue';
import StarRating from './Stars.vue';

const reviews = ref([]);
const averageRating = ref(0);
const totalReviews = ref(0);
const ratingDistribution = ref({});
const loading = ref(true);

const reviewsListRef = ref(null); // Add ref for reviews list element
const loadingNewPage = ref(false); // Separate loading state for pagination

// Pagination state
const currentPage = ref(1);
const lastPage = ref(1);
const perPage = ref(3);
const total = ref(0);

// New review form state
const showReviewForm = ref(false);
const newReview = ref({
    rating: 0,
    reviewer_name: '',
    reviewer_email: '',
    comment: ''
});
const submitting = ref(false);
const formError = ref('');

const props = defineProps({
    testCompleted: {
        type: Boolean,
        required: true,
    },
    testStarted: {
        type: Boolean,
        required: true,
    }
});

const formatDate = (date) => {
    if (!date) return 'Unknown date';
    return new Date(date).toLocaleDateString();
};

const getReviewerName = (review) => {
    return review.reviewer_name || 'Anonymous User';
};

const getInitial = (name) => {
    return (name || 'A')[0].toUpperCase();
};

const loadReviews = async (page = 1) => {
    try {
        loading.value = true;
        const response = await fetch(`/api/reviews?page=${page}`);
        const data = await response.json();

        reviews.value = data.reviews;
        averageRating.value = data.averageRating;
        totalReviews.value = data.totalReviews;
        ratingDistribution.value = data.ratingDistribution;

        currentPage.value = data.pagination.current_page;
        lastPage.value = data.pagination.last_page;
        perPage.value = data.pagination.per_page;
        total.value = data.pagination.total;
    } catch (err) {
        console.error('Error loading reviews:', err);
    } finally {
        loading.value = false;
    }
};

const changePage = (page) => {
    if (page >= 1 && page <= lastPage.value) {
        currentPage.value = page;
        loadReviews(page);
    }
};

const handleRatingSelect = (rating) => {
    newReview.value.rating = rating;
    showReviewForm.value = true;
};

const resetForm = () => {
    newReview.value = {
        rating: 0,
        reviewer_name: '',
        reviewer_email: '',
        comment: ''
    };
    showReviewForm.value = false;
    formError.value = '';
};

const getCsrfToken = () => {
    return document.querySelector('meta[name="csrf-token"]')?.content;
};

const submitReview = async () => {
    if (!newReview.value.rating) {
        formError.value = 'Please select a rating';
        return;
    }

    const token = getCsrfToken();
    if (!token) {
        formError.value = 'Security token not found. Please refresh the page.';
        return;
    }

    try {
        submitting.value = true;
        formError.value = '';

        const response = await fetch('/reviews', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'Accept': 'application/json',
                'X-CSRF-TOKEN': token
            },
            credentials: 'include', // Include cookies
            body: JSON.stringify(newReview.value)
        });

        // Check if the response is JSON
        const contentType = response.headers.get('content-type');
        if (!contentType || !contentType.includes('application/json')) {
            const text = await response.text();
            console.error('Non-JSON response:', text);
            throw new Error('Server returned an invalid response. Please try again.');
        }

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || 'Failed to submit review');
        }

        // Refresh the reviews
        await loadReviews(1);
        resetForm();
    } catch (err) {
        formError.value = err.message || 'Error submitting review. Please try again.';
        console.error('Submit error:', err);
    } finally {
        submitting.value = false;
    }
};

onMounted(() => {
    loadReviews();
});
</script>

<template>
    <div class="review-section my-8 max-w-4xl mx-auto">
        <div v-if="loading" class="text-center py-4">
            <p class="text-gray-600 dark:text-gray-400">Loading reviews...</p>
        </div>

        <div v-else>
            <!-- Reviews Summary -->
            <div v-if="!testStarted || testCompleted" class="mb-6 bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
                <div class="grid md:grid-cols-2 gap-6">
                    <!-- Left side - Average rating -->
                    <div class="text-center md:border-r md:dark:border-gray-700">
                        <div class="text-4xl font-bold text-gray-800 dark:text-gray-200 mb-2">
                            {{ averageRating }}
                        </div>
                        <div class="flex justify-center my-2">
                            <StarRating :rating="averageRating" :readonly="true" size="lg" />
                        </div>
                        <div class="text-gray-600 dark:text-gray-400">
                            {{ totalReviews }} {{ totalReviews === 1 ? 'review' : 'reviews' }}
                        </div>
                    </div>

                    <!-- Right side - Rating distribution -->
                    <div v-if="totalReviews > 0" class="space-y-2">
                        <div v-for="stars in [5, 4, 3, 2, 1]" :key="stars" class="flex items-center">
                            <span class="text-sm w-12 text-gray-600 dark:text-gray-400">{{ stars }} stars</span>
                            <div class="flex-1 mx-2">
                                <div class="h-2 bg-gray-200 dark:bg-gray-700 rounded-full overflow-hidden">
                                    <div class="h-full bg-yellow-400 rounded-full transition-all duration-500"
                                        :style="{ width: `${(ratingDistribution[stars] / totalReviews) * 100}%` }">
                                    </div>
                                </div>
                            </div>
                            <span class="text-sm w-16 text-right text-gray-600 dark:text-gray-400">
                                {{ ratingDistribution[stars] || 0 }}
                                ({{ Math.round((ratingDistribution[stars] / totalReviews) * 100) || 0 }}%)
                            </span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- New Review Section -->
            <div v-if="testCompleted" class="mb-6 bg-white dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden">
                <div class="p-6">
                    <h3 class="text-lg font-semibold text-gray-800 dark:text-gray-200 mb-4">Write a Review</h3>
                    <div class="flex justify-center mb-4">
                        <StarRating :rating="newReview.rating" @update:rating="handleRatingSelect" size="lg" />
                    </div>

                    <!-- Review Form -->
                    <div class="overflow-hidden transition-all duration-300" :style="{
                        maxHeight: showReviewForm ? '500px' : '0',
                        opacity: showReviewForm ? 1 : 0
                    }">
                        <form @submit.prevent="submitReview" class="space-y-4">
                            <div class="space-y-2">
                                <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">
                                    Name
                                </label>
                                <input type="text" v-model="newReview.reviewer_name"
                                    class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
                                    required />
                            </div>

                            <div class="space-y-2">
                                <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">
                                    Email (optional)
                                </label>
                                <input type="email" v-model="newReview.reviewer_email"
                                    class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white" />
                            </div>

                            <div class="space-y-2">
                                <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">
                                    Comment
                                </label>
                                <textarea v-model="newReview.comment" rows="4"
                                    class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
                                    required></textarea>
                            </div>

                            <div v-if="formError" class="text-red-500 text-sm">
                                {{ formError }}
                            </div>

                            <div class="flex justify-end space-x-3">
                                <button type="button" @click="resetForm"
                                    class="px-4 py-2 text-sm font-medium text-gray-700 dark:text-gray-300 bg-gray-100 dark:bg-gray-700 rounded-md hover:bg-gray-200 dark:hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500">
                                    Cancel
                                </button>
                                <button type="submit" :disabled="submitting"
                                    class="px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed">
                                    {{ submitting ? 'Submitting...' : 'Submit Review' }}
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>

            <!-- Existing Reviews List -->
            <div v-if="reviews.length > 0 && !testStarted || testCompleted" class="space-y-4">
                <div v-for="review in reviews" :key="review.id"
                    class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg">
                    <div class="flex items-center justify-between mb-3">
                        <div class="flex items-center space-x-3">
                            <div
                                class="w-10 h-10 bg-blue-100 dark:bg-blue-900 rounded-full flex items-center justify-center">
                                <span class="text-blue-600 dark:text-blue-300 font-semibold">
                                    {{ getInitial(getReviewerName(review)) }}
                                </span>
                            </div>
                            <div>
                                <div class="font-semibold text-gray-800 dark:text-gray-200">
                                    {{ getReviewerName(review) }}
                                </div>
                                <div class="text-sm text-gray-500 dark:text-gray-400">
                                    {{ formatDate(review.created_at) }}
                                </div>
                            </div>
                        </div>
                        <StarRating :rating="review.rating" :readonly="true" />
                    </div>
                    <div v-if="review.comment" class="text-gray-700 dark:text-gray-300 mt-2">
                        {{ review.comment }}
                    </div>
                </div>

                <!-- Pagination Controls -->
                <div v-if="lastPage > 1" class="flex justify-center items-center space-x-2 mt-6">
                    <button @click="changePage(currentPage - 1)" :disabled="currentPage === 1"
                        class="px-4 py-2 rounded-lg bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors">
                        Previous
                    </button>

                    <div class="flex items-center space-x-1">
                        <template v-for="page in lastPage" :key="page">
                            <button @click="changePage(page)" class="px-4 py-2 rounded-lg transition-colors" :class="{
                                'bg-blue-500 text-white': page === currentPage,
                                'bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600': page !== currentPage
                            }">
                                {{ page }}
                            </button>
                        </template>
                    </div>

                    <button @click="changePage(currentPage + 1)" :disabled="currentPage === lastPage"
                        class="px-4 py-2 rounded-lg bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors">
                        Next
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
