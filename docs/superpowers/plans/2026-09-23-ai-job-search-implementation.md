# AI Job Search Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Establish a fully functional, personalized AI Job Search pipeline for Yoga Sulistiyo Widodo with CLI scrapers, profile scoring, and LaTeX CV generation.

**Architecture:** Connects candidate profiling data (`CLAUDE.md`, `01-candidate-profile.md`) to TypeScript job portal CLIs executed via Bun in `.agents/skills/`, evaluating postings using fit scoring criteria, and compiling targeted LaTeX CVs and cover letters.

**Tech Stack:** Bun, TypeScript, Python 3.12 (`pypdf`), LaTeX / ModernCV, Git / GitHub.

## Global Constraints
- Target candidate: Yoga Sulistiyo Widodo (S1 TI UNY Cum Laude, Product Engineer AstraPay, Ex-BSI).
- Target roles: Backend Engineer (Java / Spring Boot), Fullstack Engineer (Next.js / TypeScript), Android Engineer (Kotlin), Solution Architect.
- Locations: Global Remote (Worldwide/US/EU/APAC), Hybrid/Remote Indonesia (Jakarta/Yogyakarta), Relocation (Europe/APAC).
- Single commit and push per feature/task as instructed by the user rule.

---

### Task 1: Runtime Toolchain Setup (Bun & Scraper Dependencies)

**Files:**
- Create: `scripts/test_scrapers.bat`
- Modify: `.agents/skills/*/cli/package.json` (install node_modules via Bun)

**Interfaces:**
- Consumes: System shell & Winget/PowerShell
- Produces: Working `bun` executable and installed CLI packages under `.agents/skills/*/cli/node_modules/`

- [ ] **Step 1: Check and install Bun runtime on Windows**
  Execute: `winget install Oven-sh.Bun --accept-source-agreements --accept-package-agreements` or the official install script.
  Verify: `bun --version` returns version number (e.g. `1.x.x`).

- [ ] **Step 2: Install dependencies across all scraper CLIs**
  Run `bun install` in each directory:
  - `.agents/skills/freehire-search/cli`
  - `.agents/skills/linkedin-search/cli`
  - `.agents/skills/jobindex-search/cli`
  - `.agents/skills/jobnet-search/cli`
  - `.agents/skills/jobbank-search/cli`
  - `.agents/skills/jobdanmark-search/cli`

- [ ] **Step 3: Test scraper CLI invocations**
  Run smoke test on freehire-search:
  `bun run .agents/skills/freehire-search/cli/src/index.ts --help`
  Expected: CLI usage and flag documentation displayed.

- [ ] **Step 4: Commit and Push**
  ```bash
  git add scripts/test_scrapers.bat
  git commit -m "chore: setup bun runtime and install scraper cli dependencies"
  git push origin master
  ```

---

### Task 2: Configure Candidate Master Profile

**Files:**
- Modify: `CLAUDE.md`
- Modify: `.claude/skills/job-application-assistant/01-candidate-profile.md`

**Interfaces:**
- Consumes: Extracted resume data from `documents/cv/experience-for-cv.txt`, `projects.txt`, and PDF files
- Produces: Canonical identity, education, experience, skills, and target preferences in `CLAUDE.md` and `01-candidate-profile.md`

- [ ] **Step 1: Update CLAUDE.md**
  Replace all `[PLACEHOLDER]` tokens with Yoga Sulistiyo Widodo's actual data:
  - Identity, Location (Sleman, DI Yogyakarta & Jakarta Selatan), Contact (`yogawidodo1411@gmail.com`).
  - Education (UNY B.Eng. Information Technology, GPA 3.80 / 4.00, Cum Laude).
  - Professional Experience (AstraPay Product Engineer, BSI Backend Developer Team Leader).
  - Technical Skills (Java 21, Spring Boot, Kotlin, Android Jetpack, Next.js, Angular 20, PostgreSQL, Docker, GCP).
  - Certifications (DBS ML Engineer, Bangkit Mobile Cohort, Bitlabs Junior Data Analyst).

- [ ] **Step 2: Update 01-candidate-profile.md**
  Populate comprehensive profile methodology with detailed achievements, metrics (70% operational time reduction, SLA breach 22.7% -> 0%, query halving 10s -> 5s), and repository links.

- [ ] **Step 3: Verify profile completeness**
  Run grep/check to ensure zero `[PLACEHOLDER]` tokens remain.

- [ ] **Step 4: Commit and Push**
  ```bash
  git add CLAUDE.md .claude/skills/job-application-assistant/01-candidate-profile.md
  git commit -m "feat: configure personal candidate profile and career history"
  git push origin master
  ```

---

### Task 3: Configure Behavioral Profile and Fit Scoring Rules

**Files:**
- Modify: `.claude/skills/job-application-assistant/02-behavioral-profile.md`
- Modify: `.claude/skills/job-application-assistant/04-job-evaluation.md`

**Interfaces:**
- Consumes: Work style from AstraPay & BSI leadership
- Produces: Configured behavioral response patterns and job fit scoring matrix (1-10)

- [ ] **Step 1: Update 02-behavioral-profile.md**
  Document collaboration with cross-functional teams (Product, QA, Security, Ops), RFC and architectural documentation standards, ownership mindset, and mentoring.

- [ ] **Step 2: Update 04-job-evaluation.md**
  Align fit evaluation rubric:
  - Primary criteria: Java/Spring Boot, Next.js/React, Android Kotlin, Solution Architecture.
  - Work mode preferences: Global Remote, Indonesia Remote/Hybrid, International Relocation.
  - Language constraints: Indonesian (Native), English (Professional).

- [ ] **Step 3: Commit and Push**
  ```bash
  git add .claude/skills/job-application-assistant/02-behavioral-profile.md .claude/skills/job-application-assistant/04-job-evaluation.md
  git commit -m "feat: configure behavioral profile and job fit scoring criteria"
  git push origin master
  ```

---

### Task 4: Personalize LaTeX ModernCV Template & ATS Readability Check

**Files:**
- Create: `cv/main_yoga.tex`
- Create: `tests/verify_cv_ats.py`

**Interfaces:**
- Consumes: Candidate data & `pypdf`
- Produces: Compilable LaTeX CV template and ATS parseability verification script

- [ ] **Step 1: Create cv/main_yoga.tex**
  Write a clean `moderncv` LaTeX file containing Yoga's contact, summary, education, AstraPay experience, BSI experience, key projects (FIF Adventure, SEHATI, Microsite), and skills.

- [ ] **Step 2: Write tests/verify_cv_ats.py**
  Create an automated test script that reads compiled PDF or checks template keyword density using `pypdf`.

- [ ] **Step 3: Run ATS verification script**
  Execute: `python tests/verify_cv_ats.py`
  Expected: PASS with keyword match summary.

- [ ] **Step 4: Commit and Push**
  ```bash
  git add cv/main_yoga.tex tests/verify_cv_ats.py
  git commit -m "feat: add personalized LaTeX CV template and ATS verification"
  git push origin master
  ```

---

### Task 5: Live Scraper & Job Fit Evaluation Verification

**Files:**
- Create: `tests/live_scraper_test.py`

**Interfaces:**
- Consumes: Bun runtime and `.agents/skills/`
- Produces: Live job search results and sample fit evaluation report

- [ ] **Step 1: Write test script to query scrapers**
  Write a Python script that invokes `bun run ...` on `freehire-search` or `linkedin-search` to query live postings for "Backend Engineer Java" or "Fullstack Engineer".

- [ ] **Step 2: Run live scraper test**
  Execute: `python tests/live_scraper_test.py`
  Expected: Returns live job listings with titles, companies, locations, and descriptions.

- [ ] **Step 3: Perform sample fit evaluation**
  Evaluate top result against candidate profile, scoring it 1-10 with pros, gaps, and recommendation.

- [ ] **Step 4: Commit and Push**
  ```bash
  git add tests/live_scraper_test.py
  git commit -m "test: verify live scraper execution and job fit evaluation"
  git push origin master
  ```
