// Portfolio data helpers. The content itself lives in portfolio.json, which routes/web.php also reads (for 404s and
// per-case-study SEO), so the two always agree. Only published case studies are in that file: drafts are kept out
// of it (and so out of the JS bundle) until they are cleared.
import data from './portfolio.json';

export const CATEGORIES = [
  { key: 'all', label: 'All' },
  { key: 'web', label: 'Web & SaaS' },
  { key: 'mobile', label: 'Mobile' },
  { key: 'desktop', label: 'Desktop' },
  { key: 'ai', label: 'AI & Automation' },
  { key: 'games', label: 'Games' },
  { key: 'apis', label: 'APIs & Infrastructure' },
];

// List fields default to empty so a case study missing one renders without it instead of breaking the page.
const LISTS = ['categories', 'platforms', 'stack', 'challenge', 'built', 'results', 'nextSteps', 'gallery', 'videos', 'links'];

export const projects = data
  .filter((p) => p.published !== false)
  .map((p) => ({ ...Object.fromEntries(LISTS.map((k) => [k, []])), ...p }))
  .sort((a, b) => (a.order ?? 99) - (b.order ?? 99));

export function getProject(slug) {
  return projects.find((p) => p.slug === slug) ?? null;
}

export function categoryLabel(key) {
  return CATEGORIES.find((c) => c.key === key)?.label ?? key;
}

// Neighbours for the previous / next links at the bottom of a case study (wraps around).
export function neighbours(slug) {
  const i = projects.findIndex((p) => p.slug === slug);
  if (i === -1 || projects.length < 2) return { prev: null, next: null };
  return {
    prev: projects[(i - 1 + projects.length) % projects.length],
    next: projects[(i + 1) % projects.length],
  };
}

const STATUS_CLASSES = {
  'Live': 'bg-ink/85 text-positive ring-positive/40',
  'Shipped': 'bg-ink/85 text-accent-400 ring-accent-400/40',
  'In development': 'bg-ink/85 text-warning ring-warning/40',
};

// Badge classes for a status; an unknown status still gets a readable badge.
export const statusClasses = new Proxy(STATUS_CLASSES, {
  get: (target, key) => target[key] ?? 'bg-ink/85 text-content-muted ring-line',
});
