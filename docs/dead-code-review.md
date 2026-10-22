# Dead-code audit — CCAT-era remnants still in the repo

**Scope:** every file touched by the port from the CCAT (Crossover Career Assessment Test) prep site to
the AIBrainLink automation-services site — i.e. all 50 files in `ffc549b..eed0d46` ("visual
improvements, dead code removal ccat") **plus** everything those files orphaned.
**Date:** 2026-02-12. **Nothing outside this file was modified.**
**Verdict up front:** 43 frontend files (6,258 lines), 15 PHP classes (10 of them the Teams slice),
2 blade views, 3 registered + 2 commented routes, 6 unused DB tables, 3 composer packages,
2 dead CSS rules and ~318 kB of per-deploy build output are provably dead. Two items need a product
decision (§6, §1c), and five deletions must be paired with edits or they *will* break the live
site — those are called out in §12. Two **live-but-broken** routes were found along the way
(`complete-registration`, `generate-explanation`); they are not dead code but they are in scope for
the same cleanup commit.

---

## 0. Method — how each verdict was established

Not by eyeballing. Seven independent checks, cross-referenced:

1. **Route-dispatch ground truth.** Every registered GET route (68 of them) was dispatched through the
   real HTTP kernel with the real session/middleware stack, guest and authenticated. The Inertia
   `data-page` attribute of each response was parsed for its `component` value. That yields the exact
   set of **27 Vue components the application can actually render** — no guessing about which
   Jetstream/Fortify vendor features are enabled, because the vendor routes answer or don't.
2. **Comment-aware reachability graph.** BFS over `import` / `export … from` / dynamic `import()` in
   all 132 files under `resources/js`, seeded from `app.js`, `bootstrap.js` and the 27 live pages.
   Comments and `<!-- -->` blocks are stripped *before* extraction, so a commented-out import does not
   count as a reference. Result: **90 reachable / 43 unreachable.** (A naive first pass counted
   commented imports and wrongly called `SolutionsDropdown.vue` and `Eleven.vue` live — the corrected
   pass catches them.)
3. **Repo-wide negative search.** For each of the 43 unreachable files, its basename was grepped across
   the whole repo (excluding `vendor/`, `node_modules/`, `.git/`, `public/build/`). Zero references
   outside `resources/js` — the only hits are this document.
4. **Vendor-source check.** `vendor/laravel/jetstream/src/JetstreamServiceProvider.php` registers
   `Pages/Teams/*` only when `Features::teams()` is on, `Pages/API/*` only when `Features::api()` is
   on, `Pages/Auth/VerifyEmail.vue` only under Fortify's email-verification feature. All three are
   commented out in `config/jetstream.php` / `config/fortify.php`, so those pages are unreachable *by
   construction*, not by omission.
5. **Inertia prop truth table.** `props.jetstream` as actually delivered on a live page:
   `canCreateTeams=false, hasTeamFeatures=false, hasApiFeatures=false, hasEmailVerification=false,
   hasTermsAndPrivacyPolicyFeature=false, managesProfilePhotos=false` (everything else true). This is
   what makes whole template branches provably dead rather than "probably".
6. **Production build.** `vite build` (2,548 modules) emits a chunk for every file matched by
   `import.meta.glob('./Pages/**/*.vue')` in `app.js:16` — including all the dead pages. Measured dead
   output: `Dashboard` 80 kB, `FullPracticeTest` 120 kB (112 kB of it CSS), `FreePracticeTestStart`
   16 kB, ~8–9 kB each for the other 10 CCAT pages, plus `upgrade2`, and chunks for
   `ApiTokenManager / CreateTeamForm / DeleteTeamForm / TeamMemberManager / UpdateTeamNameForm / Show /
   Create / VerifyEmail`. The glob is expanded at **build** time, so "it's only lazily loaded" is not a
   defence: the bytes ship on every deploy.
7. **PHP-side inbound-reference analysis** per class (constructor injection, route action, Blade view,
   config indirection such as `config('jetstream_teams')`), plus `php artisan route:list`, the Ziggy
   payload (`window.Ziggy` → 58 names), `composer`/`npm` usage scans, and a DB schema cross-check
   against every `users.*`/`referrals.*` read in `app/` and `resources/js/`.

---

## 1. Frontend — 43 unreachable files

### 1a. CCAT pages (`resources/js/Pages/`) — 15

| File | Lines | Why it is dead |
|---|---|---|
| `Dashboard.vue` | ~60 | Only rendered by the `/dashboard` route, which is commented out in `routes/web.php`; nothing links to it. Expects `isSubscribed`/`practiceTestType` props that no live route supplies. |
| `FreePracticeTestStart.vue` | ~380 | Route commented out. Emits a 15.3 kB chunk. |
| `FullPracticeTest.vue` | 1,052 | Route commented out. Emits 120 kB (7.96 kB JS + 112.4 kB CSS). |
| `FullPracticeTestStart.vue` | ~250 | Route commented out. |
| `FullTest.vue` | ~230 | Route commented out. |
| `VerbalTest.vue`, `VerbalTestStart.vue`, `VerbalJsonStart.vue` | ~250 ea | Routes commented out. |
| `MathLogicTest.vue`, `MathLogicTestStart.vue`, `MathLogicJsonStart.vue` | ~250 ea | Routes commented out. |
| `SpatialReasoningTest.vue`, `SpatialReasoningTestStart.vue`, `SpatialReasoningJsonStart.vue` | ~250 ea | Routes commented out. |
| `upgrade2.vue` | ~180 | Never routed. A stale fork of the upgrade page (still points at `route('dashboard')`). |

### 1b. CCAT-era / never-imported components (`resources/js/Components/`) — 18

`CompaniesUsingCCAT.vue`, `DashboardHeader.vue`, `Definition.vue`, `FAQ.vue`,
`GetHiredAtCrossover.vue`, `LifetimePlan.vue`, `MathLogicTest.vue`, `PracticeWithCCATtest.vue`,
`Question.vue`, `SpatialReasoningTest.vue`, `Timer.vue`, `VerbalTest.vue`,
`UpgradeAccount.vue` (the *component* — distinct from the live `Pages/UpgradeAccount.vue`),
`ConfirmationModal.vue`, `ApplicationLogo.vue`, `Eleven.vue`, `SolutionsDropdown.vue`, `Welcome.vue`.

Every one of these is imported **only** by files in §1a/§1b/§1c — verified per file, so removing the
pages orphans them exactly, and removing them orphans nothing live. `Eleven.vue` and
`SolutionsDropdown.vue` survive today only inside comments (`Welcome.vue:9`, `AppLayout.vue:14`) —
dead in the corrected pass, live-looking in a naive one that counts commented imports as references
(the first pass got this wrong). `ApplicationLogo.vue` is dead because the redesigned auth screens
use their own mark; it is Jetstream blueprint scaffolding, so treat it like §1c.

### 1c. Jetstream scaffolding for disabled features — 9

`Pages/Teams/Show.vue`, `Pages/Teams/Create.vue`,
`Pages/Teams/Partials/{CreateTeamForm,DeleteTeamForm,TeamMemberManager,UpdateTeamNameForm}.vue`,
`Pages/API/Index.vue`, `Pages/API/Partials/ApiTokenManager.vue`, `Pages/Auth/VerifyEmail.vue`
(`ConfirmationModal.vue`, listed in §1b, belongs to this group too).

Feature flags are off (§0.5), and their menu links are `v-if="hasApiFeatures"` / `canCreateTeams`, so
they can never render. `ConfirmationModal.vue` is imported by nothing (Jetstream's own Vue blueprints
use it, but the app's live profile screens don't).

> Paired-edit caveat: `Pages/Auth/VerifyEmail.vue` is rendered by **vendor** code
> (`JetstreamServiceProvider.php:215`) if `Fortify::emailVerification()` is ever re-enabled. Same for
> the Teams/API pages and `Features::teams()`/`api()`. Deleting them makes re-enabling those features
> a build error ("Cannot find module ./Pages/Teams/Show.vue"). Decide consciously; §12 groups them so
> the intent is recorded in the commit message.

### 1d. Misc — 3

- `resources/js/vite-env.d.ts` — its entire payload is `interface Window { gtag(...) }`. `gtag()` is
  never called anywhere in `resources/` (the Google Ads tag was removed from `app.blade.php`), and the
  file is not referenced by `tsconfig.json`'s `include`.
- `Pages/SubUpgradeAccount.vue` is **live** (rendered kebab-case as `<sub-upgrade-account/>` from
  `Pages/UpgradeAccount.vue`) — a reachability pass that misses kebab-case component usage calls it
  dead. It isn't.
- `Pages/Error.vue` is live (rendered by the 404/500 closures in `Handler.php` / `web.php`).

---

## 2. Dead weight inside files that ARE live

Line-level removals that are individually safe:

| File | Dead element | Evidence |
|---|---|---|
| `Layouts/AppLayout.vue` | `showingFullPracticeTestSubmenu` ref; `switchToTeam()` (calls the **non-existent** `current-team.update` route — safe only because nothing ever invokes it); `isSubscribed` computed (used only inside commented nav blocks); commented `SolutionsDropdown` import; commented "Upgrade Account" nav blocks (~lines 162, 299); `.nav-icon` in `<style>` | §0.2, `route:list` has no `current-team.update` |
| `Pages/Welcome.vue` | `//import Eleven …`; commented `<!-- <Eleven /> -->`; unused `Link` import; `canLogin`/`canRegister` props (the `/` route renders `Welcome` with **no** props) | prop never passed; token appears once |
| `Pages/Portfolio.vue` | unused `import { Link }` | token appears once |
| `Pages/Referrals/Index.vue` | unused `computed` import | ditto |
| `Pages/Referrals/PublicIndex.vue` | unused `ref` import | ditto |
| `Pages/Admin/{Dashboard,Contacts/Index,Contacts/Show,Referrals/Index}.vue` | unused `ref` imports; `Admin/Dashboard.vue` declares a `stats` prop that its template never reads **and** `Admin\DashboardController` never passes | both sides dead |
| `Pages/Solutions/SolutionLayout.vue` | `const props =` binding unused (defineProps itself is used) | cosmetic |
| `Components/BusinessSolutionCard.vue` | `timeline` prop — declared, passed by `SolutionsSection`, never rendered | token appears once in card |
| `Components/Review.vue` | `reviewsListRef`, `loadingNewPage` refs ("Add ref for reviews list element" — the ref was never wired) | token appears once |
| `Components/FlashMessage.vue` | unused `onMounted` import | ditto |
| `Components/Icon.vue` | `CreditCard`, `ReceiptText` imports in the icon registry — no file ever requests those names | repo-wide token scan |
| `Pages/SubUpgradeAccount.vue` | `initPayPalButton()` superseded by `initPayPalWithRetry()` / `initializePayPalButton()`; never called | token appears once |
| `Pages/Solutions/CustomerService.vue` | `.hover-scale` in `<style>` — no user | CSS scan |
| `resources/css/app.css` | `[x-cloak] { display: none }` (Alpine.js is not a dependency — zero `x-cloak` in the codebase); the hand-rolled `.transition-colors` block re-declares a Tailwind utility that Tailwind already emits | `package.json`, `composer.json` |

---

## 3. Template branches that can never render

Guarded by Jetstream props that are hard-wired `false` (§0.5). These are not bugs, but they are dead
UI inside live files and they *mask* route names that don't exist:

| Location | Guard | Consequence |
|---|---|---|
| `AppLayout.vue:114-121`, `:259-263` | `managesProfilePhotos` | profile-photo avatar (desktop menu + responsive header) never renders → `Components/LazyImage.vue`'s only remaining consumer is this dead branch |
| `AppLayout.vue:146`, `:281` | `hasApiFeatures` | "API Tokens" links never render, and `route('api-tokens.index')` is absent from Ziggy — safe **only** because the guard is false |
| `Auth/Register.vue:104-116` | `hasTermsAndPrivacyPolicyFeature` | terms checkbox never renders; the `route('terms.show')` / `route('policy.show')` calls inside it are therefore **never evaluated** (see §13) |
| `Profile/Partials/UpdateProfileInformationForm.vue:93`, `:161` | `managesProfilePhotos`, `hasEmailVerification` | photo editor block + "your email is unverified" block dead; `route('verification.send')` absent from Ziggy but unreachable |

---

## 4. Backend — dead classes, methods, views

| Item | Why dead |
|---|---|
| `app/Http/Controllers/QuestionPDF.php` (69 l) | FPDF renderer that draws CCAT questions/answers/options. Only used by `QuestionPDFController`; its route is commented at `routes/web.php` (`// Route::get('question-pdf', …)`). |
| `app/Http/Controllers/QuestionPDFController.php` (126 l) | Same. No route, no other reference. |
| `resources/views/pdf/test.blade.php` | "Full Practice Test {testNumber}" HTML for dompdf. `grep -rn "pdf.test\|pdf/test"` → **zero** references. Also the reason `barryvdh/laravel-dompdf` is installed but never used. |
| `app/Http/Controllers/PdfDownloadController.php` | Routed (`GET /download-pdf/{filename}`, `web.php:177`, behind `paid.user`) but **nothing in the frontend ever calls it**, and it can only ever 404: it streams from `storage/app/public/`, which contains only `.gitignore`, and `public/storage` was never created (`php artisan storage:link` absent). Dead-by-content, not dead-by-route — see §6. |
| `User::isSubscribed()` | Its only caller was the commented `/dashboard` closure. `PaidUserMiddleware` reads the raw column `$user->has_paid_subscription`, not the accessor. |
| `User` → `use Illuminate\Contracts\Auth\MustVerifyEmail;` | Imported, never used (the class does not implement it — which is why the `verified` middleware is a no-op). |
| `routes/channels.php` + `app/Providers/BroadcastServiceProvider.php` | Provider commented out in `config/app.php:167`; no broadcast event exists in the app; no pusher/reverb package installed. |
| `routes/console.php` | Stock `inspire` closure only. |
| `resources/views/emails/team-invitation.blade.php` | Vendor-shipped mail view for team invitations; unreachable with teams disabled. |
| `routes/web.php` auth-group `verified` middleware | No-op: `User` does not implement `MustVerifyEmail` (§5 note). Runs on every authenticated request for nothing. |

### 4.1 `ReviewController.php` — cosmetic merge artifact
The file declares `namespace App\Http\Controllers;` twice (second block re-imports
`Review`, `OpenRouter`, `Request`). Legal PHP (the second declaration resets the import table) and not
a live bug, but it is a port leftover; both `store()` (live: `POST /reviews`) and `getReviews()`
(live: `GET /api/reviews`) are reachable.

---

## 5. The Jetstream **Teams** cluster — the largest dead subtree

Teams is disabled (`config/jetstream.php:61` — `// Features::teams()`), yet the whole vertical slice
was left in place **and is still executing**: `app/Actions/Fortify/CreateNewUser.php` creates a
personal team for *every* signup (that is why production has ~100 `teams` rows for a service site).

Dead today:

- `app/Actions/Jetstream/{CreateTeam,UpdateTeamName,AddTeamMember,InviteTeamMember,RemoveTeamMember,DeleteTeam}.php`
- `app/Models/{Team,TeamInvitation,Membership}.php`, `app/Policies/TeamPolicy.php`
- `User::use HasTeams` (adds `teams()`, `ownedTeams()`, `allTeams()`, `switchTeam()`, `currentTeam`)
- `CreateNewUser::createTeam()` (live code path doing dead work)
- `database/migrations/2020_05_21_100000_create_teams_table.php`,
  `2020_05_21_200000_create_team_user_table.php`,
  `2020_05_21_300000_create_team_invitations_table.php`
- `database/factories/TeamFactory.php`, `UserFactory::withPersonalTeam()`
- `resources/views/emails/team-invitation.blade.php`
- `JetstreamServiceProvider`'s six team bindings + `configurePermissions()` roles
- `tests/Feature/UpdateTeamNameTest.php`, `DeleteTeamTest.php`, `InviteTeamMemberTest.php`,
  `LeaveTeamTest.php`, `RemoveTeamMemberTest.php`, `UpdateTeamMemberRoleTest.php`,
  `CreateTeamTest.php` — these are the 8 errors + 2 failures in `php artisan test`
- `AppLayout.vue`'s `switchToTeam()` and every team prop reference
- `Pages/Teams/*` (§1c)

> **Trap.** `app/Actions/Jetstream/DeleteUser.php` is **live** (account deletion is enabled) but its
> constructor takes `DeletesTeams`, and the binding that makes that resolvable is
> `Jetstream::deleteTeamsUsing(DeleteTeam::class)` in `JetstreamServiceProvider`. Delete `DeleteTeam`
> (or that binding) without rewriting `DeleteUser` and account deletion fatals. This is exactly the
> class of removal that "would affect current functionality" — §12 sequences it.

---

## 6. Paid-user CCAT commerce chain — **product decision required**

This is the one cluster that is *not* unreachable in the routing sense:

- `/upgrade-account` is **live and nav-linked**, and `Pages/UpgradeAccount.vue` + `SubUpgradeAccount.vue`
  sell **"$49.95 Lifetime Access"** whose copy is pure CCAT ("10 Full Practice tests … from the current
  CCAT", "10 Additional Full PDF files"). Its JSON-LD advertises CCAT test prep to Google.
- Everything that purchase unlocks is dead: `has_paid_subscription` gates the whole paid-user group
  (`web.php:164-178`) — `/api/generate-question` + `/api/generate-explanation` (CCAT question
  generators whose only callers are the three dead *Start pages) and `/download-pdf/{filename}`
  (no caller, empty storage), plus the PDFs in `public/ccat/`.
- The purchase path is broken anyway: `UpgradeAccountController` redirects to `route('dashboard')`,
  which is commented out → `RouteNotFoundException` → HTTP 500 on successful payment (reproduced:
  `POST /complete-registration` → 500 "Route [dashboard] not defined"). It also points at hardcoded
  `api-m.sandbox.paypal.com` with `'verify' => false`.
- `POST /api/generate-explanation` (`web.php:172`) points at
  `OpenRouterController::generateExplanation()`, **which does not exist** — the class only defines
  `generateQuestion()`. Any paid user hitting it gets a 500 (`BadMethodCallException`). Live broken
  route, not merely dead code.
- `OpenRouterController` is CCAT-only: `HTTP-Referer: https://ccattest.com`, `X-Title: CCAT`, and a
  $7 lifetime spend cap recorded in a config table — for a service no customer can reach.
- `Pages/UpgradeAccount.vue` / `SubUpgradeAccount.vue` call `route('dashboard')` client-side; `dashboard`
  is confirmed absent from the Ziggy payload, so even the JS side throws at PayPal `onApprove`.

Two coherent resolutions (pick one, then the rest follows): **(a)** delete the whole funnel
(page, sub-component, `UpgradeAccountController`, `OpenRouterController`, `complete-registration`,
`paid.user` middleware alias, `public/ccat/`, `QuestionPDF*`, `PdfDownloadController`,
`User::isSubscribed`) — but keep `users.has_paid_subscription` + `subscription_started_at`, see §7;
or **(b)** keep the funnel and re-scope it to a real AIBrainLink offer (then fix the `dashboard`
redirect, move PayPal off sandbox, rewrite copy/JSON-LD, and repurpose the OpenRouter budget for a
live feature).

---

## 7. Unused DB surface — and the columns that must NOT be dropped

Unused tables (no code path reads them): `sessions` (`SESSION_DRIVER=file`), `failed_jobs`
(`QUEUE_CONNECTION=sync`), `personal_access_tokens` (`Features::api()` off, no Sanctum guard use — the
`auth:sanctum` middleware in `web.php` resolves the *session* guard via `config('jetstream.auth_session')`),
`teams`, `team_user`, `team_invitations`.

Columns:

- `users.current_team_id` — dead with teams.
- `oauth_accounts.*` — live (Google sign-in).
- **`users.has_paid_subscription` and `users.subscription_started_at` are NOT dead even if §6 goes
  away**: `app/Http/Middleware/PaidUserMiddleware.php` reads the first, and
  `Pages/Profile/Partials/UpdateProfileInformationForm.vue` renders both in the live profile screen.
  Dropping either column requires a paired edit of those two live files. Deleting the *frontend*
  upgrade funnel does not make these columns safe to drop.

---

## 8. Unused assets and tracked junk

| Path | Verdict |
|---|---|
| `public/ccat/` (7 files: `CROSSOVERCCAT-TEST{3,4,5}-ANSWERS.pdf`, `…TEST5-ANSWERS (1).doc`, `officialCCATtest{1,2}.pdf`, `desktop.ini`) | Referenced by **nothing** in code. Because they sit in `public/`, nginx serves them statically — they are reachable by URL guess, which is a licensing exposure, not just dead weight. Check Search Console for indexed URLs before/after removal. |
| `public/ransomize.py` | CCAT question-shuffler; its inputs (`public/test2.json` … `test20.json`) no longer exist. Publicly downloadable `.py`. |
| `public/img/logos/{cisco,docusign,wayfair}.svg` | Not in `LogoSlider.vue`'s list, not in `data/webDevelopmentServices.js`, not in `Portfolio.vue`. |
| `public/img/{landing.PNG,workflow.PNG}` | Zero references in CSS, Vue, Blade. |
| `laravel.log` (tracked, 2,379 lines) | Log committed to git; contains personal e-mails and old `W:\WAMP` paths. Belongs in `.gitignore` + history purge. |
| `dmca-validation.html` (repo **root**) | Tracked but not in `public/`, so it cannot validate anything — and the `<div id="dmca-badge"></div>` in `app.blade.php:30` is empty because the DMCA/Tawk.to script above it is commented out. Dead div + dead file. |

---

## 9. Dependencies and config that nothing uses

- **composer:** `codedge/laravel-fpdf` and `fpdf/fpdf` — used only by the dead `QuestionPDF*` classes;
  `barryvdh/laravel-dompdf` — **zero** references anywhere (its view is `pdf/test.blade.php`, itself
  unreferenced). Removing the three is what actually shrinks `vendor/`.
  `@fortawesome/fontawesome-free` (npm) is live but only via `Pages/Solutions/AIIntegrations.vue`.
- **Tailwind theme tokens never used:** `brand-900`, `brand-500`, `brand-300` (only `from-brand-700`
  appears); every `ink-*`/`surface-*` sub-shade is unused because the palette is consumed as flat
  tokens (`bg-ink`, `bg-surface`, `bg-surface-2`, `border-line`) — the nested `ink: {…}` / `surface: {…}`
  scales declared in earlier iterations are gone now, but the remaining `brand` sub-shades are dead.
  `positive`/`warning`/`danger`, `shadow-e1/e2/e3`, `rounded-card`/`rounded-control` are all live.
- `tsconfig.json` **and** `jsconfig.json` both present (redundant; `tsconfig` has no `paths`, so the
  `@/` alias used by every file resolves only through Vite).
- `config/broadcasting.php` pusher block with no pusher package installed.
- `AuthServiceProvider`'s `admin` gate is hardcoded to `admin@example.com` and the same list is
  duplicated in `AppLayout.vue`'s `isAdmin` — live, but a single-source-of-truth problem to note.

---

## 10. Dead tests (they run, and they fail)

`php artisan test` → 43 tests, **8 errors + 2 failures, 9 skipped**; every failure is in the Teams
slice (`CreateTeamTest`, `DeleteTeamTest`, `InviteTeamMemberTest`, `LeaveTeamTest`,
`RemoveTeamMemberTest`, `UpdateTeamMemberRoleTest`, `UpdateTeamNameTest`, `ApiTokenPermissionsTest`).
Also dead-but-passing: `tests/Feature/RegistrationTest.php`'s two team assertions,
`EmailVerificationTest` (feature disabled → skips), `CreateApiTokenTest`, `DeleteApiTokenTest`,
`PasswordConfirmationTest`-adjacent API tests, and the two stock `ExampleTest.php`sm.

---

## 11. Do **not** delete — looks CCAT, is load-bearing

| Item | Why it stays |
|---|---|
| `Pages/UpgradeAccount.vue`, `Pages/SubUpgradeAccount.vue`, `UpgradeAccountController`, `routes/web.php` `GET /upgrade-account` + `POST /complete-registration` | Live, nav-linked route. Deleting them *is* a product decision (§6), not cleanup. |
| `Components/DynamicSEO.vue` + its `WebDevelopment/{Ecommerce,Presentation,Mobile,Automation}` and CCAT-worded meta keys | Live: the key is derived at runtime from `page.component` + slug, so all four service pages resolve correctly. Copy is stale, wiring is live. |
| `AppServiceProvider`'s `Inertia::share(['component' => …])` | `DynamicSEO.vue` reads `usePage().component`. Removing the share silently kills every title/description. |
| `Components/LazyImage.vue` | Imported by live `AppLayout.vue` — but only inside the `managesProfilePhotos` branch (§3). Remove the branch first, then the component. |
| `Users.has_paid_subscription`, `subscription_started_at` | Read by `PaidUserMiddleware` and the live Profile screen (§7). |
| `Http\Middleware\TrackReferralCode` (+ `referral.track` alias) | Active on every request; feeds `Referral`/`ContactFormSubmission` attribution. |
| `ReviewController::getReviews()`, `Components/Review.vue` | `POST /reviews` + `GET /api/reviews` are live. |
| `Components/Icon.vue` registry (minus the two unused entries) | Central icon resolver for the redesigned pages. |
| `Pages/Error.vue`, `Pages/{PrivacyPolicy,TermsOfService}.vue` | Error handlers and legal pages, reachable. |
| `routes/web.php`'s `Route::get('user/profile/{id}')` | Already removed in `eed0d46`; Jetstream's own `profile.show` (`GET /user/profile`) is the only registration now — verified via `route:list` and the Ziggy payload. |

---

## 12. Removal plan that cannot break the live site

Ordered so each commit is independently verifiable. **Never** do these as one sweep.

1. **Zero-risk repo hygiene** — `git rm laravel.log` (+ add to `.gitignore`), `public/ransomize.py`,
   `public/ccat/`, `public/img/landing.PNG`, `public/img/workflow.PNG`,
   `public/img/logos/{cisco,docusign,wayfair}.svg`, empty `#dmca-badge` div + stray
   `dmca-validation.html`. No code references (§8).
2. **Frontend dead-code sweep** — delete the 43 files in §1 and the line-level items in §2 + §3's dead
   branches. Keep §11's list. Then delete `Components/LazyImage.vue` (its last consumer was the
   `managesProfilePhotos` branch). Verify: `npx vite build` must still succeed, and the emitted chunk
   list must no longer contain `Dashboard*`, `FullPracticeTest*`, `*TestStart*`, `upgrade2`,
   `ApiTokenManager`, `*Team*`, `VerifyEmail`.
3. **Backend CCAT-only classes** — `QuestionPDF.php`, `QuestionPDFController.php`,
   `PdfDownloadController.php`, `resources/views/pdf/test.blade.php`, the `paid.user` route group
   (`web.php:164-178`) + its middleware alias in `Http/Kernel.php:71`, and the two commented blocks at
   `web.php:110-117` / `web.php:185`; then
   `composer remove codedge/laravel-fpdf fpdf/fpdf barryvdh/laravel-dompdf`.
   Verify `php artisan route:list` loses exactly `generate.question`, `generate.explanation`,
   `download.pdf` and nothing else.
4. **Teams removal (one atomic commit, or nothing)** — `User`: drop `HasTeams` + `MustVerifyEmail`
   import; `JetstreamServiceProvider`: drop the six team bindings **and** `deleteTeamsUsing` + team
   roles; `Actions/Jetstream`: delete the six team actions and rewrite `DeleteUser` without
   `DeletesTeams`; `CreateNewUser`: drop `createTeam()`; delete the 4 models + policy + blade + factory
   + `Pages/Teams/*` + the 7 team tests + `AppLayout::switchToTeam`; add a migration dropping
   `teams`, `team_user`, `team_invitations`, `users.current_team_id`. Verify: account deletion in the
   Profile screen still works, and `php artisan test` goes to 0 failures with ~35 tests.
5. **§6 decision, then act.** Whichever way: the `route('dashboard')` 500 on
   `POST /complete-registration` must be fixed or the route deleted — it is currently a live
   broken-money path.
6. **Dead-but-executing work** — `CreateNewUser::createTeam()` (§5) and the `verified` middleware on
   the auth group (no-op, since `User` does not implement `MustVerifyEmail`).

---

## 13. Correction to the earlier draft of this audit

The first pass claimed `/register` was broken because `route('terms.show')` / `route('policy.show')`
are absent from the Ziggy payload. That is **wrong**: those calls live inside
`v-if="$page.props.jetstream.hasTermsAndPrivacyPolicyFeature"` (§0.5 → `false`), so they never
evaluate. The genuinely broken route reference is `route('dashboard')`.

A second correction: §6 said `/upgrade-account` was "nav-linked". It is not — every nav reference
(`AppLayout.vue:162`, `:299`) is inside an HTML comment, and the only live-looking link was in the
dead `FreePracticeTestStart.vue`. The page was reachable only by direct URL.

---

## 14. Applied pass (2026-02-12, second session)

The §6 ambiguity was resolved by the owner: **the site has no paid functionality**, so the whole
upgrade funnel went rather than being re-scoped. Steps 1–3 of §12 plus the §6 funnel were executed.
**Teams (§5) was deliberately left for its own atomic commit** — it is not CCAT-related and it
carries the `DeleteUser` trap.

### Removed — files
- **Public CCAT material:** `public/ccat/` (7 files incl. answer-key and official test PDFs),
  `public/ransomize.py`, `public/img/landing.PNG`, `public/img/workflow.PNG`,
  `public/img/logos/{cisco,docusign,wayfair}.svg`, `dmca-validation.html`, `laravel.log`
  (log untracked, `laravel.log` + `storage/logs/*.log` added to `.gitignore`).
- **44 unreachable frontend files** — the 43 in §1a–§1d, plus `Components/LazyImage.vue`, which only
  survived because of the `managesProfilePhotos` branches (also removed).
- **CCAT backend:** `QuestionPDF.php`, `QuestionPDFController.php`, `PdfDownloadController.php`,
  `OpenRouterController.php`, `PaidUserMiddleware.php`, `resources/views/pdf/test.blade.php`.
- **Paid funnel (new, per the no-paid-functionality decision):** `UpgradeAccountController.php`,
  `Pages/UpgradeAccount.vue`, `Pages/SubUpgradeAccount.vue`, `ReviewController.php`,
  `Models/Review.php`, `Components/Review.vue`, `Components/Stars.vue` (orphaned once Review went).
- **Broadcast scaffolding:** `app/Providers/BroadcastServiceProvider.php` + `routes/channels.php`
  (provider already commented in `config/app.php:194`; nothing calls `Broadcast::`).

### Removed — code inside surviving files
`routes/web.php` (paid-user group, `upgrade-account` ×3, `complete-registration`, `reviews` ×2,
commented `/dashboard` block, 4 now-unused imports, `canLogin`/`canRegister` props on `/`);
`Http/Kernel.php` (`paid.user` alias); `User.php` (`isSubscribed()`, `subscriptionStartDate()`,
unused `MustVerifyEmail` import, the two paid columns from `$fillable`/`$casts`);
`config/services.php` (`paypal` block); `AppServiceProvider` (dead `component` Inertia share);
`Auth/Register.vue` (`pendingUpgrade` prop + conditional post to the deleted `complete.registration`);
`CustomRegisterController` (that prop); `app.blade.php` (empty `#dmca-badge` div + commented Tawk.to);
`bootstrap.js` (commented Echo/Pusher block); `AppLayout.vue` (`LazyImage` import, both
`managesProfilePhotos` branches, both `hasApiFeatures` links, `switchToTeam()`,
`showingFullPracticeTestSubmenu`, `isSubscribed`, commented upgrade/solutions imports and blocks,
`.nav-icon`); `UpdateProfileInformationForm.vue` (photo section, email-verification block,
subscription fields — now 2 live fields only); plus the unused-import/prop/decl/CSS items in §2
(`Welcome`, `Portfolio`, `Referrals/{Index,PublicIndex}`, four Admin pages, `FlashMessage`, `Icon.vue`
(`CreditCard`/`ReceiptText`), `BusinessSolutionCard`/`SolutionsSection` (`timeline` prop and the
`delay`→`animationDelay` fall-through that was leaking a stray DOM attribute), `CustomerService.vue`,
`app.css` (`[x-cloak]`, duplicate `.transition-colors`).

### Behaviour fixes that came with the removals
- `Http/Middleware/Authenticate.php` redirected unauthenticated visitors to
  `route('upgrade.account')` — a paid page that no longer exists (and would have thrown once the route
  was deleted). Now `route('login')`.
- `GoogleController` did `redirect()->intended('dashboard')` → 404 after Google sign-in. Now `/`.
- Fixed the two broken money paths by deleting them: `POST /complete-registration` (500 on
  `route('dashboard')`) and `POST /api/generate-explanation` (500 — the controller method never existed).

### Verification after the pass
- `php -l` clean on every modified PHP file; `php artisan config:clear` fine.
- `route:list`: **68 → 60** routes; none of the deleted names remain.
- All GET routes re-dispatched through the kernel, guest + authenticated: **23 × 200, 1 × 204,
  15 × 302, 1 × 404 (the intentional fallback)**; the only 404s are unbound `{param}` patterns.
  26 live Inertia components, unchanged set.
- `vite build`: succeeds, **2.5 MB → 2.0 MB** of emitted assets; no CCAT chunks remain; largest
  chunks are now `app` 231 kB, `PageHero` 74 kB (gsap), `AIIntegrations` 45 kB.
- Reachability re-run: **0 unreachable files** under `resources/js` (was 43).
- `php artisan test` against a scratch MySQL DB: **24 passed, 10 failed, 9 skipped — byte-identical to
  the pre-change baseline**; all 10 failures are the Jetstream Teams tests. `user accounts can be
  deleted` still passes.
- `composer remove codedge/laravel-fpdf fpdf/fpdf barryvdh/laravel-dompdf` (vendor dirs gone).

### Still outstanding (intentionally not touched)
1. **Teams cluster (§5)** — one atomic commit; clears all 10 failing tests.
2. **Database vestige** — no destructive migration was added. `users.has_paid_subscription`,
   `users.subscription_started_at`, `users.current_team_id`, the `reviews` table, plus
   `sessions`/`failed_jobs`/`personal_access_tokens`/`teams`/`team_user`/`team_invitations` remain in
   the schema with no code reading them (except the Teams code, which still exists). Dropping the two
   paid columns would erase the record of any legacy lifetime customers — do it only deliberately.
3. **Revoke the dead credentials** in `.env` (untracked, but real): `PAYPAL_CLIENT_ID` / `PAYPAL_SECRET`
   (`PAYPAL_SANDBOX=false`, i.e. live keys) and `OPENROUTER_API_KEY`. Nothing reads them any more.
   Also worth rotating after the `laravel.log` removal, since that log was in git history.
4. **Search Console** — the deleted `/ccat/*.pdf` URLs may still be indexed; they were served straight
   by nginx with no internal links.
5. `composer.json` still pins Laravel 10 (EOL) with 58 open advisories — unrelated to this pass.
