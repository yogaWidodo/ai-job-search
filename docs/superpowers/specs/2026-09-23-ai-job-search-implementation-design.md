# Design Specification: AI Job Search End-to-End Implementation

**Date:** 2026-09-23  
**Author:** Antigravity AI Pair Programmer & Yoga Sulistiyo Widodo  
**Status:** Approved  
**Target Repository:** `yogaWidodo/ai-job-search`  

---

## 1. Overview & Objective

The goal of this implementation is to establish a fully working, personalized end-to-end **AI Job Search** framework for **Yoga Sulistiyo Widodo**, tailored for:
1. **Target Roles**:
   - Backend Engineer / Senior Backend Engineer (Java / Spring Boot / Microservices)
   - Fullstack Engineer (Next.js / TypeScript / React / Node.js)
   - Mobile / Android Engineer (Kotlin / Clean Architecture / Jetpack)
   - Solution Architect / Product Engineer / Tech Lead
2. **Target Work Modes & Locations**:
   - Global Remote (Worldwide, US, Europe, APAC)
   - Remote / Hybrid in Indonesia (Jakarta, Yogyakarta/Sleman)
   - International Relocation (Europe, Singapore, etc.)
3. **Core Workflow**:
   - Scraping & searching live jobs via unified CLI tools (`linkedin-search`, `freehire-search`, and Danish/EU portals).
   - Evaluating job descriptions against candidate skills, preferences, and behavioral attributes (*Fit Rating & Gap Analysis*).
   - Tailoring CVs (LaTeX/ModernCV) and drafting metric-driven cover letters.
   - Practicing mock interview questions tailored to specific job specs.

---

## 2. Architecture & Toolchain Design

```
+-------------------------------------------------------------+
|                     Candidate Data Layer                    |
|  - CLAUDE.md (Master summary & identity)                    |
|  - 01-candidate-profile.md (Detailed experiences & skills)  |
|  - 02-behavioral-profile.md (Leadership & working style)    |
|  - cv/main_yoga.tex (LaTeX ModernCV master template)        |
+-------------------------------------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                     Job Sourcing Layer                      |
|  Runtime: Bun CLI                                           |
|  - .agents/skills/freehire-search/cli (Global ATS Search)   |
|  - .agents/skills/linkedin-search/cli (LinkedIn Jobs API)   |
|  - .agents/skills/jobindex-search/cli (Jobindex Denmark)    |
|  - .agents/skills/jobnet-search/cli (Jobnet STAR DK)        |
+-------------------------------------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                 Evaluation & Generation Layer               |
|  - 04-job-evaluation.md (Fit scoring matrix 1-10)          |
|  - 05-cv-templates.md (Tailoring logic for LaTeX CV)       |
|  - 06-cover-letter-templates.md (Targeted cover letters)    |
|  - pypdf (ATS parseability & keyword density checking)      |
+-------------------------------------------------------------+
```

### Components:
1. **Runtime & Packages**:
   - **Bun**: Installed on Windows via `winget install Oven-sh.Bun` (or PowerShell script) to execute the TypeScript-based CLI tools in `.agents/skills/*/cli/`.
   - **pypdf**: Installed via `pip install pypdf` for parsing PDF CVs and checking ATS readability.
   - **Portal Search CLIs**: Each skill under `.agents/skills/` (`freehire-search`, `linkedin-search`, `jobbank-search`, `jobdanmark-search`, `jobindex-search`, `jobnet-search`) has its dependencies installed via `bun install`.
2. **Thin-Pointer Agent Compatibility**:
   - Compliant with `AGENTS.md`. Antigravity uses tools to execute scrapers and references the canonical prompts under `.claude/`.

---

## 3. Candidate Profile Specification

### 3.1 Personal Details & Identity
- **Name**: Yoga Sulistiyo Widodo
- **Location**: Sleman, DI Yogyakarta & Jakarta Selatan, Indonesia
- **Contact**: `yogawidodo1411@gmail.com` | `+62 882 3318 1003`
- **Profiles**:
  - LinkedIn: `linkedin.com/in/yogawidodo`
  - GitHub: `github.com/yogaWidodo` & `github.com/ap-yoga`
  - Portfolio: `yoga-portofolio-v1-0-0.vercel.app`
- **Languages**:
  - Indonesian: Native
  - English: Professional Working Proficiency / C1

### 3.2 Education
- **Universitas Negeri Yogyakarta** (Aug 2021 – Aug 2025)
  - Bachelor of Engineering (B.Eng.) in Information Technology
  - Honors: Graduated Cum Laude, GPA 3.80 / 4.00

### 3.3 Professional Experience
1. **PT Astra Digital Arta (AstraPay - Astra Financial)** (Feb 2026 – Present)
   - **Role**: Product Engineer / Software Engineer (Platform, KYC/KYB & Merchant Platform)
   - **Key Achievements & Impact**:
     - Developed merchant bank account change platform with Java 21, Spring Boot, PostgreSQL, and Angular 20 micro-frontend, reducing operational handling time by 70%.
     - Engineered automated approval workflow with centralized audit trails, reducing SLA breach rate from 22.7% to 0%.
     - Implemented biometric liveness (VIDA Liveness SDK & ID Fraud Shield) in Android Kotlin KYC V5 with A/B testing and Espresso POM automated testing.
     - Architected multi-provider OCR failover (Google Vertex AI to Advance AI) and brute-force lockout security.
     - Authored RFCs and enterprise solution architecture documentation for Dukcapil Face Recognition and KYB services.
2. **PT Bank Syariah Indonesia Tbk. (BSI)** (Sep 2024 – Mar 2025)
   - **Role**: Backend Developer – Team Leader (Internship)
   - **Key Achievements & Impact**:
     - Led development of Umroh back-office monitoring platform with Java & Kotlin Spring Boot and Oracle DB.
     - Halved query load time from 10s to 5s through indexing and query decomposition.
     - Added Redis caching improving high-read endpoints response time by 20%.
     - Implemented Spring Security, JWT authentication, and Swagger documentation.

### 3.4 Key Projects
- **FIF Adventure**: Real-time gamification platform for 1,500+ users. Next.js, Supabase, PL/pgSQL, row-level locking (`FOR UPDATE SKIP LOCKED`), Fast-Check property-based testing.
- **FIFGROUP Microsite Branch Competition**: Gamified internal competition platform for ~10,000 employees. Next.js, Supabase, PWA + CMS.
- **SEHATI**: AI-powered health detection platform. FastAPI, LSTM, Google Gemini API, Docker, Google Cloud Run.
- **MyAlquran**: Android Kotlin, MVVM, Retrofit, Jetpack Compose / XML.

### 3.5 Certifications & Programs
- Machine Learning Engineer – Coding Camp powered by DBS Foundation (2025)
- Mobile Development Cohort – Bangkit Academy by Google, GoTo, Traveloka (2023)
- Junior Data Analyst – Bitlabs Academy (2024–2025)

---

## 4. Evaluation & Fit Scoring Rules

The evaluation engine ranks job postings on a 1–10 scale:
- **Primary Match Criteria (+)**:
  - Strong requirement for Java / Spring Boot / Microservices architecture.
  - Fullstack opportunities using Next.js, TypeScript, React, PostgreSQL.
  - Android development utilizing Kotlin, Jetpack, MVVM, Clean Architecture.
  - Solution Architecture / System Design / Tech Lead opportunities.
  - Distributed systems, high concurrency, financial technology / fintech, biometric or payment integrations.
- **Deal Breakers (-)**:
  - Strict mandatory requirement for local languages other than English or Indonesian.
  - Strict requirement for 100% on-site presence in locations outside Jakarta/Sleman without relocation or visa sponsorship.

---

## 5. CV & Cover Letter Generation System

1. **LaTeX ModernCV Template (`cv/main_yoga.tex`)**:
   - Clean, professional styling using `moderncv`.
   - Sections: Header, Professional Summary, Technical Skills Matrix, Experience (AstraPay, BSI), Education (UNY), Projects (FIF Adventure, SEHATI, Microsite), Certifications (DBS, Bangkit, Bitlabs).
   - Validated against ATS readability standards using `pypdf`.
2. **Cover Letter Generator**:
   - Focus on problem-solving, quantifiable metrics (70% handling time reduction, SLA breach 22.7% -> 0%, query halving 10s -> 5s).
   - Forward-looking narrative connecting past impact to the target company's challenges.

---

## 6. Verification & Testing Plan

1. **CLI Toolchain Smoke Test**:
   - Verify `bun --version`.
   - Run test commands for `.agents/skills/freehire-search/cli` and `.agents/skills/linkedin-search/cli`.
2. **Live Job Search Test**:
   - Query global remote roles: `bun run start --query "Backend Engineer Java" --remote` (or equivalent CLI flags).
   - Verify output schema and response parsing.
3. **Fit Evaluation Test**:
   - Run a sample fit evaluation against a live job posting to verify the score, pros, gaps, and tailored strategy.
4. **Git Commit Structure**:
   - Commit & push each feature independently to follow user guidelines.
