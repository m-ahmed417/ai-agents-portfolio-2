# Project Scope — AI Support Ticket Triage Agent for FlowPilot

## 1. Project Overview

I was hired to design and build an AI-powered support ticket triage agent for **FlowPilot**, a B2B SaaS platform used by small and mid-sized service businesses to manage projects, clients, tasks, billing, reporting, and team collaboration.

The purpose of this project is to improve the first stage of support operations by converting messy inbound customer messages into **strict structured JSON** that can be used for routing, prioritization, and follow-up.

This project will be built in **pure Python** and will compare **OpenAI** and **DeepSeek** on the same ticket-routing task and test set.

---

## 2. Product Scope

### 2.1 Product Definition

**FlowPilot** is a B2B workflow and client-operations SaaS platform for small and mid-sized service businesses. It helps teams manage day-to-day operations from one shared workspace.

### 2.2 Core Product Capabilities In Scope

FlowPilot includes:

- user accounts and login
- shared team workspaces
- client records
- project and task management
- file uploads and attachments
- analytics and reporting dashboards
- subscription billing and invoices
- teammate invitations and role-based access
- notifications
- integrations with tools such as Slack, Google Calendar, Stripe, and Zapier

### 2.3 Target Users

FlowPilot is used by:

- agencies
- consultancies
- operations teams
- virtual assistant businesses
- service-based small and mid-sized companies

### 2.4 Product Interaction Channels In Scope

Users may interact with FlowPilot through:

- the web application
- a mobile-responsive browser experience
- email notifications
- supported third-party integrations

### 2.5 Product Areas Out of Scope

The FlowPilot product scope does **not** include:

- physical goods or shipping
- hardware support
- on-premise deployments
- unrelated customer IT support
- employee HR/internal workplace issues
- supplier or vendor management workflows
- advanced developer platform/API support unless added later

---

## 3. Business Problem

FlowPilot receives inbound support messages that are often:

- messy
- emotional
- incomplete
- vague
- multi-issue
- inconsistent in wording and detail

This makes first-line support triage slower and less consistent.

The business problem is not that the support team lacks skill. The problem is that incoming tickets are unstructured, which creates delays in:

- routing tickets to the correct queue
- identifying urgent issues
- spotting missing information
- deciding the next support action

The goal of this project is to build an AI agent that improves this intake stage.

---

## 4. Role of the Agent

## 4.1 Primary Role

The agent is a **first-line support ticket triage agent**.

Its job is to analyze messy customer support messages and convert them into structured triage data.

## 4.2 What the Agent Must Do

The agent must:

- read informal or unstructured support messages
- identify the primary issue category
- assess urgency
- identify missing information needed for the next support step
- suggest the next support action
- return the result in strict JSON format
- provide a confidence score

## 4.3 What the Agent Is Not Meant To Do

The agent is **not** responsible for:

- fully solving the support issue
- replying directly to customers
- issuing refunds
- making account or billing changes
- fixing product bugs
- executing actions inside FlowPilot
- replacing human judgment in sensitive or high-risk cases

The system is intended to support **triage and routing**, not complete resolution.

---

## 5. Project Objective

The objective of this project is to build a Python-based AI agent that can reliably transform incoming FlowPilot support tickets into a strict structured format containing:

- `category`
- `urgency`
- `missing_information`
- `suggested_next_action`
- `confidence`

This structured output will help support teams triage tickets faster and more consistently.

A secondary objective is to compare **OpenAI** and **DeepSeek** on the same task using the same schema, prompts, and evaluation set.

---

## 6. Ticket Scope

## 6.1 Tickets In Scope

The ticket triage agent should support customer messages related to the following broad support areas:

### Account Access

Examples:

- cannot log in
- password reset not working
- invite link failed
- locked out of workspace
- verification email not arriving
- role/access issue blocking use

### Billing

Examples:

- charged twice
- invoice missing
- subscription canceled incorrectly
- payment failed
- plan change issue
- trial ended unexpectedly
- refund request

### Bugs

Examples:

- dashboard not loading
- task changes not saving
- report export failing
- automation not triggering
- file upload failing
- app freezing
- incorrect product behavior

### How-To / Product Usage

Examples:

- how to invite teammates
- how to export reports
- how to update billing details
- how to create automations
- how to change workspace settings
- how to use an existing feature

### Feature Requests

Examples:

- add dark mode
- improve filters
- allow custom roles
- support recurring templates
- add new dashboard widgets

### Integrations

Examples:

- Slack notifications not sending
- Google Calendar sync broken
- Stripe connection failing
- Zapier automation not working
- webhook-related sync issue

## 6.2 Tickets Out of Scope

The triage agent is not specifically designed for:

- sales inquiries
- partnership requests
- job applications
- spam
- abusive messages with no product issue
- legal complaints
- supplier/vendor issues
- internal employee support
- unsupported product requests outside FlowPilot
- security incident handling beyond identifying urgency and flagging for escalation

Out-of-scope messages may be classified into a fallback category such as `other`, depending on the final taxonomy.

---

## 7. Routing Assumptions

The project will follow these routing assumptions:

- each ticket must receive **one primary category**
- if a message contains multiple issues, the agent should choose the **most actionable** or **most urgent** issue according to the taxonomy rules
- urgency should be based on **business impact**, not emotional tone alone
- missing information should only include details that are genuinely needed for the next support step
- suggested next action should be short, practical, and support-oriented
- confidence should reflect how certain the model is about the structured output

---

## 8. Output Contract

The agent must return strict JSON with the following fields:

```json
{
  "category": "string",
  "urgency": "string",
  "missing_information": ["string"],
  "suggested_next_action": "string",
  "confidence": 0.0
}
```
