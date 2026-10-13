<script setup>
import LegalDocument from '@/Components/LegalDocument.vue';

// DRAFT — reviewed by the owner, not by a lawyer.
// Commercial terms use small-agency norms: 40% deposit (50/50 on small jobs),
// 14-day invoices, 30-day defect warranty. Late-payment interest is not a
// chosen figure — it is the statutory rate under Romanian law implementing
// EU Directive 2011/7/EU (ECB reference rate + 8pp) plus the fixed recovery fee.
const sections = [
  {
    heading: 'Who we are',
    paragraphs: [
      'These terms govern your use of this website and any software development services provided by MarkIT S.R.L., a company registered in Romania (Fiscal Code 50900467, Trade Register ROONRC.J2024042186003), trading as AIBrainL.ink. In these terms "we", "us" and "our" refer to MarkIT S.R.L., and "you" refers to the client or website visitor.',
      'Using this website means you accept these terms. If you engage us for project work, a separate signed proposal or statement of work also applies, and takes precedence over these terms wherever the two differ.',
    ],
  },
  {
    heading: 'How engagements work',
    paragraphs: [
      'Enquiries made through this website are not binding on either side. We respond with a written proposal setting out scope, deliverables, assumptions, timeline and price. Work begins once you accept that proposal in writing and any required deposit has cleared.',
      'Estimates given before a proposal — including any figures on this website — are indicative only. Pricing is fixed in the proposal for the scope described there.',
    ],
  },
  {
    heading: 'Payment',
    paragraphs: [
      'We accept PayPal, Stripe and direct bank transfer. Card payments are processed by PayPal or Stripe; bank transfer details are provided on the invoice. We do not store your card details.',
      'Unless the proposal says otherwise, a deposit of 40% is invoiced before work starts and the balance is invoiced against the milestones set out in the proposal, with the final instalment due on delivery. Smaller engagements may be invoiced 50% on signature and 50% on delivery. Invoices are payable within 14 days of issue.',
      'Prices exclude VAT unless stated. VAT is applied where required under Romanian and EU law; reverse charge may apply for VAT-registered clients in other EU member states.',
      'We may pause work on overdue invoices after giving you written notice. Overdue amounts accrue statutory late-payment interest under Romanian law implementing EU Directive 2011/7/EU — the European Central Bank reference rate plus eight percentage points — together with the fixed recovery charge that directive provides for.',
    ],
  },
  {
    heading: 'Scope and change requests',
    paragraphs: [
      'The proposal defines what is included. Work outside it — new features, redesigns, additional integrations, or changes to agreed requirements — is handled as a change request: we quote the additional time and cost, and proceed once you approve it in writing.',
      'We will tell you before doing chargeable work. You will not receive an invoice for work you did not approve.',
    ],
  },
  {
    heading: 'What we need from you',
    paragraphs: [
      'Projects depend on timely input from your side. You agree to provide the content, brand assets, credentials, third-party account access and decisions the project needs, and to respond to review requests within a reasonable time.',
      'You confirm that any material you supply — text, images, logos, data — is yours to use, and does not infringe anyone else\'s rights. Delays caused by outstanding input may move agreed dates and, where they cause us to hold capacity, may affect cost.',
    ],
  },
  {
    heading: 'Intellectual property',
    paragraphs: [
      'On receipt of full payment, ownership of the custom code, designs and assets we produce specifically for your project transfers to you.',
      'This does not cover third-party components. Open-source libraries, frameworks, fonts, stock media and commercial licences remain under their own terms, and any licence fees are yours unless the proposal says otherwise.',
      'We keep ownership of our own pre-existing tools, libraries, internal frameworks and know-how, including anything we developed before the project or use across clients. Where such material is embedded in your deliverables, you receive a perpetual, non-exclusive licence to use it as part of those deliverables.',
      'Unless you ask us not to, we may describe the work and show screenshots in our portfolio and marketing. We will not disclose anything covered by clause 8.',
    ],
  },
  {
    heading: 'Warranty and support',
    paragraphs: [
      'We warrant that deliverables will materially match the specification in the proposal. For 30 days after delivery we will fix defects in our work at no charge. Longer warranty periods can be agreed in the proposal.',
      'That warranty does not cover faults caused by changes made by you or a third party, by third-party services or APIs changing or failing, by hosting or infrastructure we do not manage, or by use outside the intended purpose.',
      'Ongoing maintenance, monitoring, hosting and feature work after the warranty period are available under a separate support agreement.',
    ],
  },
  {
    heading: 'Confidentiality',
    paragraphs: [
      'Each side may receive non-public information from the other. Both sides agree to keep it confidential, use it only for the project, and protect it with reasonable care. This does not apply to information that is already public, was already known, or must be disclosed by law.',
      'This obligation continues after the project ends.',
    ],
  },
  {
    heading: 'Liability',
    paragraphs: [
      'Nothing in these terms limits liability for death or personal injury caused by negligence, for fraud, or for anything else that cannot lawfully be limited.',
      'Subject to that, our total liability arising from an engagement is limited to the total fees you paid us for that engagement. We are not liable for indirect or consequential loss, including lost profit, lost revenue, lost data or business interruption.',
      'We are not liable for failures of third-party services, hosting providers or APIs outside our control.',
    ],
  },
  {
    heading: 'Cancellation and refunds',
    paragraphs: [
      'Either side may end an engagement by giving written notice. If you cancel, you pay for work completed and any non-recoverable third-party costs committed on your behalf up to the cancellation date; anything already invoiced beyond that is refunded.',
      'Deposits cover scheduled capacity and work already started, and are refundable only to the extent that work has not begun. If we cancel other than for non-payment or breach, we refund fees for work not delivered.',
      'Refund requests should be sent to support@aibrainl.ink.',
    ],
  },
  {
    heading: 'Governing law',
    paragraphs: [
      'These terms are governed by Romanian law, and the courts of Romania have exclusive jurisdiction over any dispute. If any clause is found unenforceable, the rest stays in force.',
      'We may update these terms. The version in force for your project is the one published when your proposal was accepted.',
    ],
  },
];
</script>

<template>
  <LegalDocument
    title="Terms of Service"
    description="The terms that govern this website and our software development engagements."
    last-updated="21 September 2026"
    intro="These terms cover both casual use of this website and paid project work. For any engagement, the signed proposal comes first — these terms fill in everything it does not say."
    :sections="sections"
  />
</template>
