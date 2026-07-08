# DocIntel AI - Project Architecture

## Vision

DocIntel AI is a Documentation Intelligence Platform.

It is NOT an AI documentation generator.

Core capabilities:

- Documentation Intelligence
- Gap Analysis
- Screenshot Intelligence
- Impact Analysis
- Style Intelligence
- Documentation Generation
- Knowledge Intelligence

---

# Architecture Principles

1. One responsibility per module.
2. No duplicate logic.
3. Workflows orchestrate only.
4. Pages contain UI only.
5. Agents perform AI tasks only.
6. Documentation Intelligence owns search and matching.
7. Job Engine owns execution.
8. Runtime data never mixes with source code.
9. Old code moves to ARCHIVE, never deleted.
10. Every major change is committed before the next one.

---

# Folder Responsibilities

## app.py

Application entry point.

---

## pages/

Responsible only for Streamlit UI.

Never:

- Call OpenAI directly
- Search repositories
- Perform business logic

Pages call Workflows only.

---

## workflows/

Business orchestration layer.

Responsible for:

- Calling Agents
- Calling Documentation Intelligence
- Calling Job Engine

Never contains AI prompts.

---

## agents/

AI Specialists.

Examples:

- Screenshot Analyzer
- Metadata Extractor
- Style Checker
- JIRA Parser

Agents perform ONE AI task only.

---

## documentation_intelligence/

Central Intelligence Engine.

Owns:

- Context Building
- Repository Search
- Candidate Selection
- Live Article Retrieval
- Ranking
- Documentation Impact Discovery

All modules use this engine.

---

## gap_analysis/

Gap-specific logic only.

No repository search.

No ranking.

---

## repositories/

Repository management.

Responsible for:

- Crawl
- Refresh
- Inventory
- Repository Metadata

---

## job_engine/

Responsible for:

- Jobs
- Progress
- Status
- Notifications
- Results

All long-running processes use BaseIntelligenceJob.

---

## connectors/

External integrations.

Examples:

- JIRA
- Zendesk
- GitHub
- Confluence

---

## ranking/

Ranking algorithms.

Long term this becomes part of Documentation Intelligence.

---

## utils/

Generic reusable helpers.

No business logic.

---

## data/

Runtime storage.

Contains:

- repositories
- jobs
- job_results
- logs
- cache
- exports

---

## ARCHIVE/

Legacy code.

Never referenced by production code.

Never imported.

Only retained for historical purposes.

---

# Execution Flow

User

↓

Page

↓

Workflow

↓

Job Engine

↓

Agent

↓

Documentation Intelligence

↓

Repository

↓

AI Ranking

↓

Job Result

↓

Page

---

# Documentation Intelligence Pipeline

Input

↓

Context Builder

↓

Repository Search

↓

Candidate Selection

↓

Live Content Retrieval

↓

AI Ranking

↓

Impact Detection

↓

Results

---

# Development Rules

- Always prefer complete file replacements.
- Avoid partial code snippets.
- Minimize duplicate logic.
- Reuse existing modules.
- Build once.
- Refactor only when necessary.
- Commit after every completed milestone.

---

# Future Goal

A new developer or ChatGPT conversation should understand the project within 5 minutes by reading this document.