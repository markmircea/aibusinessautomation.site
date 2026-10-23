<?php

namespace App\Providers;

use Illuminate\Support\Facades\View;
use Illuminate\Support\ServiceProvider;
use Illuminate\Support\Str;
use Inertia\Inertia;


class AppServiceProvider extends ServiceProvider
{
    /**
     * Register any application services.
     */
    public function register(): void
    {
        //
    }

    /**
     * Bootstrap any application services.
     */
    public function boot()
    {
        Inertia::share([
            'url' => function () {
                return url()->current();
            },
            'flash' => function () {
                return [
                    'success' => session()->get('success'),
                    'error' => session()->get('error'),
                    'message' => session()->get('message'),
                ];
            },
        ]);

        // Link previews (WhatsApp, Slack, LinkedIn, Facebook, X) read only the HTML the server sends and never run
        // JavaScript, so DynamicSEO.vue alone never reaches them: the root view renders the same tags from this.
        View::composer('app', function ($view) {
            $view->with('seo', self::seoFor($view->getData()['page'] ?? []));
        });
    }

    /**
     * Title, description, canonical URL and share image for an Inertia page, resolved the way DynamicSEO.vue does:
     * the page's own `seo` prop (portfolio case studies), else resources/js/data/seo.json by component.
     */
    private static function seoFor(array $page): array
    {
        $data = json_decode(file_get_contents(resource_path('js/data/seo.json')), true);
        $props = $page['props'] ?? [];
        $key = $page['component'] ?? '';
        if ($key === 'WebDevelopment/Service') {
            // The service pages share one component: 'digital-marketing' -> 'WebDevelopment/DigitalMarketing'
            $key = 'WebDevelopment/' . Str::studly($props['slug'] ?? '');
        }
        $seo = ! empty($props['seo']['title']) ? $props['seo'] : ($data['pages'][$key] ?? $data['fallback']);
        $image = $seo['image'] ?? $data['image'];

        return [
            'site' => $data['site'],
            'title' => $seo['title'],
            'description' => $seo['description'] ?? '',
            'url' => url()->current(),
            'image' => url($image['src']),
            'imageAlt' => $image['alt'] ?? $seo['title'],
            'imageWidth' => $image['width'] ?? null,
            'imageHeight' => $image['height'] ?? null,
        ];
    }
}
