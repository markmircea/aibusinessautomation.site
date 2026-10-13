# Dead-code review — CCAT remnants vs. AIBrainLink

Date: 2026-07-XX · Scope: read-only audit, **no code changed**.
Goal: confirm which Crossover Career Assessment Test (CCAT) era artefacts are unreachable from
the current AIBrainLink (aibrainl.ink) surface, so a future cleanup pass can delete them safely.

## How this was determined (not by eyeballing)

1. **Live page set, measured not guessed.** All 68 registered routes were dispatched through the
   real HTTP kernel (guest pass + authenticated pass, fresh app per request, probe DB
   `aibaa_probe` built from the actual 16 migrations). The Inertia `data-page` blob of each
   response was parsed for `"component"`. Result: **27 components are actually rendered by live
   routes** (list in §1).
2. **Import-graph reachability.** `resources/js` (132 `.vue`/`.js` files) was parsed for static,
   re-export and dynamic `import()` specifiers, `@/` alias resolved per `jsconfig.json`, and a BFS
   was run from `app.js` + the 27 live page roots. → **92 reachable, 40 unreachable** (+ `vite-env.d.ts`).
3. **Dynamic-reference sweep.** Grepped for `<component :is>`, `defineAsyncComponent`,
   `resolveComponent`, `import.meta.glob`, and string component maps. Only hits: `Icon.vue`
   (resolves imported lucide icons, not pages) and `app.js`'s `import.meta.glob('./Pages/**/*.vue')`
   (a bundler glob, not a runtime lookup). Nothing looks up pages/components by string, so the
   import graph is trustworthy.
4. **Assets classified by exact filename match** (case-insensitive) against live vs dead sources,
   with `LogoSlider.vue`'s `platforms[]` list treated as the source of truth for `/img/logos/*`.
5. **Backend:** every class under `app/` scanned for inbound references across
   `app/ routes/ config/ database/ tests/ resources/views/ bootstrap/`, then manually reconciled
   against vendor-invoked classes (Fortify/Jetstream actions, middleware, providers).

---

## 1. What is live (keep)

Rendered by registered routes:

```
Welcome, Portfolio, PrivacyPolicy, TermsOfService, Error,
WebDevelopment/{Index,Service}, Solutions/{AIIntegrations,CustomerService,DesktopAutomation,
  DocumentProcessing,FinancialOperations,HrRecruitment,SalesMarketing,SupplyChain},
Referrals/{Index,PublicIndex}, UpgradeAccount,
Admin/{Dashboard,Contacts/Index,Contacts/Show,Referrals/Index,Referrals/Edit},
Auth/{Login,Register,ForgotPassword,ResetPassword,ConfirmPassword,TwoFactorChallenge},
Profile/Show
```

Supporting JS that the BFS proves is load-bearing: `Layouts/{AppLayout,AuthenticatedCard}`,
`Components/{ActionMessage,ApplicationMark,Banner,Checkbox,ConfirmsPassword,DangerButton,
DialogButton,Dropdown,DropdownLink,FlashMessage,InputError,InputField,Label,LazyImage,LoadingSpinner,
Modal,NavLink,Navigation,Pagination,PrimaryButton,ResponsiveNavLink,SectionBorder,SectionTitle,
SwitchTeamDropdown,TextInput,Welcome?no,WebDevelopmentDropdown,DynamicSEO,Footer,Header,
LogoSlider,ReviewSection,GuaranteeBadge,ChatWithFounder,SidePanel,FeatureSection,CopywritingCard,
DynamicText,AnimatedCounter,ProcessTimeline,TrustedBySection}`, `data/webDevelopmentServices.js`.
(Exact list = 92 files in the BFS output; anything not in §2–§4 is live.)

Backend live surface: `routes/web.php` (all non-commented), `routes/api.php`,
controllers `{Admin/*,ContactFormController,CustomRegisterController,GoogleController,
ReferralController,ReviewController}`, models `{User,Contact,Review,Referral}`,
middleware `{HandleInertiaRequests,TrackReferralCode,PaidUserMiddleware}`,
`Actions/Fortify/*`, `Actions/Jetstream/DeleteUser.php`, `Providers/*`.
All 16 migrations are structurally valid; see §6 for tables nothing writes to.

---

## 2. Confirmed dead — delete freely (zero inbound refs from live code)

### 2a. CCAT test pages — 15 files (`resources/js/Pages/`)
`FullTest.vue`, `FullPracticeTest.vue`, `FullPracticeTestStart.vue`, `FreePracticeTestStart.vue`,
`MathLogicTest.vue`, `MathLogicTestStart.vue`, `MathLogicJsonStart.vue`,
`SpatialReasoningTest.vue`, `SpatialReasoningTestStart.vue`, `SpatialReasoningJsonStart.vue`,
`VerbalTest.vue`, `VerbalTestStart.vue`, `VerbalJsonStart.vue`, `Dashboard.vue` (route is commented
out — verified absent from the Ziggy payload), `upgrade2.vue`.

Their routes were already commented out (`routes/web.php:147-167, 185-186`) and no live page links
to `verbal.test`, `math.test`, `full.test`, `free.practice.test`, `generate.pdf`, etc. — verified by
grepping every `route('…')` call in `resources/js` against `php artisan route:list`.

### 2b. CCAT-only components — 15 files (`resources/js/Components/`)
`CompaniesUsingCCAT.vue`, `PracticeWithCCATtest.vue`, `GetHiredAtCrossover.vue`,
`DashboardHeader.vue`, `Definition.vue`, `FAQ.vue`, `LifetimePlan.vue`,
`MathLogicTest.vue`, `SpatialReasoningTest.vue`, `VerbalTest.vue`, `Question.vue`, `Timer.vue`,
`UpgradeAccount.vue` (the *component*; the page of the same name is live),
`ApplicationLogo.vue` (only consumer is `Components/Welcome.vue`; `AppLayout` uses `ApplicationMark.vue`),
`Welcome.vue` (Jetstream stub, nothing imports it).

Each of these is imported **only** by `Pages/Dashboard.vue` or by the §2a test pages.

### 2c. Jetstream scaffolding for disabled features — 9 files
`Pages/Teams/{Create,Show}.vue`, `Pages/Teams/Partials/{CreateTeamForm,DeleteTeamForm,
TeamMemberManager,UpdateTeamNameForm}.vue` — `Features::teams()` is commented out
(`config/jetstream.php:61`), and `route:list` shows **zero** `teams.*` routes.
`Pages/API/{Index.vue,Partials/ApiTokenManager.vue}` — `Features::api()` disabled, no `api-tokens.*`
routes. `Pages/Auth/VerifyEmail.vue` — Fortify `emailVerification()` feature disabled
(`config/fortify.php`), and `User` does not implement `MustVerifyEmail`, so no `verify-email` route
exists. `Components/ConfirmationModal.vue` becomes unreachable once Teams/API go.

### 2d. Public files reachable only by URL guess (currently served by nginx, bypassing all Laravel auth)
`public/ccat/` — 7 files: `CROSSOVERCCAT-TEST3-ANSWERS.pdf`, `-TEST4-ANSWERS.pdf`,
`-TEST5-ANSWERS.pdf`, `CROSSOVERCCAT-TEST5-ANSWERS (1).doc`, `officialCCATtest1.pdf`,
`officialCCATtest2.pdf`, `desktop.ini`. Referenced by **nothing** in `resources/`.
`public/ransomize.py` — CCAT question-shuffler; its inputs (`public/test2.json` … `test20.json`)
no longer exist, so it cannot even run.
`laravel.log` (repo root, tracked, 2,379 lines of WampServer-era CCAT stack traces + personal emails) —
should be untracked + gitignored regardless.

### 2e. Orphan images
`public/img/landing.PNG`, `public/img/workflow.PNG` (referenced nowhere, note the uppercase `.PNG`),
`public/img/logos/{cisco,docusign,wayfair}.svg` (the other 12 logos are in `LogoSlider.vue`'s list).

---

## 3. Dead *behind live routes* — decide, then remove route + controller together

| Live route | Controller | Only caller |
|---|---|---|
| `POST /api/generate-question` | `OpenRouterController::generateQuestion` | `MathLogicTestStart`, `SpatialReasoningTestStart`, `VerbalTestStart` (all §2a) |
| `POST /api/generate-explanation` | `OpenRouterController::generateExplanation` | same three |
| `GET /download-pdf/{filename}` (`paid.user`) | `PdfDownloadController` | **nothing** — and `storage/app/public/` is empty (no PDFs, no `storage:link`) |
| `GET /generate-pdfs` | `QuestionPDFController` + `QuestionPDF.php` (extends FPDF) | route already commented (`web.php:185`) |

`OpenRouterController` also carries CCAT fingerprints: `HTTP-Referer: https://ccattest.com`,
model `claude-3.5-sonnet` for question generation, `OPENROUTER_API_KEY` read via `env()` (breaks
under `config:cache`), and a `$7` lifetime call cap stored in a `config` table.
`ReviewController.php` still contains a duplicated `namespace App\Http\Controllers;` block at
line 84 (merge scar from the port; currently harmless in PHP 8.2).

## 4. The live $49.95 product sells the dead catalogue ⚠️

`/upgrade-account` (`Pages/UpgradeAccount.vue`) is live and linked from the nav in 4 places. Its
own copy sells the CCAT product:

> "Upgrade to Lifetime Access … $49.95 … **10 Full Practice tests with timers (500 Questions,
> Answers and Explanations) from the current CCAT**, 10 Additional Full PDF files with Questions and
> Answers, Detailed Explanations for ALL Questions, Original Tests, Weekly updates with new questions"

and the same strings go into the page's JSON-LD structured data (`value: '49.95'`), i.e. Google is
being told this web-development agency sells CCAT prep.

Everything the paid tier unlocks is §3 — `paid.user` guards only `download-pdf` and the two
OpenRouter endpoints, all of which are unreachable or non-functional. The purchase path is itself
broken: it targets a hardcoded `https://api-m.sandbox.paypal.com` with `'verify' => false`
(`UpgradeAccountController.php:31-36`), and the post-purchase handoff 500s —
`POST /complete-registration` → `Route [dashboard] not defined` (same bug in
`GoogleController::completeGoogleRegistration:178`, since the `dashboard` route is commented out).

So this is not just dead code, it is a **money path with no delivery behind it**. The cleanup PR has
to make a product decision, not just a delete: drop the funnel
(`upgrade.account` + `upgrade.account.process` routes, `UpgradeAccountController`,
`UpgradeAccount.vue`, `PaidUserMiddleware` + `paid.user` registration, the
`has_paid_subscription`/`subscription_started_at` columns written by
`UpgradeAccountController` and `GoogleController::handleExistingUser`, `isSubscribed`/
`SwitchTeamDropdown` usage in `AppLayout`) — or re-scope the paid tier to something that exists.

## 5. Teams cluster — dead by config, but load-bearing in code (needs surgery)

`Features::teams()` is commented out, yet:
- `User` uses `HasTeams` and `current_team_id` is added in `2014_10_12_000000_create_users_table.php`;
- `Actions/Fortify/CreateNewUser.php:44-49` **creates a Team for every signup** (explains the 100
  rows in `teams` / `team_user` on the production DB) and `currentTeam` is never used by any live page;
- `Actions/Jetstream/{AddTeamMember,CreateTeam,DeleteTeam,InviteTeamMember,RemoveTeamMember,
  UpdateTeamName}.php`, `Models/{Team,TeamInvitation,Membership}.php`, `Policies/TeamPolicy.php`
  (no inbound refs), `resources/views/emails/team-invitation.blade.php`, and 7 team feature tests
  (`CreateTeamTest`, `DeleteTeamTest`, `InviteTeamMemberTest`, `LeaveTeamTest`,
  `RemoveTeamMemberTest`, `UpdateTeamMemberRoleTest`, `UpdateTeamNameTest`) all exist solely for the
  disabled feature; `CreateNewUser`'s validation closure references `Team::class`.
- **Landmine in a live file:** `Layouts/AppLayout.vue:23` `switchToTeam()` calls
  `route('current-team.update')`, a route that does **not** exist (0 matches in `route:list`).
  It is harmless today only because the function is never called; `showingFullPracticeTestSubmenu`
  (AppLayout:21) is likewise a declared-but-unused CCAT leftover.
- Related disabled-feature tests: `{Create,Delete,Update}ApiTokenTest`, `ApiTokenPermissionsTest`,
  `EmailVerificationTest` (2 of its 3 tests skip; the third is the "not enabled" assertion).

Removing teams cleanly = delete the 6 actions + 4 models/policy + blade + 7 tests + 6 pages, drop
`HasTeams`/`current_team_id` and the 3 team migrations, and fix `CreateNewUser` + `DeleteUser` +
`AppLayout::switchToTeam` in the same commit.

## 6. Tables nothing writes to

`SESSION_DRIVER=file` → `sessions` table unused. `QUEUE_CONNECTION=sync` → `failed_jobs` unused.
`Features::api()` off and nothing mints tokens → `personal_access_tokens` unused.
`teams`, `team_user`, `team_invitations` → written only at signup (§5).
In use: `users`, `password_reset_tokens` (Fortify resets), `reviews`, `contacts`, `referrals`, `migrations`.

## 7. Build weight this is costing today

`app.js` resolves pages with `import.meta.glob('./Pages/**/*.vue')`, so **all 61 pages compile into
the production bundle today**. The last build emitted, among others: `Dashboard-*.js` 67.9 kB,
`VerbalTestStart` 17.9 kB, `SpatialReasoningTestStart` 17.4 kB, `FullPracticeTest` 10 kB,
`FullTest` 8.6 kB, `MathLogicTest` 4.6 kB — ≈130 kB of dead, CCAT-branded JS shipped as lazy chunks.

## 8. Suggested sequencing (for the cleanup PR, not done here)

1. Untrack `laravel.log`, add it to `.gitignore`; delete `public/ccat/`, `public/ransomize.py`,
   `public/img/{landing.PNG,workflow.PNG}`, the 3 unused logos. Zero code impact.
2. Delete §2a + §2b (30 files) and the already-commented CCAT route blocks in `web.php`.
3. Delete the §3 endpoints + `OpenRouterController` + `PdfDownloadController` +
   `QuestionPDF*` — *after* the §4 product decision, since `paid.user`/`download-pdf` are the
   subscription's only payload.
4. §4: either delete the upgrade funnel or rebuild it around a real deliverable; either way fix the
   `Route [dashboard] not defined` 500s (`web.php` dashboard block, `UpgradeAccountController:80`,
   `GoogleController:178`) — that bug exists today and is reachable by anyone who completes a purchase.
5. §5: remove the teams cluster in one commit (User trait, `CreateNewUser`, `DeleteUser`,
   `AppLayout`, migrations, 7 tests) or commit to keeping it — the half-state is what makes the next
   Jetstream upgrade risky.
6. Re-run `php artisan route:list` + the vite build + `php artisan test` afterwards; expect the
   Jetstream Teams/API/EmailVerification test failures (8 errors, 2 failures) to disappear with §2c/§5.

## 9. Confidence caveats

- Files in §2d are unreachable *from this codebase*, but `/ccat/*.pdf` URLs may still be live on the
  production host and possibly indexed; delete on the server too, and check Search Console.
- `Auth/TwoFactorChallenge.vue` looks unused in a cold session but **is** live (2FA feature enabled);
  keep it.
- `Pages/Auth/VerifyEmail.vue` is dead only while the Fortify feature stays disabled — re-enabling
  email verification resurrects it, so note the dependency rather than silently deleting.
- Reachability proves "nothing in this repo references X", not "no external page links to X".
