# MCQ Platform Complete Documentation

**CRITICAL DEPLOYMENT REQUIREMENT:** Always deploy your changes to Heroku immediately after making any code modifications. Use `git push heroku main` or the deployment scripts provided. Never leave changes uncommitted or undeployed. The production environment must always reflect the latest improvements.

**IMPORTANT INSTRUCTION FOR ALL AGENTS:** Always update this document whenever ANY changes are made to the codebase. This includes frontend changes, backend updates, new features, bug fixes, configuration changes, or modifications to any workflow. This document must remain the single source of truth for the platform's functionality.

## Table of Contents
1. [Platform Overview](#platform-overview)
2. [Core Features](#core-features)
3. [AI-Powered Editing](#ai-powered-editing)
4. [User Interface Components](#user-interface-components)
5. [Backend Architecture](#backend-architecture)
6. [Authentication & Permissions](#authentication-permissions)
7. [Async Processing with Celery](#async-processing-with-celery)
8. [Testing & Automation](#testing-automation)
9. [Deployment & Configuration](#deployment-configuration)

## Platform Overview

The MCQ Platform is a comprehensive neurology question bank system with advanced AI-powered editing capabilities, cognitive reasoning analysis, and personalized learning features. It supports both regular users (residents/students) and staff administrators with different feature sets.

### Access Levels
- **Anonymous Users**: Redirected to login page
- **Authenticated Users**: Full access to study features, bookmarking, notes, flashcards
- **Staff Members**: Additional access to AI editing tools, admin console, and MCQ management

## Core Features

### 1. Question Display & Interaction (`mcq_detail.html`)

#### Answer Selection & Verification
- **Single-choice selection**: Click on any option to select it
- **Answer checking**: "Check Answer" button reveals correct/incorrect status
- **Visual feedback**:
  - ✓ Green checkmark for correct answers
  - ✗ Red X with strikethrough text for incorrect answers
  - Detailed explanation panel appears after answer check
- **Keyboard shortcuts**: Number keys (1-5) for quick option selection

#### Bookmarking System
- **Toggle bookmark**: Star icon in top-right of question panel
- **Review bookmarked**: Dedicated page at `/review_bookmarked/`
- **Persistence**: Bookmarks saved per user account
- **Visual state**: Filled star = bookmarked, outline star = not bookmarked

#### Note-Taking Feature
- **Personal notes**: Text area below question for private annotations
- **Auto-save**: Notes saved on blur or explicit save
- **Character limit**: 1000 characters
- **Markdown support**: Basic formatting preserved

#### Flashcard Creation
- **Quick create**: "Create Flashcard" button after answering
- **Auto-populated**: Front = question stem, Back = correct answer + explanation
- **Review system**: Spaced repetition at `/review_flashcards/`
- **Categories**: Organized by subspecialty

### 2. Learning Enhancement Features

#### ReasoningPal (Cognitive Analysis)
- **Purpose**: Analyzes clinical reasoning patterns
- **Workflow**:
  1. User selects answer and provides reasoning
  2. System analyzes reasoning quality
  3. Provides structured feedback on clinical thinking
- **Async processing**: Uses Celery for OpenAI analysis
- **Session tracking**: Maintains reasoning history

#### Test My Understanding
- **Generate test questions**: AI creates related questions based on current MCQ
- **Difficulty levels**: Easy, Medium, Hard variations
- **Instant feedback**: Immediate scoring with explanations
- **Knowledge gaps**: Identifies weak areas

#### Case-Based Learning
- **MCQ-to-case conversion**: Transform questions into clinical scenarios
- **Interactive cases**: Step-by-step clinical decision making
- **Voice input**: Speech-to-text for responses
- **Session management**: Save/resume case discussions

#### Mock Examinations
- **Timed tests**: Simulate board exam conditions
- **Custom length**: 10, 25, 50, or 100 questions
- **Performance metrics**: Score, time taken, accuracy by topic
- **Review mode**: Post-exam analysis of all answers

### 3. Organization & Navigation

#### Search Functionality
- **Full-text search**: Questions, options, explanations
- **Filters**:
  - Subspecialty (Vascular, Neuromuscular, etc.)
  - Difficulty level
  - Bookmarked only
  - Incorrectly answered
- **Smart ranking**: Relevance-based results

#### Subspecialty Organization
- **Categories**: 15+ neurology subspecialties
- **Breadcrumb navigation**: Home > Subspecialty > Question
- **Progress tracking**: Questions completed per category
- **High-yield topics**: Curated important topics per subspecialty

#### MCQ Management (Staff Only)
- **Hide/Unhide MCQs**: Remove problematic questions from rotation
- **Reclassify**: Change subspecialty assignment
- **Report system**: Users can flag issues with questions
- **Bulk operations**: Import/export MCQ sets

## AI-Powered Editing

### Question Stem Editing (`ai_edit_mcq_question`)
- **Endpoint**: `/mcq/<id>/ai/edit/question/`
- **Model**: GPT-5-mini (maintains quality for comprehensive stem editing)
- **Modes**:
  - Improve clarity
  - Add clinical context
  - Standardize format
- **Validation**:
  - Minimum 20 words
  - Must be a question
  - Clinical relevance check
- **Fallback**: GPT-4o-mini if GPT-5-mini fails

### Options Editing (`ai_edit_mcq_options`)
- **Endpoint**: `/mcq/<id>/ai/edit/options/`
- **Model**: GPT-5-nano (optimized for fast response)
- **Processing**: Async via Celery (avoids 503 timeouts completely)
- **Modes**:
  - **Fill Missing**: Complete incomplete option sets
  - **Improve All**: Enhance all existing options
- **Features**:
  - Async processing with job polling
  - Auto-apply changes option
  - Auto-regenerate explanations after edit
  - Validation for 4-5 options
- **Smart generation**: Plausible USMLE-style distractors
- **Job polling**: 2-second intervals, 80-second timeout
- **Frontend**: Automatic async mode with progress tracking

### Explanation Editing (Unified System)
- **Endpoint**: `/mcq/<id>/ai/edit/explanation/`
- **Two-mode system** (via modal selection):
  1. **Enhance Mode**: Improves existing explanation
     - Preserves original structure
     - Adds missing details
     - Fixes formatting
     - Uses synchronous API

  2. **Rewrite Mode**: Complete regeneration with Agent SDK
     - Uses `@openai/agents` package
     - Async processing via Celery
     - 10-minute timeout for complex generation
     - Structured output with sections:
       - Option Analysis
       - Brief Overview
       - Management (Pharmacological/Non-pharmacological/Counseling)
       - Key Pearls

### Async Job Processing
- **Job creation**: Returns job_id for polling
- **Status endpoint**: `/mcq/ai/explanation-job/<job_id>/`
- **Polling mechanism**:
  - 3-second intervals
  - 60 attempts max (3 minutes)
  - Progress updates in UI
- **Result storage**: Django cache with 1-hour TTL
- **Fallback**: Django database if cache fails

## User Interface Components

### Admin AI Editor (`admin_ai_editor.js`)

#### State Management
```javascript
const state = {
  mcqId: null,
  csrfToken: null,
  endpoints: {},
  modals: {
    instruction: null,
    explanationMode: null
  },
  explanation: {
    lastSuccessfulText: null
  }
}
```

#### Visual Feedback System
- **Loading states**: Spinner overlays with progress text
- **Success messages**: Green toast notifications (auto-dismiss 5s)
- **Warning messages**: Yellow toasts for non-critical issues
- **Error messages**: Red toasts with detailed error info
- **Debug console**: Staff-only logging for troubleshooting

#### Modal Dialogs
1. **Instruction Modal**: Custom instructions for AI
2. **Mode Selection Modal**: Choose enhance vs rewrite
3. **Confirmation Dialogs**: For destructive actions

#### DOM Manipulation
- **Progressive enhancement**: Works without JavaScript
- **AJAX updates**: Partial page refreshes
- **Auto-save indicators**: Visual confirmation of saves
- **Keyboard navigation**: Tab order preserved

### Explanation Rendering

#### Color-Coded Cards
- **Option Analysis**: Blue cards for each option
- **Brief Overview**: Green card for summary
- **Management**: Orange card with subsections
- **Key Pearls**: Purple card for highlights

#### Icon System
- 💊 Pharmacological management
- 🏃 Non-pharmacological management
- 💬 Counseling essentials
- ✓ Correct answer indicator
- ✗ Incorrect answer indicator
- ⭐ Bookmark status
- 🔒 Staff-only features

## Backend Architecture

### Models (`mcq/models.py`)

#### MCQ Model
```python
class MCQ:
    question: TextField
    options: JSONField  # {"A": "text", "B": "text", ...}
    correct_answer: CharField
    unified_explanation: TextField
    subspecialty: CharField
    is_hidden: BooleanField
    created_at: DateTimeField
    updated_at: DateTimeField
```

#### Related Models
- **UserBookmark**: Many-to-many user bookmarks
- **UserNote**: Personal annotations
- **Flashcard**: Generated study cards
- **CognitiveReasoningSession**: ReasoningPal data
- **MCQReport**: User-submitted issues

### Views (`mcq/views.py`)

#### Authentication Decorators
- `@login_required`: Basic authentication
- `@staff_required_json`: Staff + JSON response
- `@staff_member_required`: Staff + HTML response

#### Key View Functions
- `view_mcq`: Main question display
- `check_answer`: Answer verification logic
- `toggle_bookmark`: AJAX bookmark toggle
- `save_note`: Personal note persistence
- `ai_edit_*`: AI editing endpoints
- `regenerate_all_explanations`: Bulk explanation update

### OpenAI Integration (`mcq/openai_integration.py`)

#### Configuration
```python
# Model Configuration (Optimized for Performance)
DEFAULT_MODEL = "gpt-5-mini"  # For question stem editing
OPTIONS_MODEL = "gpt-5-nano"  # For options editing (40% faster)
OPTIONS_FALLBACK_MODEL = "gpt-5-mini"

# GPT-5-nano Optimizations (Applied Nov 2025)
TEMPERATURE = 0.4  # Reduced from 0.6 for consistency
TOP_P = 0.85  # Reduced from 0.9 for focus
MAX_TOKENS = 500  # Reduced from 600 for speed
RETRY_ATTEMPTS = 2  # Reduced from 3 for faster failing

# Timeouts
AGENT_TIMEOUT_SECONDS = 25  # Synchronous
AGENT_BACKGROUND_TIMEOUT_SECONDS = 600  # Async
OPTION_REQUEST_TIMEOUT = 26  # Options-specific timeout
MCQ_USE_AGENT_EXPLANATION = True  # Feature flag
```

#### Key Functions
- `_run_explanation_agent`: Executes Node.js agent
- `generate_explanation_with_agent`: High-level wrapper
- `ai_edit_question`: Question improvement
- `ai_edit_options`: Options generation
- `regenerate_unified_explanation`: Complete rebuild

#### Fallback Strategy
1. Try GPT-5-mini with Responses API
2. Fallback to GPT-4o-mini
3. Fallback to Chat Completions API
4. Return error if all fail

### OpenAI Responses API (New Implementation)

#### Overview
The platform now uses OpenAI's new Responses API, which is a unified, stateful interface that replaces chat completions and assistants. Key features:
- **Stateful conversations**: Maintains context across multiple calls
- **Tool integration**: Built-in web search, file search, and custom functions
- **Multi-modal support**: Text and image inputs with text/JSON outputs
- **400k-token context window** across all GPT-5 models

#### GPT-5 Model Family

| Model | Use Case | Speed | Cost (per 1M tokens) | Best For |
|-------|----------|-------|---------------------|----------|
| **GPT-5** | Complex reasoning, agentic tasks | Medium | $1.25/$10.00 (in/out) | Deep analysis, complex logic |
| **GPT-5-mini** | Well-defined tasks, precise prompts | Fast | $0.25/$2.00 (in/out) | Question editing, balanced tasks |
| **GPT-5-nano** | Short requests, classification | Very Fast | $0.05/$0.40 (in/out) | Options editing, quick tasks |

#### Implementation Details

##### Python Client Setup
```python
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    organization=os.environ.get("OPENAI_ORGANIZATION"),
    project=os.environ.get("OPENAI_PROJECT")
)
```

##### Response Creation
```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[{"type": "text", "content": "Question text"}],
    instructions="System prompt/instructions",
    max_output_tokens=800,
    temperature=0.3,
    top_p=0.85,
    store=False,  # Privacy: don't store responses
    conversation="conv_id"  # Optional for stateful interactions
)
```

##### Key Parameters
- **model**: Choose GPT-5, GPT-5-mini, or GPT-5-nano
- **input**: Text/image content as list of items
- **instructions**: System-level instructions (replaces system messages)
- **max_output_tokens**: Total token limit including reasoning
- **temperature/top_p**: Control randomness (lower = more deterministic)
- **store**: Set to False for HIPAA/privacy compliance
- **conversation**: ID for maintaining state across calls

#### Migration from Chat Completions
- **Endpoint**: Use `/v1/responses` instead of `/v1/chat/completions`
- **Messages format**: Replace with `input` and `instructions`
- **Response parsing**: Access via `response.output[0].content[0].text`
- **Error handling**: Enhanced with reasoning tokens and better fallbacks

#### Optimization Strategies
1. **Model Selection**:
   - GPT-5-nano for options (fast, cheap)
   - GPT-5-mini for questions (balanced)
   - GPT-5 for complex clinical reasoning

2. **Caching**: Identical inputs automatically cached (reduced cost)
3. **Reasoning tokens**: Set `reasoning={"effort":"minimal"}` for cost savings
4. **Batch API**: Submit multiple requests for better throughput

#### Current Implementation Status
- ✅ Question editing: GPT-5-mini with text response
- ✅ Options editing: GPT-5-nano with inline parsing
- ✅ Explanation generation: GPT-5-mini with agent
- ✅ Clinical reasoning: GPT-5-mini with structured output
- ✅ Error handling: Comprehensive logging and fallbacks

## Authentication & Permissions

### User Levels
1. **Anonymous**: No access (redirect to login)
2. **Authenticated**: Study features only
3. **Staff**: Full editing capabilities
4. **Superuser**: Django admin access

### Session Management
- Django session framework
- Remember me: 2-week sessions
- Automatic logout: 24-hour timeout
- CSRF protection: All POST requests

## Async Processing with Celery

### Configuration (`neurology_mcq/celery_app.py`)
```python
broker_url = REDIS_URL  # Heroku Redis
result_backend = 'django-db'  # Avoid SSL issues
task_serializer = 'json'
task_always_eager = False  # True for local testing
```

### Task Definitions (`mcq/tasks.py`)

#### run_explanation_agent_job
- **Purpose**: Background explanation generation
- **Timeout**: 600 seconds
- **Retries**: 0 (no retry on failure)
- **Result storage**: Cache + database fallback

#### process_clinical_reasoning_analysis
- **Purpose**: ReasoningPal analysis
- **Retries**: 3 with exponential backoff
- **Error handling**: Graceful degradation

### Worker Management
- **Procfile**: `worker: cd django_neurology_mcq && celery -A neurology_mcq worker -l info`
- **Scaling**: Heroku dyno scaling
- **Monitoring**: Heroku logs aggregation

## Testing & Automation

### Playwright Tests (`playwright/tests/*.spec.ts`)
- **Login flow**: Authentication verification
- **AI endpoints**: 200/202 response handling
- **Job polling**: Async completion checks
- **Visual regression**: Screenshot comparisons

### Django Unit Tests (`mcq/tests/`)
- **Model tests**: Data integrity
- **View tests**: Permission checks
- **AI integration**: Mocked OpenAI responses
- **Celery tasks**: Eager mode testing

### Coverage Requirements
- Minimum 80% code coverage
- All AI endpoints tested
- Error paths validated
- Edge cases documented

## Deployment & Configuration

### Environment Variables
```bash
# OpenAI
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-5-mini  # Default model for question stems and general use
OPENAI_OPTIONS_MODEL=gpt-5-nano  # Faster model for options editing
OPENAI_OPTIONS_FALLBACK_MODEL=gpt-4o-mini  # Fallback for options
OPENAI_OPTION_REQUEST_TIMEOUT=26  # Timeout for options requests
MCQ_USE_AGENT_EXPLANATION=1
AI_AGENT_TIMEOUT=25
AI_AGENT_BACKGROUND_TIMEOUT=600

# Redis/Celery
REDIS_URL=rediss://...
CELERY_EAGER=false

# Django
SECRET_KEY=...
DEBUG=False
ALLOWED_HOSTS=...
DATABASE_URL=postgres://...
```

### Heroku Deployment
```bash
# Deploy
git push heroku main

# Run migrations
heroku run python django_neurology_mcq/manage.py migrate

# Scale workers
heroku ps:scale worker=1

# View logs
heroku logs --tail --dyno worker
```

### Monitoring
- **Application logs**: Heroku Papertrail
- **Error tracking**: Built-in Django logging
- **Performance**: New Relic APM (optional)
- **Uptime**: Heroku metrics dashboard

## Deployment Process

### Standard Deployment
```bash
# Add all changes
git add .

# Commit with descriptive message
git commit -m "Description of changes"

# REQUIRED: Deploy to Heroku
git push heroku main

# Optional: Restart workers if needed
heroku ps:restart worker --app enigmatic-hamlet-38937-db49bd5e9821
```

### Quick Deployment Scripts
- `./deploy_gpt5_nano_now.sh` - Deploy GPT-5-nano optimizations
- `./deploy_to_heroku_now.sh` - General deployment script
- Always run deployment scripts after making changes

### Performance Optimizations (Nov 2025)
- **GPT-5-nano for options**: 40% faster response (3-5s vs 8-12s)
- **Intelligent caching**: Avoids redundant API calls
- **Medical terminology database**: Smart fallback options
- **Enhanced error handling**: <1% empty responses (down from 10-15%)

## Common Workflows

### Adding a New AI Feature
1. Create endpoint in `views.py` with `@staff_required_json`
2. Add OpenAI integration in `openai_integration.py`
3. Create Celery task if async needed
4. Add frontend handler in `admin_ai_editor.js`
5. Write Playwright test
6. Update this documentation
7. **MANDATORY**: Deploy to Heroku immediately using `git push heroku main`

### Debugging Production Issues
1. Check Heroku logs: `heroku logs --tail`
2. Review worker logs: `heroku logs --dyno worker`
3. Check Redis connection: `heroku redis:cli`
4. Verify environment variables: `heroku config`
5. Test locally with production data

### Database Operations
```bash
# Backup
heroku pg:backups:capture

# Restore locally
heroku pg:backups:download
pg_restore --verbose --clean --no-acl --no-owner -d mcq_dev latest.dump

# Run Django shell
heroku run python django_neurology_mcq/manage.py shell
```

---

**Last Updated**: November 2025
**Version**: 2.2.0 (OpenAI Responses API Integration & Enhanced Error Handling)
**Maintained By**: AI Agents + Development Team

**DEPLOYMENT RULE**: Always deploy changes immediately after making them. Never leave code uncommitted or undeployed.

**REMINDER**: This document must be updated with EVERY change to maintain accuracy. When in doubt, document it!