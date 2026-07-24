# DocIntel AI – Project Architecture
Version: 2.0

---

# Vision

DocIntel AI is an AI-powered Documentation Intelligence Platform.

It is NOT an AI documentation generator.

The platform helps organizations understand, maintain, improve, analyze and publish documentation throughout the software development lifecycle.

Version 1 delivers a complete AI-powered Documentation Intelligence Platform focused on documentation analysis, generation, quality review and publishing.

The long-term vision is to evolve into a Documentation Operations Platform that combines AI, Documentation Intelligence, Repository Intelligence, Publishing, Governance and Enterprise Collaboration into one unified solution.

---

# Core Product Pillars

The platform is organized around the following intelligence pillars.

## Repository Intelligence

Responsible for understanding documentation repositories.

Capabilities

- Repository Build
- Repository Discovery
- Repository Refresh
- Metadata Extraction
- Repository Inventory
- Repository Dashboard
- Repository Summary
- Knowledge Search

---

## Documentation Intelligence

The central intelligence engine of the platform.

Responsible for

- Context Building
- Repository Search
- Candidate Discovery
- Hybrid Ranking
- Semantic Search
- Documentation Discovery
- Documentation Impact
- Coverage Intelligence
- Knowledge Intelligence

Every module that needs repository intelligence must use this engine.

---

## Screenshot Intelligence

Responsible for understanding software screens.

Modules

- Screenshot Analysis
- Compare Screenshots
- Documentation Impact
- Help Site Impact
- Workflow Studio

Future

- Video Intelligence

---

## Workflow Intelligence

Transforms screenshots into intelligent documentation workflows.

Pipeline

Screenshots

↓

Context Extraction

↓

Workflow Detection

↓

Procedure Generation

↓

Workflow Preview

↓

Export

---

## Gap Analysis

Responsible for identifying documentation gaps between product changes and existing documentation.

Pipeline

Input

↓

Repository Intelligence

↓

Gap Detection

↓

Documentation Action Plan

↓

Documentation Generation

↓

Export

---

## Impact Analysis

Responsible for identifying documentation impacted by product changes using a shared Change Context model.

Supported Inputs

- Manual Input
- CSV
- Excel
- JIRA
- Release Notes

Future Inputs

- PRD
- Meeting Transcript
- Figma

Outputs

- Impacted Articles
- Documentation Recommendations
- Documentation Action Plan
- Generated Documentation
- Export

---

## Documentation Generation

Central document generation capability.

Supported Inputs

- Manual
- JIRA
- JQL
- Sprint
- Epic
- PRD
- Transcript
- Figma
- Workflow Studio
- Gap Analysis
- Impact Analysis

Supported Outputs

- User Guide
- FAQ
- KB Article
- Release Notes
- Solution Article

---

## Style Intelligence

Responsible for documentation quality.

Supports

Built-in

- Microsoft Style Guide
- Google Style Guide
- IBM Style Guide

Custom

- DOCX
- PDF
- URL

Future

- UX Writing Intelligence
- Template Learning
- Compliance Engine

---

## UX Intelligence

Builds on Screenshot Intelligence and Style Intelligence to evaluate the usability and quality of product interfaces.

Capabilities

- UX Writing Review
- Button Label Review
- Terminology Validation
- Accessibility Suggestions
- Screenshot-based UX Analysis
- Style Guide Compliance

---

## AI Workspace

Provides a centralized AI experience for documentation teams.

Capabilities

- Documentation Generation
- Documentation Analysis
- Documentation Summarization
- Documentation Rewriting
- Release Notes Generation
- FAQ Generation
- AI-assisted Documentation Q&A

---

## Analytics Dashboard

Provides operational visibility into platform usage.

Metrics

- Repository Statistics
- Documentation Metrics
- Gap Analysis Activity
- Impact Analysis Activity
- Documentation Generation Activity
- Export Activity
- Recent AI Operations

---

# Shared Platform Components

The platform is built around reusable shared services.

---

## Export Center

Purpose

Reusable documentation export framework.

Supported Formats

- DOCX
- PDF
- HTML
- Markdown
- TXT
- XML
- DITA XML

Future

Publish Center

- Confluence
- SharePoint
- GitHub Pages
- MkDocs
- Zendesk
- Salesforce

---

## Procedure Renderer

Reusable renderer used by all modules generating procedures.

Current Usage

- Workflow Studio

Future

- Documentation Generator
- Impact Analyzer
- Gap Analysis

---

## Notification Framework

Current

- Email Notifications

Future

- In-App Notifications
- Toast Notifications
- Banner Notifications
- Notification Preferences

---

## Background Job Framework

Purpose

Standardize all long-running AI operations.

Current Usage

- Repository Build
- Gap Analysis
- Impact Analysis

Future

- Documentation Generation
- Additional AI Modules

---

## Job Result Framework

Purpose

Reusable framework for displaying AI results.

Supports

- Documentation Action Plan
- Impact Analysis

Future

- Repository Summary
- Generated Documentation
- Additional AI Modules

---

# Architecture Principles

1. Pages contain UI only.

2. Workflows orchestrate business logic.

3. Agents perform individual AI tasks.

4. Documentation Intelligence owns repository intelligence.

5. Repository metadata is stored separately from repository content.

6. Repository content is fetched on demand.

7. Shared functionality belongs in shared/.

8. Export functionality is centralized.

9. Procedure rendering is centralized.

10. Analysis pages do not export documentation.

11. Only final deliverables expose

- Generate Documentation
- Export Center

12. Duplicate business logic is never allowed.

13. Complete file replacements are preferred over partial edits.

14. Every major milestone is committed before the next.

---

# Folder Responsibilities

## app.py

Application entry point.

---

## pages/

User interface only.

Never

- Call OpenAI directly
- Perform repository search
- Execute business logic

---

## workflows/

Business orchestration.

Responsible for coordinating

- Agents
- Documentation Intelligence
- Job Framework

---

## agents/

AI specialists.

Examples

- Screenshot Analyzer
- Metadata Extractor
- Style Checker
- JIRA Parser

Each agent performs a single AI task.

---

## documentation_intelligence/

Platform intelligence engine.

Responsible for

- Search
- Matching
- Ranking
- Context
- Repository Intelligence

---

## repositories/

Repository management.

Responsible for

- Build
- Refresh
- Metadata
- Inventory

---

## ranking/

Hybrid ranking algorithms.

Future

Merged into Documentation Intelligence.

---

## gap_analysis/

Gap-specific logic.

Responsible only for gap analysis.

---

## screenshot_intelligence/

Screenshot-specific intelligence.

Responsible only for screenshot workflows.

---

## job_engine/

Background execution.

Responsible for

- Jobs
- Progress
- Results
- Notifications

---

## shared/

Reusable platform capabilities.

Examples

- Export Center
- Procedure Renderer

---

## utils/

Generic helper functions.

No business logic.

---

## data/

Runtime storage.

Contains

- repositories
- jobs
- logs
- cache
- exports

---

## ARCHIVE/

Legacy implementations.

Never imported.

---

# Execution Pattern

Every module follows the same architecture.

User

↓

Page

↓

Workflow

↓

Agent

↓

Documentation Intelligence

↓

Job Framework

↓

Result Framework

↓

Generate Documentation

↓

Export

---

# Development Standards

Every new feature must

✓ Reuse existing shared components

✓ Avoid duplicate logic

✓ Follow the Job Framework

✓ Follow the Result Framework

✓ Follow Export Center

✓ Follow Procedure Renderer

✓ Maintain modular architecture

---

# Architecture Decision Records (ADR)

Major architectural decisions

ADR-001

Documentation Intelligence is the single repository intelligence engine.

ADR-002

Repository stores metadata only.

Repository content is fetched dynamically.

ADR-003

Export Center is shared across all modules.

ADR-004

Procedure Renderer is shared across all modules.

ADR-005

Analysis pages never export documentation.

Only final deliverables expose Export Center.

ADR-006

Workflow Studio is the reference implementation for AI-assisted documentation workflows.

ADR-007

Knowledge Map is intentionally deferred until the platform foundation is complete.

---

# Engineering Quality Gates

Before every major release

- All long-running operations use the Background Job Framework.
- All results use reusable renderers.
- Export functionality uses the shared Export Center.
- AI outputs are normalized.
- Repository validation completed using real repositories.
- End-to-end testing completed.
- Git checkpoint created.

---

# Version 1 Product Architecture

The Version 1 platform delivers an end-to-end documentation workflow built on reusable platform services.

Repository Intelligence

↓

Documentation Intelligence

↓

Gap Analysis / Impact Analysis

↓

Documentation Generation

↓

UX Intelligence

↓

Publishing

↓

Analytics Dashboard

↓

Authentication

↓

Version 1 Release

Future versions will extend this architecture with enterprise collaboration, advanced AI intelligence and enterprise deployment capabilities while continuing to reuse the shared platform foundation.