# ADR-005: Base Intelligence Job Framework

## Status
Draft

## Purpose

Create a reusable execution framework for all long-running Documentation Intelligence workflows.

## Current Problem

Each intelligence module currently manages its own:

- Job creation
- Progress updates
- Result persistence
- Completion
- Failure handling

This duplicates infrastructure logic.

## Goal

Standardize the lifecycle for all intelligence modules.

Target modules:

- Gap Analysis
- Screenshot Intelligence
- Impact Analysis
- Documentation Generation

Repository Build will be evaluated later.

## Proposed Intelligence Job Lifecycle

1. Initialize Job
   - Create job
   - Register with Job Manager

2. Validate Inputs
   - Validate repository
   - Validate module inputs

3. Prepare Context
   - Load configuration
   - Initialize module resources

4. Execute Intelligence Workflow
   - Module-specific logic
   - Documentation Intelligence Engine
   - AI analysis

5. Report Progress
   - Progress %
   - Current phase
   - Current item
   - Current step

6. Persist Results
   - Save result
   - Register result type

7. Complete Job
   - Mark completed
   - Notify Job Manager

8. Handle Failure
   - Capture exception
   - Mark failed
   - Preserve error details

## Benefits

- No duplicated workflow code
- Consistent progress reporting
- Reusable result handling
- Easier module development
## Base Intelligence Job Responsibilities

The Base Intelligence Job owns:

- Job creation
- Progress reporting
- Result persistence
- Job completion
- Failure handling

The module owns:

- Input validation
- Repository search
- Documentation Intelligence Engine calls
- AI prompts
- Result generation

## Module Interface

Each Intelligence Module must implement:

- validate_inputs()
- execute()
- build_result()

The Base Intelligence Job provides:

- create_job()
- update_progress()
- save_result()
- complete_job()
- fail_job()
## Modules Planned to Inherit

Phase 1
- GapAnalysisJob

Phase 2
- ScreenshotIntelligenceJob
- ImpactAnalysisJob
- DocumentationGenerationJob

Future
- KnowledgeGapAnalysisJob
- StyleComplianceJob
- UXReviewJob

RepositoryBuildJob remains independent until the framework is proven.