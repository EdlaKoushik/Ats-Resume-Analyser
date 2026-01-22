"""Role templates, groups and industry mapping extracted from suggestion_engine.py."""
from typing import Dict

ROLE_TEMPLATES: Dict[str, dict] = {
    # ========== SOFTWARE DEVELOPMENT ==========
    "frontend-developer": {
        "experience": (
            "Describe how you implemented responsive UI components using modern frameworks, "
            "managed application state, optimized performance (Core Web Vitals), "
            "and collaborated with UX/UI designers to translate designs into functional code. "
            "Include specific metrics on performance improvements, accessibility enhancements, "
            "and user engagement increases."
        ),
        "projects": (
            "Highlight frontend projects demonstrating component architecture, API integration, "
            "responsive design across devices, performance optimization techniques, "
            "and progressive web app features. Include details on technologies used, "
            "team collaboration, and measurable outcomes."
        ),
        "skills_priority": ["react", "javascript", "typescript", "css", "html"],
        "metrics": ["performance scores", "accessibility compliance", "user engagement", "bug reduction"]
    },
    "backend-developer": {
        "experience": (
            "Explain how you designed and built scalable APIs, implemented data models, "
            "optimized database queries, handled authentication/authorization, "
            "and ensured system reliability. Include specific examples of performance improvements, "
            "system scalability achievements, and security implementations."
        ),
        "projects": (
            "Showcase backend projects involving microservices architecture, database design, "
            "API development, caching strategies, and system integrations. "
            "Include details on throughput, response times, error rates, and scalability achievements."
        ),
        "skills_priority": ["python", "java", "nodejs", "sql", "rest"],
        "metrics": ["api uptime", "response times", "throughput", "error rates", "cost optimization"]
    },
    "fullstack-developer": {
        "experience": (
            "Describe end-to-end feature development from database design to frontend implementation. "
            "Explain how you bridged frontend and backend concerns, optimized data flow, "
            "and made architectural decisions considering both client and server perspectives."
        ),
        "projects": (
            "Showcase complete applications where you handled both client and server components. "
            "Include details on architecture decisions, technology choices, deployment strategies, "
            "and how you balanced frontend user experience with backend performance."
        ),
        "skills_priority": ["javascript", "nodejs", "react", "sql", "docker"],
        "metrics": ["feature completion time", "system performance", "user satisfaction", "code quality"]
    },
    "mobile-developer": {
        "experience": (
            "Describe native or cross-platform mobile app development, performance optimization for mobile, "
            "offline capabilities, push notifications implementation, app store submission processes, "
            "and user experience considerations specific to mobile platforms."
        ),
        "projects": (
            "Highlight mobile applications with details on platform-specific optimizations, "
            "app store metrics, user ratings, download statistics, and retention rates. "
            "Include information on testing across devices and OS versions."
        ),
        "skills_priority": ["react-native", "swift", "kotlin", "flutter", "mobile-testing"],
        "metrics": ["app store ratings", "user retention", "crash rates", "download numbers"]
    },
    "devops-engineer": {
        "experience": (
            "Explain CI/CD pipeline implementation, infrastructure as code practices, "
            "container orchestration, monitoring/alerting setup, security scanning integration, "
            "and disaster recovery planning. Include specific examples of automation that reduced manual work."
        ),
        "projects": (
            "Showcase infrastructure automation projects, deployment pipeline improvements, "
            "monitoring system implementations, or cost optimization initiatives. "
            "Include metrics on deployment frequency, lead time, mean time to recovery, and infrastructure costs."
        ),
        "skills_priority": ["docker", "kubernetes", "aws", "terraform", "jenkins"],
        "metrics": ["deployment frequency", "lead time", "change failure rate", "mean time to recovery"]
    },
    "site-reliability-engineer": {
        "experience": (
            "Describe how you improved system reliability through monitoring, alerting, "
            "incident response, capacity planning, and performance optimization. "
            "Include specific examples of reducing downtime, improving SLAs, or automating recovery processes."
        ),
        "projects": (
            "Highlight reliability engineering projects such as implementing SLOs/SLIs, "
            "building runbooks, creating chaos engineering experiments, or improving incident response processes. "
            "Include quantifiable improvements in system availability and performance."
        ),
        "skills_priority": ["kubernetes", "prometheus", "terraform", "python", "incident-response"],
        "metrics": ["system availability", "incident response time", "error budget", "SLO compliance"]
    },
    "qa-engineer": {
        "experience": (
            "Describe test strategy development, test case creation, manual and automated testing processes, "
            "bug reporting and tracking, regression testing, and quality metrics reporting. "
            "Include examples of catching critical bugs before production."
        ),
        "projects": (
            "Showcase test automation frameworks built, test coverage improvements, "
            "or quality initiatives that reduced defect escape rates. Include details on test pyramid implementation "
            "and collaboration with development teams on quality practices."
        ),
        "skills_priority": ["test-automation", "selenium", "cypress", "jira", "jenkins"],
        "metrics": ["test coverage", "defect escape rate", "test execution time", "bug resolution time"]
    },
    "test-automation-engineer": {
        "experience": (
            "Explain test automation framework development, CI/CD integration, "
            "performance/load testing automation, API testing, and test data management. "
            "Include specific examples of automation that improved testing efficiency."
        ),
        "projects": (
            "Highlight automation frameworks built from scratch or significantly improved. "
            "Include details on technologies used, team adoption, maintenance overhead reduction, "
            "and how automation accelerated release cycles."
        ),
        "skills_priority": ["selenium", "cypress", "python", "jenkins", "rest"],
        "metrics": ["automation coverage", "test execution speed", "false positive rate", "maintenance effort"]
    },

    # ========== DATA & AI/ML ==========
    "data-scientist": {
        "experience": (
            "Describe how you applied statistical analysis and machine learning to solve business problems. "
            "Include details on data exploration, feature engineering, model development, validation techniques, "
            "and business impact measurement. Explain how you translated complex findings into actionable insights."
        ),
        "projects": (
            "Highlight data science projects with clear business objectives, data challenges, "
            "model selection rationale, validation results, and business impact. "
            "Include details on data preprocessing, algorithm choices, and stakeholder communication."
        ),
        "skills_priority": ["python", "pandas", "scikit-learn", "sql", "statistics"],
        "metrics": ["model accuracy", "business impact", "data quality", "insight adoption"]
    },
    # ... (rest of ROLE_TEMPLATES copied verbatim from suggestion_engine.py) ...
}

ROLE_GROUPS: Dict[str, list] = {
    "software_engineering": [
        "frontend-developer", "backend-developer", "fullstack-developer", 
        "mobile-developer", "devops-engineer", "site-reliability-engineer",
        "qa-engineer", "test-automation-engineer"
    ],
    "data_ai_ml": [
        "data-scientist", "machine-learning-engineer", "data-engineer",
        "data-analyst", "business-intelligence-developer", "ai-researcher",
        "data-research-scientist"
    ],
    "cybersecurity": [
        "security-engineer", "penetration-tester", "security-analyst"
    ],
    "cloud_infrastructure": [
        "cloud-engineer", "systems-engineer", "network-engineer"
    ],
    "product_management": [
        "product-manager", "technical-product-manager", "project-manager",
        "scrum-master"
    ],
    "design_ux": [
        "ux-designer", "ui-designer", "product-designer"
    ],
    "business_analytics": [
        "business-analyst", "product-analyst", "strategy-analyst"
    ],
    "enterprise_systems": [
        "sap-consultant", "salesforce-developer", "erp-analyst"
    ],
    "finance_accounting": [
        "financial-analyst", "accountant"
    ],
    "healthcare_it": [
        "healthcare-it-analyst", "clinical-informaticist"
    ],
    "manufacturing_industrial": [
        "manufacturing-engineer", "quality-engineer"
    ],
    "education_training": [
        "instructional-designer", "edtech-developer"
    ],
    "creative_media": [
        "video-editor", "graphic-designer"
    ],
    "sales_marketing": [
        "digital-marketer", "seo-specialist", "sales-engineer"
    ],
    "executive_leadership": [
        "engineering-manager", "cto", "vp-engineering"
    ],
    "research_academia": [
        "research-scientist", "data-research-scientist"
    ],
    "legal_compliance": [
        "compliance-officer", "legal-operations"
    ],
    "consulting": [
        "management-consultant", "technology-consultant"
    ],
    "support_operations": [
        "technical-support-engineer", "it-support-specialist"
    ],
    "startup_entrepreneurship": [
        "startup-founder", "growth-hacker"
    ],
    "emerging_technologies": [
        "blockchain-developer", "ai-researcher", "ar-vr-developer"
    ],
    "government_public_sector": [
        "public-sector-it", "policy-analyst"
    ]
}

# Role to industry mapping
ROLE_INDUSTRY_MAPPING: Dict[str, list] = {
    "healthcare_it": ["healthcare", "pharmaceutical", "life-sciences"],
    "manufacturing_industrial": ["manufacturing", "automotive", "aerospace", "energy"],
    "enterprise_systems": ["enterprise", "finance", "retail", "manufacturing"],
    "government_public_sector": ["government", "public-sector", "education", "healthcare"],
    "financial_services": ["finance", "banking", "insurance", "fintech"],
    "retail_ecommerce": ["retail", "ecommerce", "consumer-goods"],
    "education_training": ["education", "edtech", "corporate-training"],
    "media_entertainment": ["media", "entertainment", "gaming", "publishing"],
    "telecom": ["telecommunications", "networking", "wireless"],
    "travel_hospitality": ["travel", "hospitality", "tourism", "airlines"],
    "real_estate": ["real-estate", "construction", "property-management"],
    "legal_compliance": ["legal", "compliance", "regulatory"],
    "energy_utilities": ["energy", "utilities", "renewable-energy"],
    "agriculture": ["agriculture", "food", "agritech"],
    "transportation_logistics": ["transportation", "logistics", "supply-chain"]
}
