# Taxonomy Outline — FlowPilot Support Ticket Triage

## 1. Purpose

This document defines the support ticket taxonomy for the FlowPilot AI triage agent.

The taxonomy is designed to make messy inbound customer support messages easier to interpret, classify, and route in a consistent way. Its purpose is to turn unstructured support text into structured triage data that can be used for routing, prioritization, and follow-up by a human support team or downstream system.

This document should define:

- allowed category labels
- allowed urgency levels
- what each label means
- how to handle ambiguous or multi-issue messages
- rules for missing information
- rules for suggested next action

The taxonomy should help ensure that different messages with similar meaning are classified in the same way, even when they are written informally, emotionally, or with missing context. It should also reduce ambiguity during implementation and evaluation by making the classification rules explicit.

---

## 2. Taxonomy Design Principles

### My principles

- categories should be broad enough to cover common FlowPilot support issues, but narrow enough to remain clear and consistent
- each ticket should be assigned exactly one primary category, even if the message mentions multiple issues
- category definitions and boundary rules should minimize overlap so that similar tickets are classified in the same way
- urgency should be based on practical impact on the user or business, not on how emotional or frustrated the message sounds
- the taxonomy should reflect the actual FlowPilot support environment rather than generic support categories
- `other` should be treated as a fallback category and used only when no defined category clearly applies
- missing information should only include details that would genuinely help the next support step
- suggested next actions should be short, practical, and useful for ticket triage rather than full issue resolution

---

## 3. Category Labels

### Allowed category labels

- account_access
- billing
- bug
- how_to
- feature_request
- other

### Notes

These categories were chosen because they cover the most common support issues for a SaaS product like FlowPilot while staying simple enough to classify consistently. The goal is to keep the taxonomy broad enough to handle messy real-world tickets, but narrow enough that each message can usually be assigned one clear primary category. The labels are also designed to reduce overlap: account and payment problems are separated from product problems, usage questions are separated from broken behavior, and new feature ideas are separated from existing functionality. The `other` category is included as a fallback, but it should be used rarely.

---

## 4. Category Definitions

Define each category in one or two sentences.

### `account_access`

Definition: Issues related to login, password reset, lockout, account verification, workspace access, or permissions that prevent the user from accessing part or all of the product.

Examples:

- “I can’t log in and the password reset email never arrives.”
- “My teammate accepted the invite but still can’t access the workspace.”
- “I’m locked out of my account after turning on two-factor authentication.”

Boundary notes:

- Use `account_access` when the main issue is the user being unable to enter or access the product, workspace, or a required area of the product.
- If the user is asking how to change permissions and nothing is broken, prefer `how_to`.
- If login is failing because of a general outage or broken system behavior affecting many areas, consider `bug` only if the issue is clearly a product malfunction rather than an access problem.

---

### `billing`

Definition: Issues related to charges, invoices, subscriptions, renewals, cancellations, payment failures, and refund requests.

Examples:

- “I was charged twice after upgrading my plan.”
- “My invoice for this month still hasn’t shown up.”
- “I canceled last week but my card was billed again today.”

Boundary notes:

- Use `billing` whenever the main problem is about money, subscriptions, invoices, plan changes, payment methods, or refunds.
- Even if the user sounds angry or urgent, keep it in `billing` unless the real problem is that they cannot access the product.
- Do not use `billing` for general questions about how to update a card or change a plan if the user is simply asking for guidance; those may be `how_to`.

---

### `bug`

Definition: The product is not functioning as intended, including crashes, broken workflows, incorrect behavior, failed actions, or visible errors.

Examples:

- “The dashboard freezes every time I try to export a report.”
- “My tasks keep disappearing after I save them.”
- “Uploading a PDF gives me an error on every attempt.”

Boundary notes:

- Use `bug` when an existing feature should work but does not.
- If the user is asking how to use a feature and there is no clear sign that anything is broken, use `how_to` instead.
- If the user wants a new capability that does not exist yet, use `feature_request`, not `bug`.

---

### `how_to`

Definition: The user is asking how to use an existing feature, configure the product, or complete a task in the product, without clearly indicating that something is broken.

Examples:

- “How do I invite a client without giving them full workspace access?”
- “Where can I update our billing email?”
- “How do I set up an automation for overdue tasks?”

Boundary notes:

- Use `how_to` when the user needs guidance, instructions, or clarification about an existing feature.
- If the user says they followed the steps and the feature still does not work, consider `bug`.
- If the user is asking for functionality that does not currently exist, use `feature_request`.

---

### `feature_request`

Definition: The user wants a new feature, enhancement, or product improvement that is not currently available in the product.

Examples:

- “Can you add dark mode please?”
- “It would be great if you supported Discord integration.”
- “I’d love a way to create recurring task templates.”

Boundary notes:

- Use `feature_request` when the user is asking for something new or a product improvement.
- Do not use `feature_request` when the user is describing something that should already work but is broken; that is a `bug`.
- If the user is asking how to use an existing feature, use `how_to` instead.

---

### `other`

Definition: Messages that do not clearly fit into any of the other categories, including unclear, off-topic, or unsupported messages.

Examples:

- “Your company is terrible.”
- “I want to talk to someone about a partnership opportunity.”
- “Are you hiring right now?”

Boundary notes:

- Use `other` only when the message does not clearly belong in `account_access`, `billing`, `bug`, `how_to`, or `feature_request`.
- `other` should be a fallback category, not a default category for vague messages that still point to a real support issue.
- If a message is messy but still clearly about the product, choose the best matching category instead of using `other`.

---

## 5. Category Boundary Rules

Use this section to explain how similar categories should be separated.

### Example boundary questions

- When is something `bug` vs `how_to`?
- When is something `billing` vs `account_access`?
- When is something `feature_request` vs `bug`?
- When should `other` be used?

### Boundary rules

-
-
-
-
- ***

## 6. Multi-Issue Ticket Rules

Many support tickets contain more than one issue. Define how the agent should choose one primary category.

### Decision rule

Choose the **most urgent actionable issue** as the primary category. If urgency is similar across issues, choose the issue that is blocking the user most. If neither issue is clearly more urgent or blocking, choose the issue that support would need to handle first in order to move the ticket forward.

### Multi-issue rules

- assign exactly one primary category, even if the message mentions multiple problems
- prioritize the issue with the highest immediate impact on the user’s ability to use FlowPilot
- if one issue must be resolved before the other can be meaningfully addressed, choose that issue as the primary category
- do not choose a category just because it is mentioned first; choose based on impact and actionability
- if a message includes both a usage question and a broken feature, prefer the broken feature if it is clearly preventing the user from completing a task
- if a message includes both an access issue and another issue, prefer `account_access` when the user cannot get into the product or workspace at all
- if a message includes billing plus another issue, choose `billing` only when the main problem is the charge, invoice, payment, cancellation, or refund itself
- use `other` only if none of the issues clearly fit an existing category

### Example multi-issue cases

#### Case 1

Message:

> I was charged twice this month and now I can’t log in to update my billing details.

Primary category:

- account_access

Why:

- The user is currently blocked from accessing the product, which prevents them from taking action on anything else. Even though there is also a billing issue, support would likely need to restore account access first before the user can continue.

#### Case 2

Message:

> How do I connect Slack? Also, when I try to open automations, the page just crashes.

Primary category:

- bug

Why:

- The ticket includes both a how-to question and a product malfunction. The crash is the more urgent actionable issue because an existing feature appears broken, while the Slack setup question is secondary.

#### Case 3

Message:

> I’d love a dark mode option, and also the export button isn’t working for me.

Primary category:

- bug

Why:

- The message contains both a feature request and a broken existing feature. The export button not working is an immediate product issue that should be triaged first, while the dark mode suggestion is a lower-priority enhancement request.

---

## 7. Urgency Levels

List the final allowed urgency values here.

### Allowed urgency levels

- low
- medium
- high
- critical

### Notes

These urgency levels were chosen to keep prioritization simple, practical, and consistent for a SaaS support environment like FlowPilot. Urgency should reflect the real impact of the issue on the user, team, or business workflow, not just the emotional tone of the message. The goal is to help support quickly distinguish between minor questions, important blockers, and severe incidents that may require escalation.

---

## 8. Urgency Definitions

Define each urgency level clearly.

### `low`

Definition:
Low urgency issues are minor questions, non-blocking inconveniences, or requests that do not prevent meaningful use of the product.

Common signals:

- the user is asking for guidance or clarification
- the issue is cosmetic or minor
- there is no clear blocker or time-sensitive impact

Examples:

- “How do I change the billing email on our account?”
- “Can you add dark mode in a future update?”

Boundary notes:

- Use `low` for feature requests and basic how-to questions unless the message clearly shows an urgent business impact.
- Frustrated wording alone does not make an issue higher urgency.

---

### `medium`

Definition:
Medium urgency issues affect the user’s workflow or create a noticeable problem, but the user may still be able to continue working or use a workaround.

Common signals:

- part of the product is not working as expected
- the issue is inconvenient but not a full blocker
- only one user or one small workflow appears affected

Examples:

- “The dashboard loads very slowly when I open reports.”
- “File upload keeps failing for one project, but the rest of the app still works.”

Boundary notes:

- Use `medium` when the problem is real and needs attention, but it does not appear to completely stop work.
- If the issue blocks a core task with no workaround, consider `high` instead.

---

### `high`

Definition:
High urgency issues significantly block a user’s ability to use FlowPilot or involve an important billing or access problem that needs prompt attention.

Common signals:

- the user cannot complete a key workflow
- the user cannot log in or access an important area
- there is a serious billing/subscription problem
- the issue has clear immediate business impact for one customer or team

Examples:

- “I can’t log in and the password reset link never works.”
- “We were charged twice after upgrading our subscription.”

Boundary notes:

- Use `high` when the issue is materially disrupting the user’s ability to operate.
- Do not automatically use `high` just because the customer says “urgent”; there should be a meaningful blocker or business impact.

---

### `critical`

Definition:
Critical issues involve severe business impact, widespread disruption, security concerns, major data risk, or situations that likely require immediate escalation.

Common signals:

- multiple users or an entire team are affected
- the product appears to be down or unusable
- there are signs of data loss, data exposure, or security risk
- a core workflow is failing at a broad or severe level

Examples:

- “Our whole team is locked out of the workspace.”
- “We can’t access any client data and the dashboard is down for everyone.”

Boundary notes:

- Use `critical` for severe incidents, not ordinary urgent complaints.
- If the issue affects only one user and does not suggest a larger outage, `high` is usually more appropriate.

---

## 9. Urgency Decision Rules

Write rules that explain how urgency should be judged.

### Example rules

- urgency is based on impact, not tone
- a frustrated message is not automatically urgent
- blocked access may increase urgency
- multi-user impact may increase urgency
- security/data-loss indicators may raise urgency significantly

### My urgency rules

- urgency should be based on the practical impact on the user, team, or business workflow
- emotional language, threats to cancel, or rude wording do not automatically increase urgency
- issues that block login, billing control, or a core workflow should usually be `high` or above
- issues affecting multiple users, an entire workspace, or core product availability should be considered for `critical`
- signs of data loss, data exposure, security problems, or major outages should usually be `critical`
- simple usage questions and feature requests should usually be `low` unless the message clearly shows unusual business impact
- partial product issues with workarounds should usually be `medium`
- when in doubt between two urgency levels, choose the lower one unless the message clearly indicates severe business impact

---

## 10. Missing Information Guidelines

Define what counts as missing information.

### Purpose

The `missing_information` field should list the most important details support would need next in order to act on the ticket.

### Rules

- include only information that would help support take the next practical step
- use short noun phrases rather than full sentences
- prioritize the most important missing details first
- include at most 3 to 4 items unless more are truly necessary
- if the message already includes enough detail, the list can be empty
- missing information should be specific to the issue type
- do not request sensitive information that support should not collect in free text

### Things to avoid

- asking for irrelevant personal information
- asking for information the user already provided
- full-sentence explanations instead of short phrases
- overly technical details unless they are actually needed
- requesting passwords, full card numbers, or other unsafe details

### Good examples

- account email
- workspace name
- invoice ID
- screenshot of error
- browser and device
- steps to reproduce

### Bad examples

- more details
- tell us everything
- explain the issue better
- user identity information
- full credit card number

### Category-specific ideas

#### For `account_access`

Useful missing details might include:

- account email
- workspace name
- exact error message
- whether password reset was attempted

#### For `billing`

Useful missing details might include:

- invoice ID
- charge date
- subscription plan
- last four digits of payment method

#### For `bug`

Useful missing details might include:

- steps to reproduce
- browser/device
- screenshot or error message
- affected page or workflow

#### For `how_to`

Useful missing details might include:

- goal the user is trying to accomplish
- workspace role
- feature/page involved

#### For `feature_request`

Useful missing details might include:

- use case
- affected workflow
- why the current setup is insufficient

---

## 11. Suggested Next Action Guidelines

Define what a good `suggested_next_action` should look like.

### Purpose

The `suggested_next_action` field should provide one short, practical next step for support.

### Rules

- write one clear action, not a full support plan
- keep the action short and operational
- make it relevant to the identified category and urgency
- prefer actions that move the ticket forward immediately
- avoid vague language like “assist the customer” or “look into it”
- suggested next action should describe what support should do next, not what the customer feels
- do not include multiple unrelated steps in one action

### Good examples

- verify the account and troubleshoot the password reset flow
- review the billing history and confirm the duplicate charge
- collect reproduction details and test the export failure
- send setup guidance for teammate permissions
- log the feature request for product review

### Bad examples

- help the customer professionally
- fix this issue as soon as possible
- investigate and update the user and engineering and billing
- be empathetic and solve it
- look into the problem

---

## 12. Confidence Guidelines

Define how confidence should be interpreted.

### Purpose

The `confidence` field should reflect how certain the model is that the structured output is correct.

### Rules

- confidence should be a number between 0.0 and 1.0
- higher confidence should be used when the category and urgency are strongly supported by the message
- lower confidence should be used when the message is vague, ambiguous, incomplete, or contains multiple competing issues
- confidence should reflect uncertainty in the classification, not the seriousness of the problem
- very clear tickets should usually have relatively high confidence
- out-of-scope or highly unclear messages should usually have lower confidence

### High-confidence situations

- the user clearly describes one issue type
- the ticket uses direct language like “charged twice” or “password reset email never arrives”
- the message strongly matches one category with little ambiguity

### Low-confidence situations

- the ticket contains several different issues with no clear primary one
- the message is extremely vague, emotional, or missing context
- the issue could reasonably fit more than one category
- the message may belong in `other`

---

## 13. Fallback / `other` Rules

If you include an `other` category, define exactly when it should be used.

### `other` definition

Definition:
`other` is a fallback category for messages that are clearly out of scope, too vague to classify confidently, or do not fit any of the defined FlowPilot support categories.

### Use `other` when

- the message is not really a support issue about FlowPilot
- the message is a sales inquiry, partnership request, job application, or spam
- the message is too unclear to assign a category with reasonable confidence
- the message is abusive or off-topic without a clear product issue
- the message does not fit `account_access`, `billing`, `bug`, `how_to`, or `feature_request`

### Do not use `other` when

- the message is messy but still clearly about billing, access, bugs, usage, or features
- the ticket contains limited information but still points to a clear issue type
- the message includes a real support problem that can be reasonably classified

### Notes

- `other` should be rare
- if the message is borderline but still product-related, prefer the best matching defined category
- low confidence can be used alongside `other` when the issue is unclear

---

## 14. Example Tickets

Create a small starter set of manually labeled example tickets.

### Example 1

Message:

> I can’t log in and the password reset email never shows up.

Category:

- account_access

Urgency:

- high

Why:

- the user is blocked from accessing the product and cannot resolve it through the normal reset flow

Missing information:

- account email
- workspace name

Suggested next action:

- verify the account and troubleshoot the password reset flow

---

### Example 2

Message:

> I was charged twice after upgrading our workspace yesterday.

Category:

- billing

Urgency:

- high

Why:

- this is a billing problem involving duplicate charges and needs prompt review

Missing information:

- invoice ID
- charge date

Suggested next action:

- review the billing history and confirm the duplicate charge

---

### Example 3

Message:

> The dashboard freezes every time I try to export our monthly report.

Category:

- bug

Urgency:

- medium

Why:

- an existing feature is malfunctioning, but the ticket does not clearly indicate a full outage

Missing information:

- browser and device
- screenshot or error message
- steps to reproduce

Suggested next action:

- collect reproduction details and investigate the export failure

---

### Example 4

Message:

> How do I give a contractor access to one client without letting them see billing?

Category:

- how_to

Urgency:

- low

Why:

- the user is asking for guidance on using an existing permissions-related feature

Missing information:

- current workspace role
- client/workspace setup

Suggested next action:

- provide guidance for configuring the correct access settings

---

### Example 5

Message:

> Can you please add dark mode and better filters in the reports page?

Category:

- feature_request

Urgency:

- low

Why:

- the user is asking for product enhancements rather than reporting a broken feature

Missing information:

- primary use case
- reporting workflow affected

Suggested next action:

- log the feature request for product review

---

### Example 6

Message:

> The invite link worked, but my teammate still gets an access denied message when trying to open the workspace.

Category:

- account_access

Urgency:

- high

Why:

- the teammate cannot access the workspace, which blocks intended use

Missing information:

- teammate email
- workspace name
- exact error message

Suggested next action:

- verify the teammate’s access settings and investigate the access denial

---

### Example 7

Message:

> We canceled last week but were billed again today. Please refund this.

Category:

- billing

Urgency:

- high

Why:

- the issue is directly about an incorrect charge and refund request

Missing information:

- subscription plan
- cancellation date
- invoice ID

Suggested next action:

- verify the cancellation status and review the new charge

---

### Example 8

Message:

> Your app is running really slowly today and my automations are delayed, but I can still work.

Category:

- bug

Urgency:

- medium

Why:

- the user reports degraded product behavior, but not a complete blocker

Missing information:

- affected workflow
- workspace name
- approximate start time

Suggested next action:

- gather environment details and investigate the performance issue

---

### Example 9

Message:

> I want to speak to someone about a partnership with your company.

Category:

- other

Urgency:

- low

Why:

- this is not a product support issue and does not fit the support taxonomy

Missing information:

- company name
- partnership topic

Suggested next action:

- route the message to the appropriate non-support contact

---

### Example 10

Message:

> I’d love recurring task templates, but right now the task editor also crashes whenever I add an attachment.

Category:

- bug

Urgency:

- medium

Why:

- the ticket includes both a feature request and a broken existing workflow, and the broken workflow should be triaged first

Missing information:

- browser and device
- attachment type
- steps to reproduce

Suggested next action:

- collect reproduction details and investigate the task editor crash

---

## 15. Open Questions

Use this section to capture anything you have not decided yet.

### Questions

- should integration-related issues eventually become their own category in a later version
- should permissions issues stay inside `account_access` or be split out later
- should refund requests remain inside `billing` or become their own category if they appear frequently
- what confidence ranges should count as low, medium, or high during evaluation
- should very vague product complaints default to `bug` or `other`
- how many missing-information items should be allowed at maximum in the final schema

---
