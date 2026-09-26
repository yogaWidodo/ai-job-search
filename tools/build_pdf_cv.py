#!/usr/bin/env python3
"""Build customized, ATS-friendly PDF CVs using ReportLab.
Emulates moderncv banking style with crisp typography, precise metrics, and 100% extractable ATS text.
"""

import sys
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
)
from reportlab.pdfgen import canvas

PRIMARY_COLOR = colors.HexColor("#1b4b72")   # moderncv blue
TEXT_DARK = colors.HexColor("#222222")
TEXT_MUTED = colors.HexColor("#555555")
LINE_COLOR = colors.HexColor("#cbd5e1")

class NumberedCanvas(canvas.Canvas):
    """Two-page footer canvas showing 'Yoga Sulistiyo Widodo | Page X of Y'"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(TEXT_MUTED)
        page_text = f"Yoga Sulistiyo Widodo — Page {self._pageNumber} of {page_count}"
        self.drawRightString(A4[0] - 0.5 * inch, 0.35 * inch, page_text)
        self.drawString(0.5 * inch, 0.35 * inch, "Confidential — Prepared for Application")
        self.restoreState()

def create_cv_pdf(output_path: Path, role_type: str = "youtap"):
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=0.5 * inch,
        rightMargin=0.5 * inch,
        topMargin=0.45 * inch,
        bottomMargin=0.5 * inch
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=24,
        textColor=PRIMARY_COLOR,
        alignment=1
    )

    contact_style = ParagraphStyle(
        'DocContact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=TEXT_DARK,
        alignment=1
    )

    section_style = ParagraphStyle(
        'DocSection',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=13,
        textColor=PRIMARY_COLOR,
        spaceBefore=7,
        spaceAfter=2
    )

    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=TEXT_DARK
    )

    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=TEXT_DARK
    )

    job_meta_style = ParagraphStyle(
        'JobMeta',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11,
        textColor=TEXT_MUTED,
        alignment=2
    )

    bullet_style = ParagraphStyle(
        'DocBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=TEXT_DARK,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=2
    )

    story = []

    # 1. Header
    story.append(Paragraph("Yoga Sulistiyo Widodo", title_style))
    story.append(Spacer(1, 3))
    contact_text = (
        "Sleman, DI Yogyakarta / Jakarta Selatan, Indonesia &nbsp;|&nbsp; "
        "+62 882 3318 1003 &nbsp;|&nbsp; "
        "<b>yogawidodo1411@gmail.com</b><br/>"
        "<font color='#1b4b72'>linkedin.com/in/yogawidodo</font> &nbsp;|&nbsp; "
        "<font color='#1b4b72'>github.com/yogaWidodo</font> &nbsp;|&nbsp; "
        "Portfolio: <font color='#1b4b72'>yoga-portofolio-v1-0-0.vercel.app</font>"
    )
    story.append(Paragraph(contact_text, contact_style))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY_COLOR, spaceAfter=5))

    # Tailored configurations
    if role_type == "jpmorgan":
        role_headline = "Software Engineer II (Java, Real-Time Payments & Distributed Systems)"
        summary_text = (
            "<b>Software Engineer</b> with solid production experience designing high-throughput, mission-critical financial "
            "backend services and payment systems. Deep expertise in <b>Java 21, Spring Boot, PostgreSQL, and distributed system resilience</b> "
            "(idempotent transactions, timeouts, and Redis caching). Proven background at AstraPay and Bank Syariah Indonesia (BSI) "
            "delivering payment automations that slashed operational handling time by <b>70%</b> and eliminated SLA breach rates. "
            "Hands-on experience leveraging enterprise AI-assisted engineering workflows, code review rigor, and production telemetry in regulated environments."
        )
        primary_skills = (
            "<b>Backend & Payments:</b> Java (11, 17, 21), Spring Boot, Spring Core, REST APIs, Microservices, Idempotent Transaction Design, "
            "Event-Driven Concepts, Redis Caching, Distributed System Resiliency."
        )
        sec_skills = (
            "<b>Data, Cloud & Quality:</b> PostgreSQL, Oracle DB, SQL Optimization & Indexing, Docker, GCP, Git, CI/CD Automation, "
            "JUnit 5, Mockito, Spring Cloud Contract, Confluence Documentation, Jira."
        )
    elif role_type == "capgemini":
        role_headline = "Java Developer (Spring Boot, Microservices & Cloud)"
        summary_text = (
            "<b>Java Developer</b> with solid production experience designing, developing, and maintaining enterprise-grade "
            "backend applications and microservices. Deep expertise in <b>Core Java, Java 21, Spring Boot, Hibernate/JPA, and PostgreSQL/Oracle DB</b>. "
            "Demonstrated success at AstraPay delivering full-stack merchant banking workflows and resilient microservices that cut operational "
            "turnaround time by <b>70%</b> and eliminated SLA breach rates. Strong hands-on experience in REST API integration, query performance optimization, "
            "Docker containerization on GCP, automated JUnit testing, and frontend exposure with Angular and React."
        )
        primary_skills = (
            "<b>Core Java & Frameworks:</b> Java (11, 17, 21), Spring Boot, Hibernate, Spring Data JPA, Spring Security, Spring MVC, "
            "RESTful API Integration, Microservices Architecture, Clean Architecture, Design Patterns."
        )
        sec_skills = (
            "<b>Databases, Cloud & DevOps:</b> PostgreSQL, Oracle DB, SQL Optimization & Indexing, Redis, Docker, GCP (Cloud Run, GCS), "
            "GitHub Actions CI/CD, Git, Angular (v13–v20), React, JUnit 5, Mockito."
        )
    elif role_type == "apple":
        role_headline = "Software Development Engineer (Java, Spring & Identity Management Systems)"
        summary_text = (
            "<b>Software Engineer</b> specializing in enterprise server-side development, high-availability architecture, and "
            "Identity & Access Management (IAM). Strong background in <b>Java 21, Spring Boot, Hibernate, and relational databases (Oracle, PostgreSQL)</b>. "
            "Demonstrated track record at AstraPay engineering identity verification (KYC/KYB) services, biometric liveness integrations "
            "(VIDA & Verihubs), and robust authentication security with 0% SLA breach rates. Experienced in Docker containerization, REST API contracts, "
            "and production observability at scale."
        )
        primary_skills = (
            "<b>Core Java & Architecture:</b> Core Java, Java 21, Spring Boot, Hibernate, Spring MVC, RESTful API Design & Integration, "
            "Microservices, Object-Oriented Design, Clean Architecture."
        )
        sec_skills = (
            "<b>Security & Identity:</b> Identity & Access Management (IAM), Biometric Verification, Encryption (RSA, PKCS1), PII Data Masking, "
            "JWT Authentication, 24-Hour Brute-Force Lockout Security."
        )
    elif role_type == "hirefeed":
        role_headline = "Fullstack Developer (React, Next.js, TypeScript & Node.js)"
        summary_text = (
            "<b>Fullstack Developer</b> with extensive experience building scalable modern web applications and responsive architectures. "
            "Deep proficiency in <b>TypeScript, React, Next.js (App Router), Node.js, and PostgreSQL</b>. Proven track record leading the development "
            "of high-concurrency web systems including FIF Adventure (1,500+ participants with Supabase Realtime, PL/pgSQL, and property-based testing) "
            "and enterprise PWAs serving 10,000+ users. Skilled in modern state management, Tailwind CSS, REST APIs, and automated CI/CD deployment."
        )
        primary_skills = (
            "<b>Frontend & Mobile:</b> TypeScript, JavaScript, React, Next.js (App Router), Angular (v13–v20), Tailwind CSS, Responsive Design, "
            "Micro-frontends (Native Federation), PWA."
        )
        sec_skills = (
            "<b>Backend & Databases:</b> Node.js, Express, Next.js API Routes, FastAPI, Python, PostgreSQL, Supabase Realtime & Auth, "
            "Redis, Docker, Git, CI/CD Automation."
        )
    elif role_type == "kredivo":
        role_headline = "Android Engineer - SDE 2 (Mobile Platform & Security)"
        summary_text = (
            "<b>Mobile & Software Engineer</b> specializing in native Android development with <b>Kotlin, Android Jetpack, "
            "Clean Architecture, and MVVM</b> within high-volume fintech platforms. Proven track record at AstraPay engineering "
            "end-to-end KYC biometric integrations (<b>VIDA Liveness SDK & ID Fraud Shield</b>), dynamic A/B testing via Remote Config, "
            "and automated testing with <b>Espresso Page Object Model</b>. Bangkit Academy Mobile Development alumnus with a focus on "
            "client-side security, runtime performance, and scalable mobile components."
        )
        primary_skills = (
            "<b>Mobile Engineering:</b> Kotlin, Java, Android SDK, Android Jetpack (Navigation Component, ViewModel, LiveData, "
            "StateFlow, Room, ViewBinding), Jetpack Compose, Single Activity Pattern."
        )
        sec_skills = (
            "<b>Architecture & Testing:</b> MVVM, Clean Architecture, Dagger Hilt (DI), Coroutines & Flow, Retrofit 2, OkHttp 3, "
            "Espresso UI Automation, Page Object Model (POM), Robolectric, MockK, JUnit 5."
        )
    elif role_type == "quikhire":
        role_headline = "Backend Software Developer (Java, Python & Scalable Architecture)"
        summary_text = (
            "<b>Backend Software Engineer</b> with solid production experience designing, developing, and operating "
            "scalable backend services and distributed architectures. Strong hands-on proficiency in <b>Java (Core Java, Java 21, Spring Boot), "
            "Python (FastAPI), and relational databases (PostgreSQL, Oracle)</b>. Track record at AstraPay and BSI engineering automated "
            "backend platforms that reduced operational handling time by <b>70%</b>, halving query execution latencies (10s to 5s), and implementing "
            "distributed caching with Redis. Adept at autonomous remote engineering, cross-functional collaboration, clean code design patterns, "
            "and robust unit testing."
        )
        primary_skills = (
            "<b>Languages & Backend:</b> Java (11, 17, 21), Python, Kotlin, TypeScript, Spring Boot, FastAPI, Spring Data JPA, "
            "RESTful API Design, Microservices, Clean Architecture, Design Patterns."
        )
        sec_skills = (
            "<b>Databases, Cloud & DevOps:</b> PostgreSQL, Oracle DB, Redis Caching, SQL Query Optimization & Indexing, Docker, GCP, "
            "GitHub Actions CI/CD, Git, Linux/Bash, Datadog APM, JUnit 5, Mockito."
        )
    elif role_type == "bri":
        role_headline = "IT Specialist / Developer (Digital Banking, Web & Mobile Platforms)"
        summary_text = (
            "<b>Software Engineer & Product Engineer</b> with solid production experience delivering digital banking, "
            "payment automations, and secure web & mobile platforms. Deep expertise across <b>Java (Spring Boot), Kotlin (Android Jetpack), "
            "TypeScript (React, Next.js, Angular), and SQL (PostgreSQL, Oracle)</b>. Track record at AstraPay and Bank Syariah Indonesia (BSI) "
            "architecting enterprise banking solutions, cutting operational turnaround time by <b>70%</b>, eliminating SLA breaches (<b>22.7% down to 0%</b>), "
            "and halving database query latencies. Proven ability to drive end-to-end SDLC, CI/CD containerization, and secure banking compliance."
        )
        primary_skills = (
            "<b>Web & Mobile Development:</b> Java (11, 17, 21), Kotlin, Spring Boot, React.js, Next.js, TypeScript, Android Jetpack "
            "(MVVM, Coroutines, Flow, Room), RESTful APIs, Microservices, Clean Architecture."
        )
        sec_skills = (
            "<b>Databases, DevOps & Security:</b> PostgreSQL, Oracle DB, SQL Optimization, Redis, Docker, GCP, GitHub Actions CI/CD, "
            "Secure Coding, PII Masking, JUnit 5, Espresso, Agile/Scrum, Product Management Lifecycle."
        )
    elif role_type == "deloitte":
        role_headline = "T&T Consultant - Java Developer (Backend Engineer & Cloud)"
        summary_text = (
            "<b>Java Developer & Consultant</b> with proven production experience engineering scalable backend microservices, "
            "robust middle logic layers, and enterprise cloud solutions. Deep hands-on expertise in <b>Java 21, Spring Boot, "
            "microservices architecture, RESTful APIs, and database engineering (PostgreSQL, Oracle DB)</b>, alongside solid frontend "
            "collaboration (React.js, Next.js). Track record at AstraPay and Bank Syariah Indonesia (BSI) slashing operational handling "
            "time by <b>70%</b>, eliminating SLA breaches, and optimizing database queries (10s to 5s). Experienced in cloud-native platforms "
            "(GCP, Docker), agile delivery, RFC architecture documentation, and presenting technical solutions to cross-functional stakeholders."
        )
        primary_skills = (
            "<b>Backend & Architecture:</b> Java (11, 17, 21), Spring Boot, Spring Core, Spring Data JPA, Microservices Architecture, "
            "RESTful APIs, Middle Logic Layer, Web Servers, Clean Architecture."
        )
        sec_skills = (
            "<b>Cloud, Databases & Frontend:</b> PostgreSQL, Oracle DB, SQL Optimization & Indexing, Redis, Cloud Platforms (GCP, Cloud Run, Docker), "
            "React.js, Next.js, TypeScript, CI/CD Automation, Datadog APM."
        )
    elif role_type == "hired":
        role_headline = "Full-Stack Developer (AI Model Training, Evaluation & Benchmarking)"
        summary_text = (
            "<b>Full-Stack Developer & Machine Learning Engineer</b> specializing in modern <b>JavaScript / TypeScript (React, Next.js, "
            "Node.js, Nest.js)</b> and AI model training, evaluation, and benchmarking. Alumnus of <b>Coding Camp powered by DBS Foundation "
            "(Machine Learning Engineer, 2025)</b> with hands-on experience building AI platforms (SEHATI with LSTM networks & Google Gemini API) "
            "and high-concurrency web systems (FIF Adventure with property-based testing). Skilled in designing high-quality datasets for "
            "supervised fine-tuning (SFT), rigorously benchmarking and ranking model responses, and authoring clear technical rationales."
        )
        primary_skills = (
            "<b>Full-Stack Engineering:</b> TypeScript, JavaScript (ES6+), Node.js, Nest.js, React.js, Next.js (App Router), Angular, "
            "REST APIs, WebSockets/Realtime, Clean & Maintainable Code."
        )
        sec_skills = (
            "<b>AI/ML & Data Engineering:</b> AI Model Evaluation & Benchmarking, Supervised Fine-Tuning (SFT) Datasets, LLM Output Ranking, "
            "Python, FastAPI, Docker, PostgreSQL, Supabase Realtime, Property-Based Testing."
        )
    else:  # youtap / default
        role_headline = "Senior Backend Developer (Digital Wallet & Microservices)"
        summary_text = (
            "<b>Software Engineer</b> with strong production experience architecting, optimizing, and maintaining "
            "scalable backend microservices for digital wallet and enterprise fintech platforms. Deep hands-on expertise "
            "in <b>Java 21, Spring Boot, Spring Data JPA, and PostgreSQL</b>. Demonstrated success at AstraPay designing a "
            "merchant banking change platform that reduced operational handling time by <b>70%</b> and eliminated SLA breach rates "
            "(<b>22.7% to 0%</b>). Experienced in database query profiling, distributed caching with Redis, idempotent transaction design, "
            "and leading engineering squads with rigorous code reviews."
        )
        primary_skills = (
            "<b>Backend Technologies:</b> Java (11, 17, 21), Kotlin, Spring Boot, Spring Data JPA, Spring Security, Spring MVC, "
            "RESTful APIs, Microservices Architecture, Swagger/OpenAPI, FastAPI, Node.js."
        )
        sec_skills = (
            "<b>Databases & Caching:</b> PostgreSQL, Oracle DB, Redis Caching, SQL Query Optimization & Indexing, Hibernate, "
            "Transaction Isolation, Row-Level Locking (<code>FOR UPDATE SKIP LOCKED</code>), Flyway Migration."
        )

    # 2. Professional Summary
    story.append(Paragraph(f"PROFESSIONAL SUMMARY — <i>{role_headline}</i>", section_style))
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 4))

    # 3. Core Competencies
    story.append(Paragraph("TECHNICAL COMPETENCIES", section_style))
    story.append(Paragraph(f"• {primary_skills}", bullet_style))
    story.append(Paragraph(f"• {sec_skills}", bullet_style))
    story.append(Paragraph(
        "• <b>Security, Cloud & Observability:</b> Google Cloud Platform (Cloud Run, GCS, Vertex AI), Docker, "
        "GitHub Actions CI/CD, Datadog APM, Grafana, Biometric Liveness (VIDA, Verihubs), PII Data Masking, JWT Auth.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Testing & Quality Assurance:</b> JUnit 5, Mockito, Spring Cloud Contract, Espresso, Robolectric, "
        "Vitest, Fast-Check (Property-Based Testing).",
        bullet_style
    ))
    story.append(Spacer(1, 4))

    # 4. Professional Experience
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", section_style))

    # --- AstraPay ---
    astrapay_header = [
        [Paragraph("<b>Product Engineer / Software Engineer</b> — PT Astra Digital Arta (AstraPay)", job_title_style),
         Paragraph("Feb 2026 – Present | Jakarta, Indonesia", job_meta_style)]
    ]
    t1 = Table(astrapay_header, colWidths=[5.2 * inch, 2.3 * inch])
    t1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 1)]))
    story.append(t1)

    if role_type == "apple":
        story.append(Paragraph(
            "• <b>Identity & Access Management (KYC/KYB):</b> Architected server-side identity verification services and KYC/KYB pipelines, "
            "ensuring 100% compliance with Bank Indonesia security standards and zero unauthorized access breaches.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Biometric Liveness & Anti-Spoofing:</b> Integrated biometric face verification (VIDA & Verihubs) with server-side validation "
            "against Dukcapil registry, effectively defending identity systems against deepfakes and presentation attacks.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Secure Java Microservices:</b> Developed microservices in Java 21 and Spring Boot (<code>kyc-service</code> & <code>kyb-service</code>) "
            "with RSA asymmetric encryption, token providers, and 24-hour brute-force protection.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Automated Workflows & SLA:</b> Built automated multi-tier approval workflows with centralized audit trails, reducing SLA breach rate from <b>22.7% to 0%</b>.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Observability & Troubleshooting:</b> Monitored production service telemetry using Datadog APM, establishing alerts and resolving latency bottlenecks.",
            bullet_style
        ))
    elif role_type == "jpmorgan":
        story.append(Paragraph(
            "• <b>Real-Time Payment Workflows:</b> Designed and deployed merchant payment automation platform with Java 21, Spring Boot, and PostgreSQL, "
            "reducing operational turnaround time by <b>70%</b>.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Idempotency & Concurrency:</b> Engineered deterministic 90-day validator lock scheduler and idempotent database transactions "
            "to guarantee transfer correctness and prevent race conditions during peak settlement periods.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Fault-Tolerant Microservices:</b> Developed core microservices with automated multi-provider OCR failover (Google Vertex AI to Advance AI) "
            "to maintain 99.99% availability.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Architecture Documentation (RFC):</b> Authored comprehensive RFCs and system design documents in Confluence for payment integrations and API contracts.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Production Observability:</b> Proactively monitored service health, traces, and latency using Datadog APM, participating in incident response.",
            bullet_style
        ))
    elif role_type == "hirefeed":
        story.append(Paragraph(
            "• <b>Modern Frontend & Micro-frontends:</b> Led progressive modernization of internal admin web from Angular 13 to Angular 20, "
            "adopting Micro-frontend architecture (Native Federation), Standalone Components, and esbuild.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Full-Stack Feature Ownership:</b> Built responsive user interfaces and connected them to Java 21 / Spring Boot backend APIs, "
            "reducing operational handling time by <b>70%</b>.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>API Contract Design:</b> Defined clean RESTful API contracts and data models between frontend and backend microservices.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Automated Testing:</b> Built automated UI tests and integration tests to ensure cross-browser consistency and release reliability.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Cross-Functional Delivery:</b> Collaborated with Product, UX, and QA in an Agile/Scrum environment to iterate quickly.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Backend Microservices & Resiliency:</b> Built and maintained backend services in Spring Boot and PostgreSQL, supporting high-throughput transactions.",
            bullet_style
        ))
    elif role_type == "deloitte":
        story.append(Paragraph(
            "• <b>Middle Logic Layer & Integration:</b> Architected and deployed middle logic layer and backend integration services with "
            "Java 21, Spring Boot, and PostgreSQL, slashing operational handling time by <b>70%</b>.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Database Design & Development:</b> Designed relational schemas and multi-tier approval workflows with centralized audit trails, "
            "eliminating operational SLA breach rates (<b>22.7% down to 0%</b>).",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Fault-Tolerant Microservices:</b> Developed resilient backend microservices with automated multi-provider OCR failover "
            "(Google Vertex AI to Advance AI) and 24-hour brute-force protection.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Frontend Collaboration & Contracts:</b> Defined clean RESTful API contracts and cooperated with frontend teams on Angular and React.js "
            "interfaces for seamless enterprise partner handoffs.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Consulting Mindset & RFCs:</b> Authored comprehensive RFC architectural documents and collaborated across business, UX, and QA "
            "to translate complex business requirements into scalable technology solutions.",
            bullet_style
        ))
    elif role_type == "hired":
        story.append(Paragraph(
            "• <b>Full-Stack Engineering & Clean Code:</b> Engineered robust, maintainable full-stack systems with TypeScript, Angular 20, "
            "and Java/Spring microservices, adhering strictly to clean code design patterns and modular architecture.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>AI Model Integration & Evaluation:</b> Integrated multimodal AI services (Google Vertex AI & Advance AI) for automated "
            "document validation, engineering benchmark evaluation pipelines and intelligent fallback mechanisms.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Automated Verification & Datasets:</b> Designed automated multi-tier approval workflows with structured validation schemas, "
            "reducing SLA breach rates from <b>22.7% to 0%</b> and ensuring 100% data integrity.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Rigorous Code Review & Testing:</b> Championed automated testing and peer code reviews, ensuring code readability, "
            "high reusability, and comprehensive test coverage.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Observability & System Diagnostics:</b> Monitored production service telemetry with Datadog APM, analyzing error logs and "
            "optimizing throughput on critical customer-facing endpoints.",
            bullet_style
        ))
    elif role_type == "kredivo":
        story.append(Paragraph(
            "• <b>Biometric Liveness & Anti-Fraud:</b> Integrated VIDA Liveness SDK and ID Fraud Shield into AstraPay Android KYC V5, "
            "hardening biometric identity verification against deepfake and spoofing attacks while maintaining high pass rates.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Dynamic A/B Testing:</b> Engineered client-side experimentation framework using Firebase Remote Config to dynamically "
            "route and measure alternate verification journeys, boosting user conversion.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>UI Automation with Espresso:</b> Designed robust automated test suites using the Page Object Model (POM) and Espresso, "
            "slashing manual QA regression test cycles and preventing release regressions.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Custom Camera & Flow UX:</b> Implemented custom camera preview, fallback manual capture flows, and dynamic state "
            "management across diverse Android device tiers and OS versions.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Full-Stack Feature Ownership:</b> Collaborated with Product, UX, and Risk teams to deliver regulatory compliance "
            "under Bank Indonesia and OJK standards.",
            bullet_style
        ))
    else:  # youtap / default
        story.append(Paragraph(
            "• <b>Merchant Banking Platform Architecture:</b> Designed and deployed full-stack merchant bank account change platform "
            "with Java 21, Spring Boot, and Angular 20 micro-frontend, reducing operational handling time by <b>70%</b>.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>SLA & Automated Workflows:</b> Engineered automated multi-tier approval workflow with centralized audit trails, "
            "reducing operational SLA breach rate from <b>22.7% to 0%</b>.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Transactional Reliability & Locks:</b> Built deterministic 90-day validator lock scheduler and idempotent database transactions "
            "to prevent erroneous settlement transfers and maintain financial correctness.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Resilient Microservices:</b> Developed core microservices (<code>kyb-service</code> & <code>kyc-service</code>) featuring "
            "multi-provider OCR failover (Google Vertex AI to Advance AI) and brute-force protection.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Production Observability:</b> Monitored live services using Datadog APM, configuring log alerts, diagnosing performance "
            "bottlenecks, and managing incident triage.",
            bullet_style
        ))

    story.append(Spacer(1, 3))
    story.append(PageBreak())

    # --- Bank Syariah Indonesia ---
    story.append(Paragraph("PROFESSIONAL EXPERIENCE (CONTINUED)", section_style))
    bsi_header = [
        [Paragraph("<b>Backend Developer – Team Leader (Internship)</b> — PT Bank Syariah Indonesia Tbk.", job_title_style),
         Paragraph("Sep 2024 – Mar 2025 | Yogyakarta, Indonesia", job_meta_style)]
    ]
    t2 = Table(bsi_header, colWidths=[5.2 * inch, 2.3 * inch])
    t2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 1)]))
    story.append(t2)

    story.append(Paragraph(
        "• <b>Engineering Team Leadership:</b> Served as internship squad leader; conducted code reviews, sprint planning, "
        "architectural alignment, and bridged technical communication with Jakarta central office.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Query Performance Optimization:</b> Profiled and halved query execution latency from <b>10 seconds to 5 seconds</b> "
        "on Oracle DB by decomposing excessive multi-table joins and applying targeted indexing.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Distributed Caching:</b> Implemented Redis caching on high-read back-office endpoints, improving throughput by <b>20%</b>.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Secure API Development:</b> Implemented Spring Security, JWT authentication, and comprehensive Swagger documentation for Umroh back-office services.",
        bullet_style
    ))

    story.append(Spacer(1, 4))

    # 5. Featured Projects
    story.append(Paragraph("FEATURED PROJECTS", section_style))
    if role_type == "hirefeed":
        story.append(Paragraph(
            "• <b>FIF Adventure (High-Concurrency Platform):</b> Real-time expedition gamification platform for 1,500+ concurrent users. "
            "Built with Next.js App Router, TypeScript, Tailwind CSS, Supabase Realtime, PL/pgSQL, row-level locking (<code>FOR UPDATE SKIP LOCKED</code>), "
            "and property-based testing (Fast-Check).",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>FIFGROUP Microsite Branch Competition:</b> Enterprise PWA + CMS platform serving ~10,000 employees nationwide. "
            "Built with Next.js, Supabase, Tiptap, and dynamic SheetJS Excel parsing for real-time leaderboards and instant updates.",
            bullet_style
        ))
    elif role_type == "hired":
        story.append(Paragraph(
            "• <b>SEHATI (AI Health Detection & Evaluation Platform):</b> Microservice backend built with Python FastAPI and Docker, serving LSTM neural network "
            "inferences and Google Gemini API recommendations. Engineered model response evaluation pipelines, benchmark testing, and automated ranking.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>FIF Adventure (High-Concurrency Platform & Property-Based Testing):</b> Real-time platform serving 1,500+ users. Engineered with Next.js App Router, "
            "TypeScript, Supabase Realtime, and property-based testing (Fast-Check) to mathematically prove system correctness under thousands of edge cases.",
            bullet_style
        ))
    else:
        story.append(Paragraph(
            "• <b>FIF Adventure (High-Concurrency Platform):</b> Real-time expedition platform serving 1,500+ users. Engineered with Next.js App Router, "
            "Supabase Realtime, PL/pgSQL, row-level locking (<code>FOR UPDATE SKIP LOCKED</code>), and property-based testing (Fast-Check).",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>SEHATI (AI Health Detection Platform):</b> Microservice backend built with Python FastAPI and Docker, serving LSTM neural network "
            "inferences and Google Gemini API recommendations; deployed via CI/CD to Google Cloud Run.",
            bullet_style
        ))

    story.append(Spacer(1, 4))

    # 6. Education & Certifications
    story.append(Paragraph("EDUCATION & CERTIFICATIONS", section_style))
    edu_header = [
        [Paragraph("<b>Universitas Negeri Yogyakarta</b> — Bachelor of Engineering (B.Eng.) in Information Technology", job_title_style),
         Paragraph("Aug 2021 – Aug 2025 | Yogyakarta", job_meta_style)]
    ]
    t3 = Table(edu_header, colWidths=[5.4 * inch, 2.1 * inch])
    t3.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 1)]))
    story.append(t3)
    story.append(Paragraph(
        "• Graduated <b>Cum Laude</b> with GPA: <b>3.80 / 4.00</b>. Relevant Coursework: Software Engineering, Distributed Systems, "
        "Database Architecture, Cloud Computing, Mobile Development.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Bangkit Academy led by Google, GoTo, Traveloka:</b> Mobile Development Cohort (Completed 2023).",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Coding Camp powered by DBS Foundation:</b> Machine Learning Engineer (Completed 2025).",
        bullet_style
    ))

    story.append(Spacer(1, 4))

    # 7. Languages
    story.append(Paragraph("LANGUAGES", section_style))
    story.append(Paragraph("• <b>Indonesian:</b> Native &nbsp;|&nbsp; <b>English:</b> Professional Working Proficiency (C1)", bullet_style))

    # Build document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[SUCCESS] Built PDF CV at: {output_path}")

if __name__ == "__main__":
    cv_dir = Path("cv")
    cv_dir.mkdir(exist_ok=True)
    
    targets = ["youtap", "kredivo", "jpmorgan", "apple", "hirefeed", "capgemini", "quikhire", "bri", "deloitte", "hired"]
    for t in targets:
        out = cv_dir / f"Yoga_Sulistiyo_Widodo_CV_{t.capitalize()}.pdf"
        create_cv_pdf(out, role_type=t)
