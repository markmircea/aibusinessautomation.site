<script setup>
import LegalDocument from '@/Components/LegalDocument.vue';

// DRAFT — reviewed by the owner, not by a lawyer.
// Content below is written against what the code actually does:
//  - contact form stores name, email, company, solution, tech_stack, message,
//    referral_code and emails a copy to the team
//  - referral codes are held in the session by TrackReferralCode middleware
//  - no analytics or advertising tags: the Google Ads tag (AW-1037877088) was
//    removed once it was confirmed no campaigns are running. Only bunny.net
//    fonts load third-party.
//  - there are no user accounts: login, registration and Google OAuth were removed
// Retention periods use common practice for a small B2B agency: 24 months for
// enquiries, 90 days for server logs. The
// accounting figure is statutory, not chosen — confirm the exact split with an
// accountant, as Romanian law treats document types differently.
const sections = [
  {
    heading: 'Who is responsible for your data',
    paragraphs: [
      'This site is operated by MarkIT S.R.L., a company registered in Romania (Fiscal Code 50900467, Trade Register ROONRC.J2024042186003), trading as AIBrainL.ink. We are the data controller for the personal data described here.',
      'For anything in this policy, including requests about your data, contact support@aibrainl.ink.',
    ],
  },
  {
    heading: 'What we collect',
    paragraphs: [
      'When you submit the contact form we collect the information you enter:',
    ],
    list: [
      'Your name, email address and company name',
      'The service you enquired about and the page you enquired from',
      'Any description of your current tech stack you choose to share',
      'Your message',
      'A referral code, if you arrived through a referral link',
    ],
  },
  {
    heading: 'Other data we hold',
    paragraphs: [
      'If you become a client, we hold the billing details needed to invoice you. Card details are handled entirely by PayPal or Stripe and never reach our servers.',
      'Our web server keeps standard access logs (IP address, browser, pages requested) for security and troubleshooting.',
    ],
  },
  {
    heading: 'Why we use it, and our legal basis',
    paragraphs: [
      'We use your data only for the purposes below. Under the GDPR we rely on these legal bases:',
    ],
    list: [
      'To answer your enquiry and prepare a proposal — necessary to take steps at your request before entering a contract',
      'To deliver a project you have engaged us for, and to invoice it — performance of a contract',
      'To keep accounting and tax records — legal obligation under Romanian law',
      'To secure the site and prevent abuse — our legitimate interest',
    ],
  },
  {
    heading: 'Cookies and tracking',
    paragraphs: [
      'We do not display advertising on this site, we do not sell ad space, and we do not run analytics or advertising trackers. No third party profiles you here.',
      'The only cookies this site sets are strictly necessary ones: a session cookie and the CSRF token that protects forms from being submitted by someone else. Neither tracks you across sites, and the ePrivacy Directive does not require consent for them — which is why you will not see a cookie banner.',
      'We load fonts from Bunny Fonts, a privacy-focused provider that sets no cookies and does not log IP addresses for tracking.',
      'If you follow an outbound link from this site, the destination has its own privacy practices, which we do not control.',
    ],
  },
  {
    heading: 'Who we share it with',
    paragraphs: [
      'We do not sell, rent or trade your personal data. We share it only with service providers who help us operate, and only as far as they need:',
    ],
    list: [
      'PayPal and Stripe — payment processing',
      'Our email provider — delivering contact-form notifications and correspondence',
      'Our hosting provider — running the site',
      'Professional advisers and authorities, where the law requires it',
    ],
  },
  {
    heading: 'International transfers',
    paragraphs: [
      'Some providers process data outside the European Economic Area — PayPal and Stripe for payments. Where that happens, transfers rely on the European Commission\'s Standard Contractual Clauses or an adequacy decision.',
      'If you do not pay us, no personal data of yours leaves the EEA through this site.',
    ],
  },
  {
    heading: 'How long we keep it',
    paragraphs: [
      'Contact-form enquiries are kept for 24 months so we can follow up and keep a record of what was discussed, then deleted. Accounting records and invoices are kept for the period Romanian accounting law requires — generally 10 years for accounting registers and financial statements. Server access logs are kept for 90 days.',
      'If you ask us to delete your data and we have no legal reason to keep it, we will.',
    ],
  },
  {
    heading: 'Your rights',
    paragraphs: [
      'Under the GDPR you can ask us to:',
    ],
    list: [
      'Give you a copy of the personal data we hold about you',
      'Correct anything inaccurate',
      'Delete your data, where we have no overriding legal reason to keep it',
      'Restrict or object to how we use it',
      'Provide it in a portable, machine-readable format',
      'Withdraw consent at any time, where we relied on consent',
    ],
  },
  {
    heading: 'How to exercise them, and how to complain',
    paragraphs: [
      'Email support@aibrainl.ink. We respond within one month, as the GDPR requires. We may ask you to confirm your identity first.',
      'If you are not satisfied with our response, you can complain to the Romanian data protection authority, ANSPDCP (Autoritatea Naţională de Supraveghere a Prelucrării Datelor cu Caracter Personal), at dataprotection.ro — or to the supervisory authority in your own EU country.',
    ],
  },
  {
    heading: 'Security and changes to this policy',
    paragraphs: [
      'We protect your data with appropriate technical and organisational measures, including encrypted connections and restricted access. No system is completely secure, but we take this seriously and will notify you and the authorities of any breach that legally requires it.',
      'If we change this policy we will update the date at the top of this page. Material changes will be brought to your attention.',
    ],
  },
];
</script>

<template>
  <LegalDocument
    title="Privacy Policy"
    description="What personal data MarkIT S.R.L. collects through this site, why, and the rights you have over it."
    last-updated="21 September 2026"
    intro="We collect as little as we can, use it only for the reasons listed here, and never sell it. This policy explains what we hold, why we are allowed to hold it, and how to get it changed or removed."
    :sections="sections"
  />
</template>
