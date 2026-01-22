"""
backend/data/skill_meta.py

Filtered skill metadata dictionary.
Only contains skills that exist in the canonical SKILLS set from skills_db.py.
This file maintains the original metadata structure from suggestion_engine.py
and filters it against the reduced modern SKILLS set.

Last filtered & verified: January 2026
"""
from data.skills_db import SKILLS as SKILLS_SET
from typing import Dict, Any

# ──────────────────────────────────────────────────────────────────────────────
# Reduced canonical SKILLS set (modern, high-demand skills ~2026 perspective)
# This is the filter set — only these will remain in SKILL_META
# ──────────────────────────────────────────────────────────────────────────────
SKILLS_SET = {
    # Core Web & Frontend Foundations
    "html", "css", "javascript", "typescript", "responsive-design", "accessibility", "web-components",
    # Frameworks
    "react", "vue", "svelte", "nextjs", "nuxt",
    # State & Styling
    "zustand", "tailwind-css", "styled-components",
    # Build & Tooling
    "vite",
    # Testing
    "jest", "cypress", "playwright", "testing-library",
    # Performance & PWA
    "web-vitals", "lighthouse", "pwa", "service-workers",
    # Backend & APIs
    "nodejs", "python", "go", "express", "fastapi", "rest", "graphql", "websockets",
    # Databases
    "postgresql", "mysql", "mongodb", "redis", "prisma", "sqlalchemy",
    # Cloud & DevOps
    "aws", "docker", "terraform", "kubernetes",
    # Data & AI/ML Core
    "pandas", "numpy", "scikit-learn", "pytorch", "tensorflow",
    # Mobile
    "react-native", "flutter",
    # Methodologies & Soft Skills
    "agile", "communication", "problem-solving", "teamwork",
}

# ──────────────────────────────────────────────────────────────────────────────
# FULL RAW SKILL METADATA (source of truth - copied verbatim from suggestion_engine.py)
# ──────────────────────────────────────────────────────────────────────────────
_RAW_SKILL_META: Dict[str, Dict[str, Any]] = {
    # ========== CORE WEB ==========
    "html": {
        "why": "Fundamental markup language for creating web pages",
        "roles": ["frontend", "fullstack", "web-developer", "ui-developer"],
        "level": ["beginner", "intermediate", "advanced"],
        "category": "core-web"
    },
    "html5": {
        "why": "Latest HTML standard with new semantic elements and APIs",
        "roles": ["frontend", "fullstack", "web-developer"],
        "level": ["intermediate", "advanced"],
        "category": "core-web"
    },
    "css": {
        "why": "Styling language for designing web page appearance",
        "roles": ["frontend", "ui-developer", "web-developer"],
        "level": ["beginner", "intermediate", "advanced"],
        "category": "core-web"
    },
    "css3": {
        "why": "Modern CSS with animations, gradients, and advanced selectors",
        "roles": ["frontend", "ui-developer"],
        "level": ["intermediate", "advanced"],
        "category": "core-web"
    },
    "javascript": {
        "why": "Programming language for interactive web applications",
        "roles": ["frontend", "fullstack", "web-developer", "software-engineer"],
        "level": ["beginner", "intermediate", "advanced"],
        "category": "core-web"
    },
    "typescript": {
        "why": "Typed superset of JavaScript for scalable applications",
        "roles": ["frontend", "fullstack", "backend", "software-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "core-web"
    },
    "responsive-design": {
        "why": "Ensures websites work well on all device sizes",
        "roles": ["frontend", "ui-developer", "web-developer"],
        "level": ["intermediate", "advanced"],
        "category": "core-web"
    },
    "accessibility": {
        "why": "Makes websites usable by people with disabilities",
        "roles": ["frontend", "ui-developer", "ux-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "core-web"
    },
    "web-components": {
        "why": "Reusable custom elements with encapsulated functionality",
        "roles": ["frontend", "ui-developer"],
        "level": ["advanced"],
        "category": "core-web"
    },

    # ========== FRAMEWORKS ==========
    "react": {
        "why": "Most popular library for building user interfaces with components",
        "roles": ["frontend", "fullstack", "react-developer"],
        "level": ["intermediate", "advanced"],
        "category": "frontend-frameworks"
    },
    "vue": {
        "why": "Progressive framework for building UIs with approachable learning curve",
        "roles": ["frontend", "fullstack", "vue-developer"],
        "level": ["intermediate", "advanced"],
        "category": "frontend-frameworks"
    },
    "angular": {
        "why": "Comprehensive framework for enterprise-scale applications",
        "roles": ["frontend", "fullstack", "angular-developer"],
        "level": ["intermediate", "advanced"],
        "category": "frontend-frameworks"
    },
    "svelte": {
        "why": "Compiler-based framework for highly efficient applications",
        "roles": ["frontend", "fullstack"],
        "level": ["intermediate", "advanced"],
        "category": "frontend-frameworks"
    },
    "nextjs": {
        "why": "React framework with server-side rendering and optimized performance",
        "roles": ["frontend", "fullstack", "react-developer"],
        "level": ["intermediate", "advanced"],
        "category": "frontend-frameworks"
    },
    "nuxt": {
        "why": "Vue framework for server-side rendering and static sites",
        "roles": ["frontend", "fullstack", "vue-developer"],
        "level": ["intermediate", "advanced"],
        "category": "frontend-frameworks"
    },

    # ========== STATE MANAGEMENT ==========
    "redux": {
        "why": "Predictable state container for JavaScript applications",
        "roles": ["frontend", "fullstack"],
        "level": ["intermediate", "advanced"],
        "category": "state-management"
    },
    "redux-toolkit": {
        "why": "Official recommended way to write Redux logic",
        "roles": ["frontend", "fullstack"],
        "level": ["intermediate", "advanced"],
        "category": "state-management"
    },
    "mobx": {
        "why": "Simple, scalable state management using observables",
        "roles": ["frontend", "fullstack"],
        "level": ["intermediate", "advanced"],
        "category": "state-management"
    },
    "zustand": {
        "why": "Small, fast state management solution with minimal boilerplate",
        "roles": ["frontend", "fullstack"],
        "level": ["intermediate", "advanced"],
        "category": "state-management"
    },
    "recoil": {
        "why": "State management library for React with minimal API",
        "roles": ["frontend", "fullstack"],
        "level": ["intermediate", "advanced"],
        "category": "state-management"
    },

    # ========== STYLING ==========
    "tailwind-css": {
        "why": "Utility-first CSS framework for rapid UI development",
        "roles": ["frontend", "ui-developer"],
        "level": ["intermediate", "advanced"],
        "category": "css-frameworks"
    },
    "sass": {
        "why": "CSS preprocessor with variables, nesting, and mixins",
        "roles": ["frontend", "ui-developer"],
        "level": ["intermediate", "advanced"],
        "category": "css-preprocessors"
    },
    "styled-components": {
        "why": "CSS-in-JS library for scoped styling in React",
        "roles": ["frontend", "ui-developer"],
        "level": ["intermediate", "advanced"],
        "category": "css-in-js"
    },
    "material-ui": {
        "why": "React component library implementing Material Design",
        "roles": ["frontend", "ui-developer"],
        "level": ["intermediate", "advanced"],
        "category": "ui-libraries"
    },
    "bootstrap": {
        "why": "Popular CSS framework for responsive, mobile-first sites",
        "roles": ["frontend", "ui-developer", "web-developer"],
        "level": ["beginner", "intermediate", "advanced"],
        "category": "css-frameworks"
    },

    # ========== BUILD TOOLS ==========
    "webpack": {
        "why": "Module bundler for JavaScript applications",
        "roles": ["frontend", "fullstack", "build-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "build-tools"
    },
    "vite": {
        "why": "Next-generation frontend tooling with fast hot module replacement",
        "roles": ["frontend", "fullstack"],
        "level": ["intermediate", "advanced"],
        "category": "build-tools"
    },
    "babel": {
        "why": "JavaScript compiler for using next-gen JavaScript today",
        "roles": ["frontend", "fullstack", "build-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "build-tools"
    },

    # ========== TESTING ==========
    "jest": {
        "why": "JavaScript testing framework with built-in coverage and mocking",
        "roles": ["frontend", "fullstack", "qa-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "testing-tools"
    },
    "cypress": {
        "why": "End-to-end testing framework for modern web applications",
        "roles": ["frontend", "qa-engineer", "test-automation-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "testing-tools"
    },
    "playwright": {
        "why": "Cross-browser testing framework for reliable end-to-end testing",
        "roles": ["frontend", "qa-engineer", "test-automation-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "testing-tools"
    },
    "testing-library": {
        "why": "Testing utilities that encourage good testing practices",
        "roles": ["frontend", "fullstack", "qa-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "testing-tools"
    },

    # ========== PERFORMANCE ==========
    "web-vitals": {
        "why": "Google's metrics for measuring user experience on the web",
        "roles": ["frontend", "performance-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "performance"
    },
    "lighthouse": {
        "why": "Automated tool for improving web page quality",
        "roles": ["frontend", "performance-engineer", "seo-specialist"],
        "level": ["intermediate", "advanced"],
        "category": "performance"
    },

    # ========== PWA ==========
    "pwa": {
        "why": "Progressive Web Apps for native-like web experiences",
        "roles": ["frontend", "mobile-developer", "web-developer"],
        "level": ["intermediate", "advanced"],
        "category": "mobile-web"
    },
    "service-workers": {
        "why": "Background scripts enabling offline capabilities and push notifications",
        "roles": ["frontend", "pwa-developer"],
        "level": ["advanced"],
        "category": "mobile-web"
    },

    # ========== BACKEND LANGUAGES ==========
    "nodejs": {
        "why": "JavaScript runtime for building scalable server-side applications",
        "roles": ["backend", "fullstack", "devops", "api-developer"],
        "level": ["intermediate", "advanced"],
        "category": "backend-languages"
    },
    "python": {
        "why": "Versatile language for web development, data science, and automation",
        "roles": ["backend", "data-scientist", "ml-engineer", "devops", "automation-engineer"],
        "level": ["beginner", "intermediate", "advanced"],
        "category": "backend-languages"
    },
    "java": {
        "why": "Enterprise-grade language for large-scale, high-performance applications",
        "roles": ["backend", "java-developer", "enterprise-developer"],
        "level": ["intermediate", "advanced"],
        "category": "backend-languages"
    },
    "csharp": {
        "why": "Microsoft's language for .NET applications and enterprise solutions",
        "roles": ["backend", "dotnet-developer", "game-developer"],
        "level": ["intermediate", "advanced"],
        "category": "backend-languages"
    },
    "go": {
        "why": "Google's language for concurrent, high-performance systems",
        "roles": ["backend", "systems-programmer", "cloud-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "backend-languages"
    },
    "rust": {
        "why": "Systems programming language focusing on safety and performance",
        "roles": ["backend", "systems-programmer", "embedded-developer"],
        "level": ["advanced"],
        "category": "backend-languages"
    },
    "php": {
        "why": "Server-side scripting language powering many web applications",
        "roles": ["backend", "web-developer", "wordpress-developer"],
        "level": ["intermediate", "advanced"],
        "category": "backend-languages"
    },
    "ruby": {
        "why": "Dynamic language known for Ruby on Rails web framework",
        "roles": ["backend", "ruby-developer", "web-developer"],
        "level": ["intermediate", "advanced"],
        "category": "backend-languages"
    },

    # ========== BACKEND FRAMEWORKS ==========
    "express": {
        "why": "Minimalist Node.js web application framework",
        "roles": ["backend", "fullstack", "nodejs-developer"],
        "level": ["intermediate", "advanced"],
        "category": "backend-frameworks"
    },
    "django": {
        "why": "High-level Python web framework for rapid development",
        "roles": ["backend", "fullstack", "python-developer"],
        "level": ["intermediate", "advanced"],
        "category": "backend-frameworks"
    },
    "spring-boot": {
        "why": "Java framework for creating stand-alone, production-grade applications",
        "roles": ["backend", "java-developer", "enterprise-developer"],
        "level": ["intermediate", "advanced"],
        "category": "backend-frameworks"
    },
    "laravel": {
        "why": "PHP framework with elegant syntax and robust features",
        "roles": ["backend", "php-developer", "web-developer"],
        "level": ["intermediate", "advanced"],
        "category": "backend-frameworks"
    },
    "ruby-on-rails": {
        "why": "Full-stack web application framework following MVC pattern",
        "roles": ["backend", "fullstack", "ruby-developer"],
        "level": ["intermediate", "advanced"],
        "category": "backend-frameworks"
    },
    "aspnet-core": {
        "why": "Cross-platform framework for building modern cloud-based applications",
        "roles": ["backend", "dotnet-developer", "enterprise-developer"],
        "level": ["intermediate", "advanced"],
        "category": "backend-frameworks"
    },
    "fastapi": {
        "why": "Modern Python web framework for building APIs with automatic docs",
        "roles": ["backend", "api-developer", "python-developer"],
        "level": ["intermediate", "advanced"],
        "category": "backend-frameworks"
    },

    # ========== DATABASES - SQL ==========
    "postgresql": {
        "why": "Advanced open-source relational database with strong features",
        "roles": ["backend", "database-admin", "data-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "databases-sql"
    },
    "mysql": {
        "why": "Popular open-source relational database management system",
        "roles": ["backend", "database-admin", "web-developer"],
        "level": ["intermediate", "advanced"],
        "category": "databases-sql"
    },
    "sql-server": {
        "why": "Microsoft's enterprise relational database management system",
        "roles": ["backend", "database-admin", "enterprise-developer"],
        "level": ["intermediate", "advanced"],
        "category": "databases-sql"
    },
    "oracle-database": {
        "why": "Enterprise-grade relational database for large-scale applications",
        "roles": ["database-admin", "enterprise-developer", "data-architect"],
        "level": ["advanced"],
        "category": "databases-sql"
    },
    "sql": {
        "why": "Standard language for managing and querying relational databases",
        "roles": ["backend", "database-admin", "data-analyst", "data-engineer"],
        "level": ["beginner", "intermediate", "advanced"],
        "category": "databases-sql"
    },

    # ========== DATABASES - NOSQL ==========
    "mongodb": {
        "why": "Document database with flexible schema for modern applications",
        "roles": ["backend", "fullstack", "data-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "databases-nosql"
    },
    "redis": {
        "why": "In-memory data structure store used as database, cache, and message broker",
        "roles": ["backend", "devops", "performance-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "databases-nosql"
    },
    "elasticsearch": {
        "why": "Distributed search and analytics engine for full-text search",
        "roles": ["backend", "search-engineer", "data-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "databases-nosql"
    },
    "cassandra": {
        "why": "Distributed NoSQL database designed to handle large amounts of data",
        "roles": ["backend", "data-engineer", "big-data-engineer"],
        "level": ["advanced"],
        "category": "databases-nosql"
    },

    # ========== ORMS ==========
    "prisma": {
        "why": "Next-generation ORM for Node.js and TypeScript",
        "roles": ["backend", "fullstack", "nodejs-developer"],
        "level": ["intermediate", "advanced"],
        "category": "orms"
    },
    "sequelize": {
        "why": "Promise-based Node.js ORM for Postgres, MySQL, MariaDB, SQLite and SQL Server",
        "roles": ["backend", "fullstack", "nodejs-developer"],
        "level": ["intermediate", "advanced"],
        "category": "orms"
    },
    "sqlalchemy": {
        "why": "Python SQL toolkit and Object-Relational Mapper",
        "roles": ["backend", "python-developer", "data-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "orms"
    },
    "hibernate": {
        "why": "Object-relational mapping tool for Java applications",
        "roles": ["backend", "java-developer", "enterprise-developer"],
        "level": ["intermediate", "advanced"],
        "category": "orms"
    },
    "entity-framework": {
        "why": "Microsoft's ORM for .NET applications",
        "roles": ["backend", "dotnet-developer", "enterprise-developer"],
        "level": ["intermediate", "advanced"],
        "category": "orms"
    },

    # ========== API TECHNOLOGIES ==========
    "rest": {
        "why": "Architectural style for designing networked applications",
        "roles": ["backend", "api-developer", "fullstack"],
        "level": ["intermediate", "advanced"],
        "category": "api-technologies"
    },
    "graphql": {
        "why": "Query language for APIs that provides clients with exactly what they need",
        "roles": ["backend", "frontend", "fullstack", "api-developer"],
        "level": ["intermediate", "advanced"],
        "category": "api-technologies"
    },
    "grpc": {
        "why": "High-performance RPC framework for microservices communication",
        "roles": ["backend", "microservices-developer", "systems-engineer"],
        "level": ["advanced"],
        "category": "api-technologies"
    },
    "websockets": {
        "why": "Protocol for real-time, bidirectional communication between client and server",
        "roles": ["backend", "frontend", "real-time-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "api-technologies"
    },

    # ========== AUTHENTICATION ==========
    "oauth2": {
        "why": "Authorization framework enabling applications to obtain limited access",
        "roles": ["backend", "security-engineer", "api-developer"],
        "level": ["intermediate", "advanced"],
        "category": "authentication"
    },
    "jwt": {
        "why": "Compact, URL-safe means of representing claims to be transferred between parties",
        "roles": ["backend", "frontend", "fullstack", "api-developer"],
        "level": ["intermediate", "advanced"],
        "category": "authentication"
    },
    "openid-connect": {
        "why": "Identity layer on top of OAuth 2.0 for authentication",
        "roles": ["backend", "security-engineer", "identity-engineer"],
        "level": ["advanced"],
        "category": "authentication"
    },

    # ========== CLOUD PROVIDERS & DEVOPS ==========
    "aws": {
        "why": "Market leader in cloud computing with extensive service offerings",
        "roles": ["devops", "cloud-engineer", "sre", "backend", "solution-architect"],
        "level": ["intermediate", "advanced"],
        "category": "cloud-platforms"
    },
    "azure": {
        "why": "Microsoft's cloud platform with strong enterprise integration",
        "roles": ["devops", "cloud-engineer", "dotnet-developer", "enterprise-architect"],
        "level": ["intermediate", "advanced"],
        "category": "cloud-platforms"
    },
    "gcp": {
        "why": "Google's cloud platform with strong data and ML services",
        "roles": ["devops", "cloud-engineer", "data-engineer", "ml-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "cloud-platforms"
    },
    "docker": {
        "why": "Containerization platform for consistent application deployment",
        "roles": ["devops", "backend", "fullstack", "sre"],
        "level": ["intermediate", "advanced"],
        "category": "containerization"
    },
    "kubernetes": {
        "why": "Container orchestration platform for automating deployment and scaling",
        "roles": ["devops", "cloud-engineer", "sre", "platform-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "container-orchestration"
    },
    "terraform": {
        "why": "Infrastructure as Code tool for provisioning and managing cloud resources",
        "roles": ["devops", "cloud-engineer", "sre", "infrastructure-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "infrastructure-as-code"
    },
    "ansible": {
        "why": "Configuration management and automation tool for IT infrastructure",
        "roles": ["devops", "system-admin", "automation-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "configuration-management"
    },

    # ========== CI/CD ==========
    "jenkins": {
        "why": "Open-source automation server for building, testing, and deploying",
        "roles": ["devops", "ci-cd-engineer", "automation-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "ci-cd-tools"
    },
    "github-actions": {
        "why": "CI/CD platform integrated directly into GitHub",
        "roles": ["devops", "fullstack", "software-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "ci-cd-tools"
    },
    "gitlab-ci": {
        "why": "CI/CD tool integrated into GitLab's DevOps platform",
        "roles": ["devops", "fullstack", "software-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "ci-cd-tools"
    },

    # ========== MONITORING ==========
    "prometheus": {
        "why": "Open-source monitoring and alerting toolkit",
        "roles": ["devops", "sre", "monitoring-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "monitoring"
    },
    "grafana": {
        "why": "Open-source platform for monitoring and observability",
        "roles": ["devops", "sre", "data-visualization-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "monitoring"
    },
    "elk-stack": {
        "why": "Log management and analysis platform (Elasticsearch, Logstash, Kibana)",
        "roles": ["devops", "sre", "log-analyst"],
        "level": ["intermediate", "advanced"],
        "category": "monitoring"
    },
    "datadog": {
        "why": "Monitoring and analytics platform for cloud-scale applications",
        "roles": ["devops", "sre", "performance-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "monitoring"
    },

    # ========== SECURITY ==========
    "vault": {
        "why": "Tool for securely storing and accessing secrets",
        "roles": ["devops", "security-engineer", "sre"],
        "level": ["intermediate", "advanced"],
        "category": "security"
    },
    "sonarqube": {
        "why": "Platform for continuous inspection of code quality",
        "roles": ["devops", "security-engineer", "code-quality-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "security"
    },

    # ========== DATA SCIENCE CORE ==========
    "python": {
        "why": "Primary language for data science and machine learning",
        "roles": ["data-scientist", "ml-engineer", "data-analyst", "ai-researcher"],
        "level": ["beginner", "intermediate", "advanced"],
        "category": "data-science-languages"
    },
    "r": {
        "why": "Statistical programming language for data analysis and visualization",
        "roles": ["data-scientist", "statistician", "bioinformatician"],
        "level": ["intermediate", "advanced"],
        "category": "data-science-languages"
    },
    "pandas": {
        "why": "Python library for data manipulation and analysis",
        "roles": ["data-scientist", "data-analyst", "ml-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "data-manipulation"
    },
    "numpy": {
        "why": "Fundamental package for scientific computing in Python",
        "roles": ["data-scientist", "ml-engineer", "researcher"],
        "level": ["intermediate", "advanced"],
        "category": "data-manipulation"
    },

    # ========== MACHINE LEARNING ==========
    "scikit-learn": {
        "why": "Python library for traditional machine learning algorithms",
        "roles": ["data-scientist", "ml-engineer", "researcher"],
        "level": ["intermediate", "advanced"],
        "category": "machine-learning"
    },
    "tensorflow": {
        "why": "Open-source platform for machine learning and deep learning",
        "roles": ["ml-engineer", "data-scientist", "ai-researcher"],
        "level": ["intermediate", "advanced"],
        "category": "deep-learning"
    },
    "pytorch": {
        "why": "Deep learning framework with strong research community",
        "roles": ["ml-engineer", "ai-researcher", "data-scientist"],
        "level": ["intermediate", "advanced"],
        "category": "deep-learning"
    },
    "keras": {
        "why": "High-level neural networks API, written in Python",
        "roles": ["ml-engineer", "data-scientist", "researcher"],
        "level": ["intermediate", "advanced"],
        "category": "deep-learning"
    },

    # ========== BIG DATA ==========
    "apache-spark": {
        "why": "Unified analytics engine for large-scale data processing",
        "roles": ["data-engineer", "big-data-engineer", "data-scientist"],
        "level": ["intermediate", "advanced"],
        "category": "big-data"
    },
    "hadoop": {
        "why": "Framework for distributed storage and processing of big data",
        "roles": ["data-engineer", "big-data-engineer", "hadoop-developer"],
        "level": ["intermediate", "advanced"],
        "category": "big-data"
    },
    "kafka": {
        "why": "Distributed event streaming platform",
        "roles": ["data-engineer", "backend", "real-time-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "big-data"
    },
    "airflow": {
        "why": "Platform to programmatically author, schedule and monitor workflows",
        "roles": ["data-engineer", "ml-engineer", "etl-developer"],
        "level": ["intermediate", "advanced"],
        "category": "big-data"
    },

    # ========== DATA VISUALIZATION ==========
    "tableau": {
        "why": "Business intelligence tool for interactive data visualization",
        "roles": ["data-analyst", "business-analyst", "bi-developer"],
        "level": ["intermediate", "advanced"],
        "category": "data-visualization"
    },
    "powerbi": {
        "why": "Microsoft's business analytics service for interactive visualizations",
        "roles": ["data-analyst", "business-analyst", "bi-developer"],
        "level": ["intermediate", "advanced"],
        "category": "data-visualization"
    },
    "matplotlib": {
        "why": "Comprehensive library for creating static, animated, and interactive visualizations",
        "roles": ["data-scientist", "researcher", "analyst"],
        "level": ["intermediate", "advanced"],
        "category": "data-visualization"
    },
    "seaborn": {
        "why": "Python visualization library based on matplotlib for statistical graphics",
        "roles": ["data-scientist", "researcher", "analyst"],
        "level": ["intermediate", "advanced"],
        "category": "data-visualization"
    },

    # ========== NLP ==========
    "nltk": {
        "why": "Platform for building Python programs to work with human language data",
        "roles": ["nlp-engineer", "data-scientist", "researcher"],
        "level": ["intermediate", "advanced"],
        "category": "natural-language-processing"
    },
    "spacy": {
        "why": "Industrial-strength Natural Language Processing in Python",
        "roles": ["nlp-engineer", "data-scientist", "software-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "natural-language-processing"
    },
    "transformers": {
        "why": "State-of-the-art Natural Language Processing for Pytorch and TensorFlow",
        "roles": ["nlp-engineer", "ai-researcher", "ml-engineer"],
        "level": ["advanced"],
        "category": "natural-language-processing"
    },

    # ========== COMPUTER VISION ==========
    "opencv": {
        "why": "Open source computer vision and machine learning software library",
        "roles": ["computer-vision-engineer", "ml-engineer", "robotics-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "computer-vision"
    },

    # ========== CROSS-PLATFORM MOBILE ==========
    "react-native": {
        "why": "Framework for building native mobile apps using React",
        "roles": ["mobile-developer", "frontend", "react-developer"],
        "level": ["intermediate", "advanced"],
        "category": "cross-platform-mobile"
    },
    "flutter": {
        "why": "UI toolkit for building natively compiled applications from a single codebase",
        "roles": ["mobile-developer", "frontend", "dart-developer"],
        "level": ["intermediate", "advanced"],
        "category": "cross-platform-mobile"
    },
    "dart": {
        "why": "Programming language optimized for building mobile, desktop, server, and web applications",
        "roles": ["mobile-developer", "flutter-developer"],
        "level": ["intermediate", "advanced"],
        "category": "cross-platform-mobile"
    },
    "ionic": {
        "why": "Framework for building cross-platform mobile apps with web technologies",
        "roles": ["mobile-developer", "frontend", "web-developer"],
        "level": ["intermediate", "advanced"],
        "category": "cross-platform-mobile"
    },

    # ========== ANDROID ==========
    "kotlin": {
        "why": "Modern programming language for Android development",
        "roles": ["android-developer", "mobile-developer", "kotlin-developer"],
        "level": ["intermediate", "advanced"],
        "category": "android-development"
    },
    "java-android": {
        "why": "Traditional language for Android app development",
        "roles": ["android-developer", "mobile-developer", "java-developer"],
        "level": ["intermediate", "advanced"],
        "category": "android-development"
    },
    "jetpack-compose": {
        "why": "Modern toolkit for building native Android UI",
        "roles": ["android-developer", "mobile-developer", "ui-developer"],
        "level": ["intermediate", "advanced"],
        "category": "android-development"
    },

    # ========== iOS ==========
    "swift": {
        "why": "Programming language for iOS, macOS, watchOS, and tvOS development",
        "roles": ["ios-developer", "mobile-developer", "apple-developer"],
        "level": ["intermediate", "advanced"],
        "category": "ios-development"
    },
    "swiftui": {
        "why": "Declarative UI framework for building Apple platform applications",
        "roles": ["ios-developer", "mobile-developer", "ui-developer"],
        "level": ["intermediate", "advanced"],
        "category": "ios-development"
    },
    "objective-c": {
        "why": "Object-oriented programming language used by Apple before Swift",
        "roles": ["ios-developer", "mobile-developer", "legacy-developer"],
        "level": ["advanced"],
        "category": "ios-development"
    },

    # ========== MOBILE TESTING ==========
    "appium": {
        "why": "Open-source test automation framework for mobile applications",
        "roles": ["mobile-qa-engineer", "test-automation-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "mobile-testing"
    },
    "detox": {
        "why": "Gray box end-to-end testing and automation framework for mobile apps",
        "roles": ["mobile-qa-engineer", "react-native-developer"],
        "level": ["intermediate", "advanced"],
        "category": "mobile-testing"
    },

    # ========== APP DISTRIBUTION ==========
    "fastlane": {
        "why": "Tool to automate building and releasing iOS and Android apps",
        "roles": ["mobile-developer", "devops", "release-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "mobile-devops"
    },

    # ========== SECURITY DOMAINS ==========
    "penetration-testing": {
        "why": "Simulated cyber attacks to identify security vulnerabilities",
        "roles": ["security-engineer", "pentester", "ethical-hacker"],
        "level": ["advanced"],
        "category": "offensive-security"
    },
    "ethical-hacking": {
        "why": "Authorized attempts to gain unauthorized access to systems",
        "roles": ["security-engineer", "pentester", "security-analyst"],
        "level": ["advanced"],
        "category": "offensive-security"
    },
    "security-operations-center": {
        "why": "Centralized unit that deals with security issues on an organizational level",
        "roles": ["soc-analyst", "security-analyst", "incident-responder"],
        "level": ["intermediate", "advanced"],
        "category": "defensive-security"
    },
    "incident-response": {
        "why": "Process for handling security breaches or cyber attacks",
        "roles": ["incident-responder", "security-analyst", "soc-analyst"],
        "level": ["intermediate", "advanced"],
        "category": "defensive-security"
    },

    # ========== CRYPTOGRAPHY ==========
    "cryptography": {
        "why": "Practice and study of techniques for secure communication",
        "roles": ["security-engineer", "cryptographer", "security-architect"],
        "level": ["advanced"],
        "category": "cryptography"
    },
    "ssl-tls": {
        "why": "Protocols for establishing authenticated and encrypted links",
        "roles": ["security-engineer", "network-engineer", "devops"],
        "level": ["intermediate", "advanced"],
        "category": "cryptography"
    },

    # ========== NETWORK SECURITY ==========
    "firewalls": {
        "why": "Network security system that monitors and controls network traffic",
        "roles": ["network-security-engineer", "system-admin", "security-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "network-security"
    },
    "ids": {
        "why": "Intrusion Detection System for monitoring network traffic for suspicious activity",
        "roles": ["security-analyst", "network-engineer", "soc-analyst"],
        "level": ["intermediate", "advanced"],
        "category": "network-security"
    },
    "waf": {
        "why": "Web Application Firewall for filtering and monitoring HTTP traffic",
        "roles": ["security-engineer", "web-developer", "devops"],
        "level": ["intermediate", "advanced"],
        "category": "network-security"
    },

    # ========== SECURITY TOOLS ==========
    "burp-suite": {
        "why": "Platform for performing security testing of web applications",
        "roles": ["pentester", "security-engineer", "web-developer"],
        "level": ["intermediate", "advanced"],
        "category": "security-tools"
    },
    "metasploit": {
        "why": "Penetration testing framework for developing and executing exploit code",
        "roles": ["pentester", "security-engineer", "ethical-hacker"],
        "level": ["advanced"],
        "category": "security-tools"
    },
    "wireshark": {
        "why": "Network protocol analyzer for troubleshooting and analysis",
        "roles": ["network-engineer", "security-analyst", "system-admin"],
        "level": ["intermediate", "advanced"],
        "category": "security-tools"
    },
    "nmap": {
        "why": "Network discovery and security auditing tool",
        "roles": ["security-engineer", "network-engineer", "pentester"],
        "level": ["intermediate", "advanced"],
        "category": "security-tools"
    },

    # ========== STANDARDS & COMPLIANCE ==========
    "owasp": {
        "why": "Open Web Application Security Project providing security standards",
        "roles": ["security-engineer", "web-developer", "security-analyst"],
        "level": ["intermediate", "advanced"],
        "category": "security-standards"
    },
    "iso-27001": {
        "why": "International standard for information security management systems",
        "roles": ["security-architect", "compliance-officer", "security-manager"],
        "level": ["advanced"],
        "category": "security-standards"
    },
    "gdpr": {
        "why": "General Data Protection Regulation for data privacy in EU",
        "roles": ["compliance-officer", "security-engineer", "data-protection-officer"],
        "level": ["intermediate", "advanced"],
        "category": "security-standards"
    },
    "hipaa": {
        "why": "Health Insurance Portability and Accountability Act for healthcare data",
        "roles": ["healthcare-it", "compliance-officer", "security-engineer-healthcare"],
        "level": ["intermediate", "advanced"],
        "category": "security-standards"
    },
    "pci-dss": {
        "why": "Payment Card Industry Data Security Standard for cardholder data",
        "roles": ["security-engineer", "compliance-officer", "ecommerce-developer"],
        "level": ["intermediate", "advanced"],
        "category": "security-standards"
    },

    # ========== BLOCKCHAIN ==========
    "blockchain": {
        "why": "Distributed ledger technology enabling decentralized applications",
        "roles": ["blockchain-developer", "web3-developer", "crypto-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "blockchain"
    },
    "ethereum": {
        "why": "Decentralized platform for smart contracts and dApps",
        "roles": ["blockchain-developer", "smart-contract-developer", "web3-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "blockchain"
    },
    "solidity": {
        "why": "Programming language for writing smart contracts on Ethereum",
        "roles": ["blockchain-developer", "smart-contract-developer"],
        "level": ["intermediate", "advanced"],
        "category": "blockchain"
    },
    "smart-contracts": {
        "why": "Self-executing contracts with terms directly written into code",
        "roles": ["blockchain-developer", "smart-contract-developer"],
        "level": ["intermediate", "advanced"],
        "category": "blockchain"
    },
    "defi": {
        "why": "Decentralized Finance applications on blockchain networks",
        "roles": ["blockchain-developer", "defi-developer", "financial-engineer"],
        "level": ["advanced"],
        "category": "blockchain"
    },
    "nft": {
        "why": "Non-Fungible Tokens representing ownership of unique items",
        "roles": ["blockchain-developer", "nft-developer", "digital-artist"],
        "level": ["intermediate", "advanced"],
        "category": "blockchain"
    },

    # ========== GAME DEVELOPMENT ==========
    "unity": {
        "why": "Cross-platform game engine for creating 2D and 3D games",
        "roles": ["game-developer", "unity-developer", "vr-developer"],
        "level": ["intermediate", "advanced"],
        "category": "game-development"
    },
    "unreal-engine": {
        "why": "Game engine known for high-quality graphics and AAA games",
        "roles": ["game-developer", "3d-artist", "game-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "game-development"
    },
    "blender": {
        "why": "Free and open-source 3D creation suite",
        "roles": ["3d-artist", "game-developer", "animator"],
        "level": ["intermediate", "advanced"],
        "category": "game-development"
    },
    "game-design": {
        "why": "Art of applying design and aesthetics to create a game",
        "roles": ["game-designer", "creative-director", "product-manager-games"],
        "level": ["intermediate", "advanced"],
        "category": "game-development"
    },

    # ========== EMBEDDED & IOT ==========
    "embedded-c": {
        "why": "Programming language for microcontroller-based systems",
        "roles": ["embedded-engineer", "firmware-engineer", "iot-developer"],
        "level": ["intermediate", "advanced"],
        "category": "embedded-systems"
    },
    "arduino": {
        "why": "Open-source electronics platform for building digital devices",
        "roles": ["iot-developer", "hardware-engineer", "maker"],
        "level": ["beginner", "intermediate", "advanced"],
        "category": "embedded-systems"
    },
    "raspberry-pi": {
        "why": "Small single-board computer for hardware projects",
        "roles": ["iot-developer", "hardware-engineer", "educator"],
        "level": ["beginner", "intermediate", "advanced"],
        "category": "embedded-systems"
    },
    "iot": {
        "why": "Internet of Things - network of physical objects with embedded technology",
        "roles": ["iot-engineer", "embedded-engineer", "hardware-developer"],
        "level": ["intermediate", "advanced"],
        "category": "embedded-systems"
    },
    "plc": {
        "why": "Programmable Logic Controller for industrial automation",
        "roles": ["industrial-engineer", "automation-engineer", "control-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "embedded-systems"
    },

    # ========== ERP SYSTEMS ==========
    "sap": {
        "why": "Market leader in enterprise resource planning software",
        "roles": ["sap-consultant", "erp-analyst", "business-analyst"],
        "level": ["intermediate", "advanced"],
        "category": "enterprise-systems"
    },
    "sap-fico": {
        "why": "SAP module for Finance and Controlling functions",
        "roles": ["sap-fico-consultant", "financial-analyst", "accountant"],
        "level": ["intermediate", "advanced"],
        "category": "enterprise-systems"
    },
    "oracle-erp": {
        "why": "Oracle's enterprise resource planning software suite",
        "roles": ["oracle-consultant", "erp-analyst", "business-analyst"],
        "level": ["intermediate", "advanced"],
        "category": "enterprise-systems"
    },
    "microsoft-dynamics": {
        "why": "Microsoft's line of enterprise resource planning and customer relationship management software",
        "roles": ["dynamics-consultant", "business-analyst", "crm-consultant"],
        "level": ["intermediate", "advanced"],
        "category": "enterprise-systems"
    },
    "salesforce": {
        "why": "Leading customer relationship management platform",
        "roles": ["salesforce-developer", "crm-consultant", "business-analyst"],
        "level": ["intermediate", "advanced"],
        "category": "enterprise-systems"
    },

    # ========== FINANCE & ACCOUNTING ==========
    "accounting": {
        "why": "Systematic recording, reporting, and analysis of financial transactions",
        "roles": ["accountant", "financial-analyst", "controller"],
        "level": ["intermediate", "advanced"],
        "category": "finance-accounting"
    },
    "financial-modeling": {
        "why": "Creating abstract representation of a real-world financial situation",
        "roles": ["financial-analyst", "investment-banker", "corporate-finance"],
        "level": ["intermediate", "advanced"],
        "category": "finance-accounting"
    },
    "quickbooks": {
        "why": "Accounting software package for small and medium-sized businesses",
        "roles": ["accountant", "bookkeeper", "small-business-owner"],
        "level": ["intermediate", "advanced"],
        "category": "finance-accounting"
    },
    "ifrs": {
        "why": "International Financial Reporting Standards for global accounting",
        "roles": ["accountant", "financial-analyst", "auditor"],
        "level": ["advanced"],
        "category": "finance-accounting"
    },

    # ========== HEALTHCARE IT ==========
    "epic": {
        "why": "Leading electronic health record system in healthcare organizations",
        "roles": ["healthcare-it", "clinical-informaticist", "systems-analyst"],
        "level": ["intermediate", "advanced"],
        "category": "healthcare-it"
    },
    "cerner": {
        "why": "Major electronic health record and health information technology company",
        "roles": ["healthcare-it", "clinical-analyst", "systems-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "healthcare-it"
    },
    "hl7": {
        "why": "Set of international standards for transfer of clinical and administrative data",
        "roles": ["healthcare-it", "integration-engineer", "clinical-informaticist"],
        "level": ["intermediate", "advanced"],
        "category": "healthcare-it"
    },
    "fhir": {
        "why": "Fast Healthcare Interoperability Resources for electronic health records",
        "roles": ["healthcare-it", "integration-engineer", "software-developer-healthcare"],
        "level": ["intermediate", "advanced"],
        "category": "healthcare-it"
    },
    "hipaa": {
        "why": "Health Insurance Portability and Accountability Act for healthcare data privacy",
        "roles": ["healthcare-it", "compliance-officer", "security-engineer-healthcare"],
        "level": ["intermediate", "advanced"],
        "category": "healthcare-it"
    },

    # ========== LEGAL TECH ==========
    "legal-research": {
        "why": "Process of identifying and retrieving information to support legal decision-making",
        "roles": ["lawyer", "paralegal", "legal-analyst"],
        "level": ["intermediate", "advanced"],
        "category": "legal-tech"
    },
    "contract-management": {
        "why": "Management of contracts from vendors, partners, customers, or employees",
        "roles": ["legal-operations", "contract-manager", "procurement-manager"],
        "level": ["intermediate", "advanced"],
        "category": "legal-tech"
    },
    "e-discovery": {
        "why": "Electronic discovery in litigation and government investigations",
        "roles": ["e-discovery-specialist", "legal-tech", "litigation-support"],
        "level": ["intermediate", "advanced"],
        "category": "legal-tech"
    },

    # ========== EDUCATION TECH ==========
    "lms": {
        "why": "Learning Management System for administration, documentation, tracking of educational courses",
        "roles": ["edtech", "instructional-designer", "learning-specialist"],
        "level": ["intermediate", "advanced"],
        "category": "education-tech"
    },
    "moodle": {
        "why": "Open-source learning platform for creating personalized learning environments",
        "roles": ["edtech", "educator", "instructional-designer"],
        "level": ["intermediate", "advanced"],
        "category": "education-tech"
    },
    "instructional-design": {
        "why": "Systematic development of instructional materials using learning theory",
        "roles": ["instructional-designer", "learning-developer", "training-specialist"],
        "level": ["intermediate", "advanced"],
        "category": "education-tech"
    },

    # ========== RETAIL & E-COMMERCE ==========
    "ecommerce": {
        "why": "Buying and selling of goods or services using the internet",
        "roles": ["ecommerce-manager", "digital-marketer", "online-retailer"],
        "level": ["intermediate", "advanced"],
        "category": "retail-ecommerce"
    },
    "shopify": {
        "why": "E-commerce platform for online stores and retail point-of-sale systems",
        "roles": ["ecommerce-developer", "shopify-developer", "online-store-owner"],
        "level": ["intermediate", "advanced"],
        "category": "retail-ecommerce"
    },
    "magento": {
        "why": "Open-source e-commerce platform written in PHP",
        "roles": ["ecommerce-developer", "magento-developer", "php-developer"],
        "level": ["intermediate", "advanced"],
        "category": "retail-ecommerce"
    },
    "inventory-management": {
        "why": "Supervision of non-capitalized assets and stock items",
        "roles": ["inventory-manager", "supply-chain-analyst", "operations-manager"],
        "level": ["intermediate", "advanced"],
        "category": "retail-ecommerce"
    },

    # ========== MANUFACTURING ==========
    "mes": {
        "why": "Manufacturing Execution System for tracking and documenting production",
        "roles": ["manufacturing-engineer", "industrial-engineer", "production-manager"],
        "level": ["intermediate", "advanced"],
        "category": "manufacturing"
    },
    "scada": {
        "why": "Supervisory Control and Data Acquisition for industrial control systems",
        "roles": ["control-engineer", "automation-engineer", "industrial-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "manufacturing"
    },
    "industry-4.0": {
        "why": "Fourth industrial revolution with smart manufacturing",
        "roles": ["industrial-engineer", "manufacturing-engineer", "iot-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "manufacturing"
    },
    "lean-manufacturing": {
        "why": "Systematic method for waste minimization without sacrificing productivity",
        "roles": ["manufacturing-engineer", "operations-manager", "continuous-improvement"],
        "level": ["intermediate", "advanced"],
        "category": "manufacturing"
    },
    "six-sigma": {
        "why": "Set of techniques for process improvement",
        "roles": ["quality-engineer", "process-engineer", "operations-manager"],
        "level": ["intermediate", "advanced"],
        "category": "manufacturing"
    },

    # ========== MEDIA & ENTERTAINMENT ==========
    "video-editing": {
        "why": "Manipulation and arrangement of video shots",
        "roles": ["video-editor", "content-creator", "film-producer"],
        "level": ["intermediate", "advanced"],
        "category": "media-entertainment"
    },
    "premiere-pro": {
        "why": "Timeline-based video editing software application",
        "roles": ["video-editor", "filmmaker", "content-creator"],
        "level": ["intermediate", "advanced"],
        "category": "media-entertainment"
    },
    "after-effects": {
        "why": "Digital visual effects, motion graphics, and compositing application",
        "roles": ["motion-graphics-artist", "vfx-artist", "video-editor"],
        "level": ["intermediate", "advanced"],
        "category": "media-entertainment"
    },
    "ott": {
        "why": "Over-the-top media services delivered directly via the Internet",
        "roles": ["streaming-engineer", "media-engineer", "content-distribution"],
        "level": ["intermediate", "advanced"],
        "category": "media-entertainment"
    },

    # ========== REAL ESTATE TECH ==========
    "proptech": {
        "why": "Technology used in the real estate industry",
        "roles": ["real-estate-tech", "proptech-developer", "real-estate-analyst"],
        "level": ["intermediate", "advanced"],
        "category": "real-estate-tech"
    },
    "property-management": {
        "why": "Operation, control, and oversight of real estate",
        "roles": ["property-manager", "real-estate-agent", "facilities-manager"],
        "level": ["intermediate", "advanced"],
        "category": "real-estate-tech"
    },
    "gis": {
        "why": "Geographic Information System for capturing and analyzing spatial data",
        "roles": ["gis-analyst", "geospatial-engineer", "urban-planner"],
        "level": ["intermediate", "advanced"],
        "category": "real-estate-tech"
    },

    # ========== METHODOLOGIES ==========
    "agile": {
        "why": "Iterative approach to project management and software development",
        "roles": ["all"],
        "level": ["beginner", "intermediate", "advanced"],
        "category": "methodologies"
    },
    "scrum": {
        "why": "Agile framework for managing complex projects",
        "roles": ["scrum-master", "product-owner", "agile-coach"],
        "level": ["intermediate", "advanced"],
        "category": "methodologies"
    },
    "devops": {
        "why": "Combination of cultural philosophies, practices, and tools",
        "roles": ["devops-engineer", "sre", "platform-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "methodologies"
    },
    "pmp": {
        "why": "Project Management Professional certification for project managers",
        "roles": ["project-manager", "program-manager", "delivery-manager"],
        "level": ["advanced"],
        "category": "methodologies"
    },

    # ========== SOFT SKILLS ==========
    "communication": {
        "why": "Essential for collaboration, requirements gathering, and stakeholder management",
        "roles": ["all"],
        "level": ["all"],
        "category": "soft-skills"
    },
    "leadership": {
        "why": "Ability to guide and influence teams towards achieving goals",
        "roles": ["team-lead", "manager", "director", "executive"],
        "level": ["intermediate", "advanced"],
        "category": "soft-skills"
    },
    "problem-solving": {
        "why": "Core ability to analyze complex issues and develop effective solutions",
        "roles": ["all"],
        "level": ["all"],
        "category": "soft-skills"
    },
    "teamwork": {
        "why": "Collaborative effort of a group to achieve a common goal",
        "roles": ["all"],
        "level": ["all"],
        "category": "soft-skills"
    },

    # ========== LANGUAGES ==========
    "english": {
        "why": "Global business language and primary language of technology",
        "roles": ["all"],
        "level": ["beginner", "intermediate", "advanced", "native"],
        "category": "languages"
    },
    "spanish": {
        "why": "Second most spoken language globally, important for Americas and Europe",
        "roles": ["all"],
        "level": ["beginner", "intermediate", "advanced", "native"],
        "category": "languages"
    },
    "mandarin": {
        "why": "Most spoken language globally, crucial for business in China and Asia",
        "roles": ["all"],
        "level": ["beginner", "intermediate", "advanced", "native"],
        "category": "languages"
    },

    # ========== PRODUCT MANAGEMENT ==========
    "product-management": {
        "why": "Organizational function that guides every step of a product's lifecycle",
        "roles": ["product-manager", "product-owner", "business-analyst"],
        "level": ["intermediate", "advanced"],
        "category": "product-management"
    },
    "product-strategy": {
        "why": "High-level plan for achieving specific goals with a product",
        "roles": ["product-manager", "product-lead", "director-product"],
        "level": ["advanced"],
        "category": "product-management"
    },
    "user-research": {
        "why": "Understanding user behaviors, needs, and motivations",
        "roles": ["product-manager", "ux-researcher", "designer"],
        "level": ["intermediate", "advanced"],
        "category": "product-management"
    },

    # ========== UX/UI DESIGN ==========
    "ux-design": {
        "why": "Process of enhancing user satisfaction by improving usability and accessibility",
        "roles": ["ux-designer", "product-designer", "interaction-designer"],
        "level": ["intermediate", "advanced"],
        "category": "ux-ui-design"
    },
    "ui-design": {
        "why": "Design of user interfaces for machines and software",
        "roles": ["ui-designer", "visual-designer", "product-designer"],
        "level": ["intermediate", "advanced"],
        "category": "ux-ui-design"
    },
    "figma": {
        "why": "Collaborative interface design tool used for UI/UX design",
        "roles": ["ui-designer", "ux-designer", "product-designer"],
        "level": ["intermediate", "advanced"],
        "category": "ux-ui-design"
    },
    "wireframing": {
        "why": "Creating basic visual guide of a user interface",
        "roles": ["ux-designer", "product-designer", "business-analyst"],
        "level": ["intermediate", "advanced"],
        "category": "ux-ui-design"
    },

    # ========== QA & TESTING ==========
    "quality-assurance": {
        "why": "Process of ensuring product quality before release",
        "roles": ["qa-engineer", "test-engineer", "quality-analyst"],
        "level": ["intermediate", "advanced"],
        "category": "qa-testing"
    },
    "test-automation": {
        "why": "Use of software to control test execution and compare actual outcomes",
        "roles": ["test-automation-engineer", "sdet", "qa-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "qa-testing"
    },
    "performance-testing": {
        "why": "Testing to determine system performance under workload",
        "roles": ["performance-engineer", "qa-engineer", "devops"],
        "level": ["intermediate", "advanced"],
        "category": "qa-testing"
    },

    # ========== TECHNICAL WRITING ==========
    "technical-writing": {
        "why": "Writing technical documentation for products or services",
        "roles": ["technical-writer", "documentation-specialist", "content-developer"],
        "level": ["intermediate", "advanced"],
        "category": "technical-writing"
    },
    "documentation": {
        "why": "Creation of documents that explain product functionality",
        "roles": ["technical-writer", "developer", "product-manager"],
        "level": ["intermediate", "advanced"],
        "category": "technical-writing"
    },

    # ========== HARDWARE & NETWORKING ==========
    "networking": {
        "why": "Practice of linking computing devices together for data sharing",
        "roles": ["network-engineer", "system-admin", "network-architect"],
        "level": ["intermediate", "advanced"],
        "category": "hardware-networking"
    },
    "ccna": {
        "why": "Cisco Certified Network Associate certification for networking",
        "roles": ["network-engineer", "system-admin", "network-analyst"],
        "level": ["intermediate", "advanced"],
        "category": "hardware-networking"
    },
    "windows-server": {
        "why": "Microsoft's server operating system",
        "roles": ["system-admin", "windows-admin", "it-support"],
        "level": ["intermediate", "advanced"],
        "category": "hardware-networking"
    },
    "linux-server": {
        "why": "Linux-based server operating system",
        "roles": ["linux-admin", "devops", "system-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "hardware-networking"
    },

    # ========== AEROSPACE & DEFENSE ==========
    "aerospace": {
        "why": "Industry dealing with aircraft and spacecraft",
        "roles": ["aerospace-engineer", "systems-engineer", "avionics-engineer"],
        "level": ["advanced"],
        "category": "aerospace-defense"
    },
    "do-178c": {
        "why": "Software considerations in airborne systems and equipment certification",
        "roles": ["aerospace-software-engineer", "safety-engineer", "certification-engineer"],
        "level": ["advanced"],
        "category": "aerospace-defense"
    },
    "avionics": {
        "why": "Electronic systems used in aircraft, artificial satellites, and spacecraft",
        "roles": ["avionics-engineer", "embedded-engineer", "systems-engineer"],
        "level": ["advanced"],
        "category": "aerospace-defense"
    },

    # ========== AUTOMOTIVE ==========
    "automotive": {
        "why": "Industry involved in the design, development, manufacturing, and selling of vehicles",
        "roles": ["automotive-engineer", "embedded-automotive", "systems-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "automotive"
    },
    "adas": {
        "why": "Advanced Driver Assistance Systems for vehicle safety",
        "roles": ["adas-engineer", "automotive-software-engineer", "safety-engineer"],
        "level": ["advanced"],
        "category": "automotive"
    },
    "autonomous-vehicles": {
        "why": "Self-driving vehicle technology",
        "roles": ["autonomous-vehicle-engineer", "ml-engineer-automotive", "robotics-engineer"],
        "level": ["advanced"],
        "category": "automotive"
    },
    "can-bus": {
        "why": "Controller Area Network bus for vehicle communication",
        "roles": ["embedded-automotive", "automotive-engineer", "network-engineer-automotive"],
        "level": ["intermediate", "advanced"],
        "category": "automotive"
    },

    # ========== ENERGY & UTILITIES ==========
    "energy": {
        "why": "Industry involved in production and distribution of energy",
        "roles": ["energy-engineer", "power-systems-engineer", "renewable-energy-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "energy-utilities"
    },
    "scada-energy": {
        "why": "SCADA systems for energy distribution and management",
        "roles": ["scada-engineer", "energy-systems-engineer", "control-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "energy-utilities"
    },
    "smart-grid": {
        "why": "Electrical grid with automation and communication technology",
        "roles": ["smart-grid-engineer", "power-engineer", "systems-engineer-energy"],
        "level": ["advanced"],
        "category": "energy-utilities"
    },
    "renewable-energy": {
        "why": "Energy from sources that are naturally replenishing",
        "roles": ["renewable-energy-engineer", "solar-engineer", "wind-energy-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "energy-utilities"
    },

    # ========== PHARMACEUTICAL & LIFE SCIENCES ==========
    "pharma": {
        "why": "Pharmaceutical industry involved in drug discovery and development",
        "roles": ["pharma-it", "clinical-data-manager", "regulatory-affairs"],
        "level": ["intermediate", "advanced"],
        "category": "pharmaceutical-life-sciences"
    },
    "gxp": {
        "why": "Good Practice quality guidelines and regulations in life sciences",
        "roles": ["quality-assurance-pharma", "regulatory-affairs", "compliance-officer-pharma"],
        "level": ["advanced"],
        "category": "pharmaceutical-life-sciences"
    },
    "clinical-trials": {
        "why": "Research studies that test medical interventions in people",
        "roles": ["clinical-research-associate", "clinical-data-manager", "biostatistician"],
        "level": ["intermediate", "advanced"],
        "category": "pharmaceutical-life-sciences"
    },
    "lims": {
        "why": "Laboratory Information Management System for lab data management",
        "roles": ["lims-admin", "lab-manager", "quality-assurance-lab"],
        "level": ["intermediate", "advanced"],
        "category": "pharmaceutical-life-sciences"
    },
    "bioinformatics": {
        "why": "Application of computer technology to biological data management",
        "roles": ["bioinformatician", "computational-biologist", "genomics-data-scientist"],
        "level": ["advanced"],
        "category": "pharmaceutical-life-sciences"
    },

    # ========== CONSTRUCTION TECH ==========
    "construction-tech": {
        "why": "Technology used in the construction industry",
        "roles": ["construction-technologist", "bim-manager", "project-manager-construction"],
        "level": ["intermediate", "advanced"],
        "category": "construction-tech"
    },
    "bim": {
        "why": "Building Information Modeling for 3D model-based design",
        "roles": ["bim-specialist", "architect", "construction-manager"],
        "level": ["intermediate", "advanced"],
        "category": "construction-tech"
    },
    "autocad": {
        "why": "Computer-aided design software for 2D and 3D design",
        "roles": ["cad-drafter", "architect", "engineer"],
        "level": ["intermediate", "advanced"],
        "category": "construction-tech"
    },
    "revit": {
        "why": "Building information modeling software for architects and engineers",
        "roles": ["bim-specialist", "architect", "structural-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "construction-tech"
    },

    # ========== TRAVEL & HOSPITALITY ==========
    "travel-tech": {
        "why": "Technology used in the travel and tourism industry",
        "roles": ["travel-tech-developer", "tourism-manager", "hospitality-it"],
        "level": ["intermediate", "advanced"],
        "category": "travel-hospitality"
    },
    "gds": {
        "why": "Global Distribution System for travel bookings",
        "roles": ["gds-specialist", "travel-agent", "airline-it"],
        "level": ["intermediate", "advanced"],
        "category": "travel-hospitality"
    },
    "hotel-management": {
        "why": "Management of hotel operations and services",
        "roles": ["hotel-manager", "hospitality-manager", "operations-manager-hotel"],
        "level": ["intermediate", "advanced"],
        "category": "travel-hospitality"
    },
    "revenue-management": {
        "why": "Application of disciplined analytics to predict consumer behavior",
        "roles": ["revenue-manager", "pricing-analyst", "hospitality-analyst"],
        "level": ["intermediate", "advanced"],
        "category": "travel-hospitality"
    },

    # ========== INSURANCE TECH ==========
    "insurtech": {
        "why": "Technology used in the insurance industry",
        "roles": ["insurtech-developer", "insurance-analyst", "product-manager-insurance"],
        "level": ["intermediate", "advanced"],
        "category": "insurance-tech"
    },
    "insurance": {
        "why": "Practice of risk management through transfer",
        "roles": ["insurance-underwriter", "actuary", "claims-adjuster"],
        "level": ["intermediate", "advanced"],
        "category": "insurance-tech"
    },
    "policy-administration": {
        "why": "Management of insurance policy lifecycle",
        "roles": ["policy-administrator", "insurance-operations", "underwriting-assistant"],
        "level": ["intermediate", "advanced"],
        "category": "insurance-tech"
    },
    "actuarial-science": {
        "why": "Discipline that applies mathematical and statistical methods to risk assessment",
        "roles": ["actuary", "risk-analyst", "pricing-analyst-insurance"],
        "level": ["advanced"],
        "category": "insurance-tech"
    },

    # ========== TELECOMMUNICATIONS ==========
    "telecom": {
        "why": "Telecommunications industry for transmitting information",
        "roles": ["telecom-engineer", "network-engineer-telecom", "systems-engineer-telecom"],
        "level": ["intermediate", "advanced"],
        "category": "telecommunications"
    },
    "5g": {
        "why": "Fifth generation technology standard for broadband cellular networks",
        "roles": ["5g-engineer", "wireless-engineer", "network-architect-telecom"],
        "level": ["advanced"],
        "category": "telecommunications"
    },
    "voip": {
        "why": "Voice over Internet Protocol for voice communications over IP networks",
        "roles": ["voip-engineer", "telecom-engineer", "network-engineer"],
        "level": ["intermediate", "advanced"],
        "category": "telecommunications"
    },

    # ========== GOVERNMENT & PUBLIC SECTOR ==========
    "government": {
        "why": "Public sector organizations and administration",
        "roles": ["government-it", "public-administrator", "policy-analyst"],
        "level": ["intermediate", "advanced"],
        "category": "government-public-sector"
    },
    "e-governance": {
        "why": "Application of information technology for government services",
        "roles": ["e-governance-specialist", "digital-government", "public-sector-it"],
        "level": ["intermediate", "advanced"],
        "category": "government-public-sector"
    },
    "public-policy": {
        "why": "Principles on which social laws are based",
        "roles": ["policy-analyst", "government-advisor", "legislative-assistant"],
        "level": ["intermediate", "advanced"],
        "category": "government-public-sector"
    },
}

# ──────────────────────────────────────────────────────────────────────────────
# FINAL FILTERED SKILL_META
# Only entries that exist in SKILLS_SET are kept
# ──────────────────────────────────────────────────────────────────────────────
SKILL_META: Dict[str, Dict[str, Any]] = {
    k: v for k, v in _RAW_SKILL_META.items() if k in SKILLS_SET
}

# Optional debug output (remove in production)
if __name__ == "__main__":
    print(f"Raw metadata entries:     {len(_RAW_SKILL_META):,}")
    print(f"After filtering:          {len(SKILL_META):,}")
    print(f"Kept skills count:        {len(SKILL_META)}")
    print("Example kept keys:", list(SKILL_META.keys())[:8])