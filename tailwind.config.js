import defaultTheme from 'tailwindcss/defaultTheme';
import forms from '@tailwindcss/forms';
import typography from '@tailwindcss/typography';

/** @type {import('tailwindcss').Config} */
export default {
    content: [
        './vendor/laravel/framework/src/Illuminate/Pagination/resources/views/*.blade.php',
        './vendor/laravel/jetstream/**/*.blade.php',
        './storage/framework/views/*.php',
        './resources/views/**/*.blade.php',
        './resources/js/**/*.vue',
    ],

    // The site ships a single dark theme. `class` is kept (not dropped) so the
    // existing dark: variants stay active via <html class="dark"> in app.blade.php.
    // Dropping this would fall back to 'media' and break light-preference visitors.
    darkMode: 'class',

    theme: {
        extend: {
            fontFamily: {
                sans: ['Figtree', ...defaultTheme.fontFamily.sans],
            },

            colors: {
                // Surfaces, darkest to lightest
                ink: '#0B1020',          // page background
                surface: '#141A2E',      // cards
                'surface-2': '#1B2238',  // raised / hover
                line: '#1E2640',         // borders

                // Brand navy — headers, decorative gradients
                brand: {
                    900: '#131D4D',
                    700: '#1B2A6B',
                    500: '#2F4BC4',
                    300: '#6B82E8',
                },

                // Electric indigo — CTAs and interactive accents only
                accent: {
                    600: '#4658E8',
                    500: '#5B6CFF',
                    400: '#7C89FF',
                },

                // Text
                content: {
                    DEFAULT: '#F2F4FA',
                    muted: '#A8B0C8',
                    subtle: '#6B7490',
                },

                // Status badges only — never decorative
                positive: '#3FBF87',
                warning: '#E8B93D',
                danger: '#E8635B',
            },

            // Exactly two radii (plus rounded-full for pills/avatars)
            borderRadius: {
                control: '8px',
                card: '14px',
            },

            boxShadow: {
                e1: '0 1px 2px 0 rgb(0 0 0 / 0.30)',
                e2: '0 4px 12px -2px rgb(0 0 0 / 0.40)',
                e3: '0 16px 40px -8px rgb(0 0 0 / 0.55)',
            },
        },
    },

    plugins: [forms, typography],
};
