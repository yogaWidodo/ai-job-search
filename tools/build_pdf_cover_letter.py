#!/usr/bin/env python3
"""Build customized, ATS-friendly PDF Cover Letters using ReportLab.
Matches cover.cls 1-page standard with crisp typography.
"""

from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

PRIMARY_COLOR = colors.HexColor("#1b4b72")
TEXT_DARK = colors.HexColor("#222222")

def create_cover_pdf(output_path: Path, role_type: str = "youtap"):
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=0.65 * inch,
        rightMargin=0.65 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.55 * inch
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=22,
        textColor=PRIMARY_COLOR,
        alignment=0
    )

    contact_style = ParagraphStyle(
        'DocContact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=TEXT_DARK,
        alignment=0
    )

    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13.5,
        textColor=TEXT_DARK,
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'DocBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=TEXT_DARK,
        leftIndent=14,
        firstLineIndent=-9,
        spaceAfter=2.5
    )

    story = []

    # Header
    story.append(Paragraph("Yoga Sulistiyo Widodo", title_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph(
        "yogawidodo1411@gmail.com &nbsp;|&nbsp; +62 882 3318 1003 &nbsp;|&nbsp; "
        "<font color='#1b4b72'>linkedin.com/in/yogawidodo</font> &nbsp;|&nbsp; Jakarta / Yogyakarta, Indonesia",
        contact_style
    ))
    story.append(Spacer(1, 3))
    story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY_COLOR, spaceAfter=8))

    if role_type == "deloitte":
        company = "Deloitte Indonesia (Innovation Cloud Development Center)"
        target_role = "T&T Consultant - Java Developer (Backend Engineer)"
        story.append(Paragraph(f"Dear Hiring Team at {company},", body_style))
        story.append(Paragraph(
            f"I am writing to express my enthusiastic interest in the <b>{target_role}</b> position (Requisition ID: 114800). "
            "With a solid production track record architecting high-performance backend microservices, middle logic layers, and cloud integrations "
            "at AstraPay and Bank Syariah Indonesia (BSI), alongside an honors degree in Information Technology (<b>Cum Laude, GPA 3.80 / 4.00</b>), "
            "I am eager to leverage my engineering discipline and consulting mindset to deliver purpose-led, technology-enabled solutions for Deloitte's enterprise clients.",
            body_style
        ))
        story.append(Paragraph(
            "My technical background and professional achievements directly align with your requirements:",
            body_style
        ))
        story.append(Paragraph(
            "• <b>Middle Logic Layer & Microservices Architecture:</b> Engineered resilient backend microservices using Java 21, Spring Boot, "
            "and PostgreSQL at AstraPay, developing automated partner handoffs that slashed operational handling time by <b>70%</b> and eliminated SLA breach rates (<b>22.7% down to 0%</b>).",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Database Design & Performance Tuning:</b> Profiled and optimized relational databases (Oracle DB and PostgreSQL), halving query "
            "latencies from <b>10 seconds to 5 seconds</b> and implementing Redis distributed caching to handle high-traffic spikes.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Cloud Native & Modern Frontend Synergy:</b> Experienced deploying containerized workloads to Google Cloud Platform (Cloud Run, Docker) "
            "and collaborating with frontend teams across React.js and modern Angular micro-frontends to deliver end-to-end digital solutions.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Consulting Mindset & Architectural Documentation:</b> Authored comprehensive RFCs, system design proposals, and API contracts, "
            "translating complex business problems into clear technical implementations while presenting to cross-functional stakeholders.",
            bullet_style
        ))
        story.append(Spacer(1, 3))
        story.append(Paragraph(
            "Deloitte's dedication to making an impact that matters and solving complex client challenges inspires me. "
            "I welcome the consulting lifestyle, and I am eager to contribute my technical rigor, proactive communication, and problem-solving drive to your project teams.",
            body_style
        ))
    elif role_type == "hired":
        company = "Hired (on behalf of Global AI Technology Client)"
        target_role = "Full-Stack Developer (Remote) - AI Model Training & Evaluation"
        story.append(Paragraph(f"Dear Hiring Team at {company},", body_style))
        story.append(Paragraph(
            f"I am writing to express my strong interest in the <b>{target_role}</b> position. Combining full-stack engineering "
            "proficiency in JavaScript/TypeScript (React, Next.js, Node.js, Nest.js) with formal machine learning credentials "
            "(<b>Coding Camp powered by DBS Foundation - Machine Learning Engineer, 2025</b>), I am excited to build efficient, "
            "high-quality systems to train, evaluate, and benchmark cutting-edge AI models.",
            body_style
        ))
        story.append(Paragraph(
            "My experience directly addresses your needs for rigorous model evaluation, dataset curation, and clean code craftsmanship:",
            body_style
        ))
        story.append(Paragraph(
            "• <b>Full-Stack TypeScript & Node.js Excellence:</b> Extensive experience developing scalable web applications using TypeScript, "
            "React, Next.js (App Router), and Node.js/Nest.js architecture, writing modular, maintainable, and thoroughly tested code.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>AI Model Training, Evaluation & Benchmarking:</b> Engineered the SEHATI AI platform using Python, FastAPI, LSTM neural networks, "
            "and Google Gemini APIs; designed evaluation pipelines to score, benchmark, and rank model outputs with clear technical rationales.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Dataset Curation for Supervised Fine-Tuning:</b> Experienced preparing, cleaning, and structuring task-specific datasets "
            "for model optimization, validating inputs against strict quality rubrics to ensure deterministic model performance.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Property-Based Testing & Mathematical Rigor:</b> Implemented property-based testing (Fast-Check) on FIF Adventure "
            "(serving 1,500+ users), demonstrating deep commitment to verifying edge cases and maintaining zero-defect code standards.",
            bullet_style
        ))
        story.append(Spacer(1, 3))
        story.append(Paragraph(
            "I thrive in autonomous, remote environments and bring exceptional analytical reasoning and structured communication. "
            "I am excited to contribute to the advancement and safety of foundation AI models with your global team.",
            body_style
        ))
    elif role_type == "bri":
        company = "PT Bank Rakyat Indonesia (Persero) Tbk"
        target_role = "BRI IT Specialist (Web & Mobile Developer Track)"
        story.append(Paragraph(f"Kepada Yth. Tim Rekrutmen & Human Capital {company},", body_style))
        story.append(Paragraph(
            f"Melalui surat ini, saya bermaksud untuk mengajukan diri pada posisi <b>{target_role}</b> dalam program "
            "<b>BRILiaN Banking Associate Program (BBAP) - IT External Hire</b>. Dengan latar belakang pendidikan S1 Teknologi Informasi "
            "dari Universitas Negeri Yogyakarta (<b>Lulus Cum Laude, IPK 3.80 / 4.00</b>) serta pengalaman profesional nyata di sektor perbankan "
            "dan fintech (AstraPay dan Bank Syariah Indonesia), saya sangat antusias untuk berkontribusi dalam memperkuat kapabilitas digital BRI.",
            body_style
        ))
        story.append(Paragraph(
            "Rekam jejak teknis dan kepemimpinan saya selaras dengan kompetensi yang dicari pada jalur IT Developer & Product Management:",
            body_style
        ))
        story.append(Paragraph(
            "• <b>Pengembangan Web & Backend Perbankan:</b> Mengembangkan microservices dan platform perbankan menggunakan Java 21, Spring Boot, "
            "dan PostgreSQL di AstraPay, yang berhasil memangkas waktu penanganan operasional sebesar <b>70%</b> dan menekan tingkat SLA breach menjadi <b>0%</b>.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Pengembangan Mobile Android Native:</b> Berpengalaman mengintegrasikan biometrik (VIDA Liveness SDK & ID Fraud Shield) pada alur KYC V5 Android "
            "menggunakan Kotlin, Android Jetpack, dan pengujian otomatis Espresso POM, diperkuat sebagai alumni <b>Bangkit Academy (Google, GoTo, Traveloka)</b>.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Optimasi Performa Database:</b> Di Bank Syariah Indonesia (BSI), memimpin tim pengembang sistem monitoring dashboard, memangkas latensi query "
            "Oracle DB dari <b>10 detik menjadi 5 detik</b> dan mengimplementasikan Redis caching (+20% throughput).",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>End-to-End Product Ownership:</b> Terbiasa mengawal lifecycle produk digital secara menyeluruh (SDLC) dari penyusunan dokumen arsitektur (RFC), "
            "kontrak API, implementasi CI/CD, hingga observability produksi menggunakan Datadog.",
            bullet_style
        ))
        story.append(Spacer(1, 3))
        story.append(Paragraph(
            "Sebagai bank terbesar di Indonesia yang melayani seluruh lapisan masyarakat, komitmen BRI dalam digitalisasi perbankan sangat menginspirasi saya. "
            "Besar harapan saya untuk dapat mendiskusikan bagaimana kompetensi teknis dan dedikasi saya dapat memberikan dampak positif bagi transformasi digital BRI.",
            body_style
        ))
    elif role_type == "quikhire":
        company = "Quik Hire Staffing"
        target_role = "Backend Software Developer (Remote)"
        story.append(Paragraph(f"Dear Hiring Team at {company},", body_style))
        story.append(Paragraph(
            f"I am writing to express my strong interest in the <b>{target_role}</b> position. Having spent my career "
            "engineering scalable backend architectures, high-performance microservices, and reliable data pipelines using "
            "Java and Python, I am enthusiastic about contributing to cutting-edge software solutions for your global technology client.",
            body_style
        ))
        story.append(Paragraph(
            "My experience aligns closely with your core requirements for scalable design, independent execution, and cross-timezone collaboration:",
            body_style
        ))
        story.append(Paragraph(
            "• <b>Scalable Backend Services:</b> Developed resilient microservices in Java 21 and Spring Boot at AstraPay, designing self-service "
            "merchant platforms that reduced operational turnaround time by <b>70%</b> and eliminated SLA breaches (<b>22.7% down to 0%</b>).",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Python & Machine Learning Microservices:</b> Architected backend microservices in Python FastAPI containerized with Docker "
            "and deployed via automated CI/CD pipelines to Google Cloud Run for SEHATI.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Database Optimization & Performance:</b> Profiled and optimized database queries in PostgreSQL and Oracle DB, halving execution "
            "latencies (10s to 5s) and implementing Redis caching (+20% throughput).",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Remote Autonomy & Code Reviews:</b> Experienced working autonomously in distributed team setups, conducting rigorous code reviews, "
            "authoring architectural RFCs, and communicating proactively across cross-functional stakeholders.",
            bullet_style
        ))
        story.append(Spacer(1, 3))
        story.append(Paragraph(
            "I bring strong engineering discipline, rapid problem-solving skills, and a proven track record delivering production-grade software. "
            "I look forward to discussing how my background can support your client's long-term technical objectives.",
            body_style
        ))
    elif role_type == "capgemini":
        company = "Capgemini"
        target_role = "Java Developer"
        story.append(Paragraph(f"Dear Hiring Team at {company},", body_style))
        story.append(Paragraph(
            f"I am writing to express my strong enthusiasm for the <b>{target_role}</b> position at {company} in Singapore. "
            "With deep hands-on expertise developing production-grade enterprise backend systems using Core Java, Spring Boot, "
            "and Hibernate in high-stakes financial environments at AstraPay and Bank Syariah Indonesia (BSI), I am eager to contribute "
            "to Capgemini’s digital transformation projects across global enterprise clients.",
            body_style
        ))
        story.append(Paragraph(
            "Throughout my career as a backend engineer and team leader, I have owned end-to-end SDLC phases while driving technical excellence:",
            body_style
        ))
        story.append(Paragraph(
            "• <b>Enterprise Java & Spring Boot:</b> Architected and maintained core microservices and RESTful APIs using Java 21, Spring Boot, "
            "and Spring Data JPA, reducing merchant operations turnaround time by <b>70%</b> and eliminating SLA breaches (<b>22.7% down to 0%</b>).",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Database Optimization & Performance:</b> Profiled and tuned SQL queries across PostgreSQL and Oracle DB, halving query latency "
            "from <b>10 seconds to 5 seconds</b> and implementing Redis caching (+20% throughput) on high-load endpoints.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Cloud & Containerization:</b> Built automated CI/CD deployment pipelines using GitHub Actions and containerized microservices "
            "with Docker on Google Cloud Platform, ensuring high availability and fault tolerance.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Testing & Team Leadership:</b> Spearheaded peer code reviews and mentored junior developers during my team leadership at BSI, "
            "while enforcing high test coverage with JUnit 5, Mockito, and Contract Verifier.",
            bullet_style
        ))
        story.append(Spacer(1, 3))
        story.append(Paragraph(
            "Capgemini’s collaborative culture and commitment to innovative digital solutions make it an ideal environment for my technical skills. "
            "I welcome the opportunity to discuss how my Java engineering and problem-solving abilities can create tangible impact for your clients.",
            body_style
        ))
    elif role_type == "apple":
        company = "Apple"
        target_role = "Software Development Engineer - Identity Management"
        story.append(Paragraph(f"Dear Hiring Team at {company},", body_style))
        story.append(Paragraph(
            f"I am writing to express my strong interest in the <b>{target_role}</b> position within Apple’s Enterprise Technology "
            "Services group in Singapore. Having spent my software engineering career designing high-security server-side systems, "
            "biometric identity platforms, and microservices in Indonesia's fintech sector at AstraPay, I am deeply inspired by "
            "Apple’s commitment to operating the largest, most trusted Identity Management System in the world.",
            body_style
        ))
        story.append(Paragraph(
            "In my role as Product Engineer at AstraPay, I have taken end-to-end architectural ownership of server-side identity verification "
            "and access workflows using Java 21, Spring Boot, and enterprise relational databases:",
            body_style
        ))
        story.append(Paragraph(
            "• <b>Identity Verification & Biometrics:</b> Engineered server-side orchestration for KYC/KYB identity validation, integrating "
            "VIDA and Verihubs biometric liveness with Dukcapil government registry to prevent presentation attacks and deepfakes.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Cryptographic Security & Access Control:</b> Implemented RSA asymmetric encryption (.pem PKCS1Padding), PII data masking, "
            "and 24-hour brute-force lockout mechanisms to safeguard mission-critical authentication pipelines.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>High-Availability Microservices:</b> Developed core microservices (<code>kyc-service</code> and <code>kyb-service</code>) with automated "
            "multi-provider failover, maintaining continuous availability and zero SLA breaches across peak volumes.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Database Optimization & Performance:</b> Profiled query execution plans across PostgreSQL and Oracle DB, halving query latency "
            "(10s to 5s) and implementing Redis caching to maximize throughput.",
            bullet_style
        ))
        story.append(Spacer(1, 3))
        story.append(Paragraph(
            "Apple's reputation for uncompromising privacy and seamless user experience resonates strongly with my engineering philosophy. "
            "My experience maintaining resilient, regulated identity architectures positions me to make an immediate, lasting contribution to your team.",
            body_style
        ))

    elif role_type == "jpmorgan":
        company = "JPMorganChase"
        target_role = "Software Engineer II - Real-Time Payments"
        story.append(Paragraph(f"Dear Hiring Team at {company},", body_style))
        story.append(Paragraph(
            f"I am writing to express my strong enthusiasm for the <b>{target_role}</b> role within the Corporate & Investment Bank "
            "Real-Time Payments (RTP) organization in Singapore. With hands-on production experience engineering mission-critical payment "
            "microservices at AstraPay and Bank Syariah Indonesia (BSI), I am eager to contribute to JPMorganChase’s world-class payment rails.",
            body_style
        ))
        story.append(Paragraph(
            "At AstraPay, I have owned payment and settlement automations from discovery to production observability, aligning directly with your requirements:",
            body_style
        ))
        story.append(Paragraph(
            "• <b>Real-Time Payment Architecture:</b> Architected and deployed merchant banking automation platforms using Java 21, Spring Boot, "
            "and PostgreSQL, slashing operational turnaround time by <b>70%</b> and eliminating SLA breaches (<b>22.7% down to 0%</b>).",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Distributed System Resilience:</b> Engineered deterministic 90-day validator lock schedulers and idempotent database transactions "
            "to prevent erroneous transfers and race conditions during high-volume settlement cycles.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Caching & Query Optimization:</b> Implemented Redis distributed caching (+20% throughput) and halved query execution latency (10s to 5s) "
            "by decomposing excessive database joins in high-volume banking environments.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Responsible AI-Augmented Engineering:</b> Regularly utilize modern AI-assisted engineering workflows (code generation, unit test creation, "
            "and Confluence RFC drafts) while maintaining strict peer code review standards and test coverage.",
            bullet_style
        ))
        story.append(Spacer(1, 3))
        story.append(Paragraph(
            "JPMorganChase’s leadership in global real-time payments demands software that combines extreme reliability with operational velocity. "
            "I welcome the opportunity to bring my payment engineering background to your Singapore engineering team.",
            body_style
        ))

    elif role_type == "hirefeed":
        company = "Hire Feed"
        target_role = "Fullstack Developer (React / Next.js / TypeScript)"
        story.append(Paragraph(f"Dear Hiring Team at {company},", body_style))
        story.append(Paragraph(
            f"I am writing to express my keen interest in the <b>{target_role}</b> position at {company}. As a full-stack engineer with "
            "extensive experience shipping high-concurrency web applications using Next.js App Router, React, TypeScript, and Node.js, "
            "I am excited by the prospect of joining your remote team to deliver intuitive, performant digital products.",
            body_style
        ))
        story.append(Paragraph(
            "My experience encompasses the entire web development lifecycle, from responsive UI components to resilient database backends:",
            body_style
        ))
        story.append(Paragraph(
            "• <b>High-Concurrency Web Systems:</b> Architected <b>FIF Adventure</b>, a real-time gamification platform serving 1,500+ concurrent "
            "users, built with Next.js App Router, TypeScript, Supabase Realtime, PL/pgSQL row-level locking, and property-based testing (Fast-Check).",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Enterprise PWA & CMS Platforms:</b> Built the <b>FIFGROUP Microsite</b> for ~10,000 nationwide employees, featuring real-time "
            "leaderboards, dynamic SheetJS Excel bulk parsing, and persistent JWT authentication.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Micro-frontends & Frontend Modernization:</b> Led the migration of internal enterprise web apps from Angular 13 to Angular 20, "
            "incorporating Native Federation micro-frontends and Standalone Components.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Backend & REST API Design:</b> Developed robust backend services using Node.js, Java Spring Boot, and PostgreSQL, ensuring clean "
            "API contracts and rapid automated deployments via GitHub Actions CI/CD.",
            bullet_style
        ))
        story.append(Spacer(1, 3))
        story.append(Paragraph(
            "I thrive in autonomous, remote-first engineering cultures that value clean code, strong testing, and fast customer-focused iterations. "
            "I look forward to discussing how my full-stack background can help drive Hire Feed's product roadmap.",
            body_style
        ))

    elif role_type == "kredivo":
        company = "Kredivo Group"
        target_role = "Android Engineer - SDE 2"
        story.append(Paragraph(f"Dear Hiring Team at {company},", body_style))
        story.append(Paragraph(
            f"I am writing to express my strong enthusiasm for the <b>{target_role}</b> position at {company}. "
            "With hands-on experience engineering mission-critical mobile features in Indonesia's fintech ecosystem at AstraPay—coupled "
            "with my background as a Bangkit Academy (Google, GoTo, Traveloka) Mobile Development alumnus—I am eager to contribute to "
            "Kredivo's mobile platform, scaling seamless and secure digital credit solutions for millions of users.",
            body_style
        ))
        story.append(Paragraph(
            "At AstraPay, I have taken end-to-end ownership of client-side engineering for high-stakes financial user flows:",
            body_style
        ))
        story.append(Paragraph(
            "• <b>Biometric Security & Fraud Mitigation:</b> Integrated VIDA Liveness SDK and ID Fraud Shield into AstraPay's Android KYC V5, "
            "hardening onboarding security against spoofing while maintaining high conversion rates.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Data-Driven Mobile Experimentation:</b> Designed and executed dynamic A/B testing via Firebase Remote Config to evaluate alternative "
            "verification journeys and reduce onboarding drop-off.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Automated UI Testing & Reliability:</b> Implemented extensive Espresso UI test suites using the Page Object Model (POM), "
            "substantially reducing regression cycles across mobile releases.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Clean Architecture & Reusability:</b> Engineered modular components following MVVM, Clean Architecture, and Android Jetpack "
            "guidelines (Coroutines, Flow, Dagger Hilt) for maintainability and client-side responsiveness.",
            bullet_style
        ))
        story.append(Spacer(1, 3))
        story.append(Paragraph(
            "Kredivo has set the standard for speed, transparency, and trust in consumer lending across Southeast Asia. "
            "My technical experience in regulated financial onboarding and my focus on building resilient, performant Android architectures "
            "position me to immediately support Kredivo's mobile engineering velocity.",
            body_style
        ))

    else:  # youtap / default
        company = "Youtap Technology Ltd"
        target_role = "Senior Backend Developer"
        story.append(Paragraph(f"Dear Hiring Team at {company},", body_style))
        story.append(Paragraph(
            f"I am writing to express my strong interest in the <b>{target_role}</b> position at {company}. "
            "Having spent my career designing and optimizing backend architectures for digital wallet and payment systems "
            "at AstraPay and Bank Syariah Indonesia (BSI), I am deeply inspired by Youtap's mission to empower merchants "
            "and financial partners with seamless, reliable transaction solutions.",
            body_style
        ))
        story.append(Paragraph(
            "In my current role as Product Engineer at AstraPay, I have taken direct ownership of backend microservices "
            "using Java 21, Spring Boot, and PostgreSQL, directly matching the core objectives of your digital wallet platform:",
            body_style
        ))
        story.append(Paragraph(
            "• <b>High-Impact Architecture & Delivery:</b> Spearheaded the design of our merchant bank account change platform, "
            "reducing operational turnaround time by <b>70%</b> and completely eliminating SLA breaches (<b>22.7% down to 0%</b>).",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Transactional Integrity & Resilience:</b> Engineered idempotent workflows, 90-day validator lock schedulers, "
            "and automated OCR provider failover (Google Vertex AI to Advance AI) to ensure fault-tolerant transaction processing.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Database Optimization & Caching:</b> Profiled complex query plans in PostgreSQL and Oracle DB, halving query execution times "
            "(<b>10s to 5s</b>) and implementing Redis caching to boost throughput by <b>20%</b> on high-traffic endpoints.",
            bullet_style
        ))
        story.append(Paragraph(
            "• <b>Engineering Leadership & Code Quality:</b> As team leader during my BSI tenure and continuing at AstraPay, I have championed "
            "peer code reviews, mentored team members, and authored comprehensive API contracts to streamline frontend-backend collaboration.",
            bullet_style
        ))
        story.append(Spacer(1, 3))
        story.append(Paragraph(
            "Youtap's position as a leading digital merchant enabler requires backend services that are not only performant, "
            "but resilient under demanding transaction volumes. My hands-on background handling high-security financial workflows, "
            "coupled with continuous production monitoring via Datadog, will enable me to make an immediate impact on your platform's reliability.",
            body_style
        ))

    story.append(Paragraph(
        "I bring a strong culture of peer collaboration, constructive code reviews, and proactive communication. "
        "I look forward to discussing how my background can support your engineering roadmap.",
        body_style
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph("Kind regards,<br/><br/><b>Yoga Sulistiyo Widodo</b>", body_style))

    doc.build(story)
    print(f"[SUCCESS] Built PDF Cover Letter at: {output_path}")

if __name__ == "__main__":
    cl_dir = Path("cover_letters")
    cl_dir.mkdir(exist_ok=True)
    
    targets = ["youtap", "kredivo", "jpmorgan", "apple", "hirefeed", "capgemini", "quikhire", "bri", "deloitte", "hired"]
    for t in targets:
        out = cl_dir / f"Yoga_Sulistiyo_Widodo_Cover_Letter_{t.capitalize()}.pdf"
        create_cover_pdf(out, role_type=t)
