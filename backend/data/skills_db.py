# backend/data/skills_db.py

SKILLS = {
    # ========== FRONTEND TECHNOLOGIES ==========
    # Core Web
    "html", "html5", "xhtml", "semantic-html", "accessibility", "wai-aria",
    "css", "css3", "css-grid", "flexbox", "responsive-design", "media-queries",
    "javascript", "ecmascript", "es6", "es7", "es8", "es9", "es10", "es2020", "es2021", "es2022",
    "typescript", "tsc", "type-annotations", "interfaces", "generics",
    "dom", "bom", "web-apis", "localstorage", "sessionstorage", "indexeddb",
    "websockets", "webrtc", "service-workers", "web-workers", "webgl", "canvas",
    "svg", "web-components", "custom-elements", "shadow-dom",
    
    # Frameworks & Libraries
    "react", "react-16", "react-17", "react-18", "react-19", "jsx", "tsx",
    "react-hooks", "useState", "useEffect", "useContext", "useReducer", "useCallback", "useMemo",
    "react-router", "react-router-dom", "react-context", "react-error-boundaries",
    "react-suspense", "react-lazy", "react-portals", "react-fragments",
    "nextjs", "next-13", "next-14", "app-router", "pages-router", "server-components",
    "gatsby", "remix", "astro", "svelte", "sveltekit", "solidjs", "qwik",
    "vue", "vue2", "vue3", "composition-api", "options-api", "vue-router", "vuex", "pinia",
    "nuxt", "nuxt2", "nuxt3", "angular", "angularjs", "angular2+", "rxjs",
    "ngrx", "angular-forms", "angular-material", "angular-cli",
    
    # State Management
    "redux", "redux-toolkit", "redux-saga", "redux-thunk", "redux-observable",
    "mobx", "mobx-state-tree", "zustand", "recoil", "jotai", "xstate",
    "vuex", "pinia", "ngrx", "apollo-client", "relay",
    
    # Styling
    "css-preprocessors", "sass", "scss", "less", "stylus", "postcss",
    "css-in-js", "styled-components", "emotion", "styled-jsx", "linaria",
    "tailwind-css", "bootstrap", "material-ui", "ant-design", "chakra-ui",
    "bulma", "foundation", "semantic-ui", "prime-react", "evergreen",
    "headless-ui", "radix-ui", "shadcn-ui", "daisyui",
    
    # Build Tools
    "webpack", "webpack-config", "loaders", "plugins", "code-splitting",
    "vite", "rollup", "parcel", "esbuild", "swc", "rome",
    "babel", "polyfills", "transpilation", "npm", "yarn", "pnpm", "npm-scripts",
    "lerna", "nx", "turbo", "monorepo", "module-federation",
    
    # Testing
    "jest", "vitest", "mocha", "chai", "sinon", "enzyme", "testing-library",
    "cypress", "playwright", "puppeteer", "selenium", "webdriverio",
    "karma", "jasmine", "istanbul", "nyc", "code-coverage",
    "unit-testing", "integration-testing", "e2e-testing", "snapshot-testing",
    "tdd", "bdd", "acceptance-testing",
    
    # Performance
    "web-vitals", "core-web-vitals", "lighthouse", "pagespeed-insights",
    "code-splitting", "lazy-loading", "tree-shaking", "dead-code-elimination",
    "caching", "cdn", "http2", "http3", "preload", "prefetch",
    "optimization", "minification", "compression", "gzip", "brotli",
    
    # PWA & Mobile Web
    "pwa", "service-workers", "manifest", "offline-first", "app-shell",
    "web-app-manifest", "push-notifications", "background-sync",
    "responsive-web-design", "mobile-first", "touch-events",
    "amp", "accelerated-mobile-pages",
    
    # ========== BACKEND TECHNOLOGIES ==========
    # Server-Side Languages
    "nodejs", "express", "koa", "fastify", "nest", "hapi", "sails",
    "python", "django", "django-rest-framework", "flask", "fastapi",
    "pyramid", "sanic", "tornado", "bottle", "cherrypy",
    "java", "spring", "spring-boot", "spring-mvc", "spring-security",
    "spring-data", "spring-cloud", "jakarta-ee", "jax-rs", "jax-ws",
    "csharp", "aspnet", "aspnet-core", "blazor", "entity-framework",
    "php", "laravel", "symfony", "codeigniter", "cakephp", "yii", "zend",
    "ruby", "ruby-on-rails", "sinatra", "grape", "hanami",
    "go", "gin", "echo", "fiber", "beego", "revel", "martini",
    "rust", "actix-web", "rocket", "warp", "axum", "tide",
    "kotlin", "ktor", "jvm", "scala", "play-framework", "akka",
    "elixir", "phoenix", "erlang", "otp",
    
    # Databases - SQL
    "sql", "mysql", "mariadb", "postgresql", "oracle-database",
    "sql-server", "db2", "sqlite", "cockroachdb", "tidb", "yugabytedb",
    "plsql", "tsql", "plpgsql", "database-design", "normalization",
    "1nf", "2nf", "3nf", "bcnf", "indexing", "query-optimization",
    "stored-procedures", "triggers", "views", "materialized-views",
    "transactions", "acid", "isolation-levels", "locking", "deadlocks",
    "backup-recovery", "replication", "sharding", "partitioning",
    
    # Databases - NoSQL
    "mongodb", "mongoose", "redis", "elasticsearch", "cassandra",
    "couchdb", "couchbase", "dynamodb", "firestore", "cosmosdb",
    "arangodb", "neo4j", "orientdb", "riak", "hbase",
    "document-database", "key-value-store", "column-family",
    "graph-database", "time-series-database",
    
    # ORMs & Query Builders
    "prisma", "sequelize", "typeorm", "mongoose", "sqlalchemy",
    "django-orm", "entity-framework", "hibernate", "jpa", "mybatis",
    "knex", "bookshelf", "waterline", "activerecord", "dapper",
    
    # API Development
    "rest", "restful-apis", "graphql", "grpc", "soap", "websockets",
    "webhooks", "web-sockets", "socketio", "server-sent-events",
    "openapi", "swagger", "postman", "insomnia", "graphql-schema",
    "apollo-server", "hasura", "graphql-yoga", "rest-assured",
    "api-design", "api-gateway", "api-management", "rate-limiting",
    "throttling", "circuit-breaker", "retry-pattern", "timeout",
    
    # Authentication & Authorization
    "oauth2", "openid-connect", "jwt", "session-management",
    "saml", "ldap", "kerberos", "basic-auth", "digest-auth",
    "multi-factor-auth", "biometric-auth", "single-sign-on",
    "rbac", "role-based-access-control", "abac", "pbac",
    
    # Message Queues
    "rabbitmq", "kafka", "activemq", "sqs", "service-bus",
    "zeromq", "nats", "redis-pubsub", "google-pubsub",
    "message-brokers", "event-driven-architecture", "event-sourcing",
    "cqrs", "event-storming",
    
    # Search Engines
    "elasticsearch", "solr", "algolia", "meilisearch", "typesense",
    "lucene", "opensearch", "full-text-search", "fuzzy-search",
    "autocomplete", "search-ranking", "relevance-tuning",
    
    # ========== MOBILE DEVELOPMENT ==========
    # Cross-Platform
    "react-native", "expo", "flutter", "dart", "ionic", "capacitor",
    "cordova", "phonegap", "xamarin", "maUI", "unity",
    "nativescript", "quasar", "framework7",
    
    # Android
    "android", "kotlin", "java-android", "android-sdk", "android-studio",
    "jetpack-compose", "material-design", "room-database", "viewmodel",
    "livedata", "coroutines", "flow", "dagger", "hilt", "retrofit",
    "okhttp", "glide", "picasso", "recyclerview", "navigation-component",
    
    # iOS
    "ios", "swift", "swiftui", "objective-c", "xcode", "cocoapods",
    "carthage", "swift-package-manager", "core-data", "realm",
    "alamofire", "kingfisher", "sdwebimage", "combine", "async-await",
    
    # Mobile Testing
    "appium", "detox", "espresso", "xctest", "ui-automator",
    "firebase-test-lab", "browserstack", "sauce-labs",
    
    # App Distribution
    "fastlane", "codemagic", "bitrise", "app-center", "testflight",
    "google-play-console", "app-store-connect", "code-signing",
    
    # ========== DEVOPS & CLOUD ==========
    # Cloud Providers
    "aws", "ec2", "s3", "lambda", "rds", "dynamodb", "api-gateway",
    "cloudfront", "route53", "vpc", "iam", "cloudformation", "cloudwatch",
    "sns", "sqs", "sagemaker", "rekognition", "elastic-beanstalk",
    "azure", "azure-functions", "azure-sql", "azure-devops", "azure-ad",
    "azure-blob-storage", "azure-kubernetes-service", "azure-cosmos-db",
    "gcp", "google-cloud-functions", "firebase", "cloud-run", "bigquery",
    "cloud-sql", "cloud-storage", "kubernetes-engine", "app-engine",
    "oracle-cloud", "ibm-cloud", "alibaba-cloud", "digitalocean",
    "linode", "vultr", "heroku", "netlify", "vercel", "render",
    
    # Containers
    "docker", "docker-compose", "docker-swarm", "podman", "containerd",
    "dockerfile", "multi-stage-builds", "image-optimization",
    "container-security", "image-scanning", "registry",
    
    # Orchestration
    "kubernetes", "k8s", "helm", "kustomize", "kubectl", "minikube",
    "kind", "k3s", "openshift", "rancher", "nomad", "mesos",
    "deployments", "services", "ingress", "configmaps", "secrets",
    "statefulsets", "daemonsets", "jobs", "cronjobs", "operators",
    "service-mesh", "istio", "linkerd", "consul",
    
    # Infrastructure as Code
    "terraform", "pulumi", "cloudformation", "aws-cdk", "cdktf",
    "ansible", "puppet", "chef", "saltstack", "packer", "vagrant",
    
    # CI/CD
    "jenkins", "jenkinsfile", "pipeline", "github-actions", "gitlab-ci",
    "circleci", "travis-ci", "bamboo", "teamcity", "argo-cd", "flux",
    "spinnaker", "tekton", "drone", "woodpecker", "go-cd",
    
    # Monitoring & Observability
    "prometheus", "grafana", "elk-stack", "elasticsearch", "logstash", "kibana",
    "splunk", "datadog", "new-relic", "appdynamics", "dynatrace",
    "sentry", "rollbar", "bugsnag", "cloudwatch", "azure-monitor",
    "stackdriver", "jaeger", "zipkin", "opentelemetry", "distributed-tracing",
    
    # Security & Compliance
    "vault", "keycloak", "oauth2-proxy", "cert-manager", "lets-encrypt",
    "security-scanning", "dependency-checking", "snyk", "sonarqube",
    "owasp", "zap", "burp-suite", "nessus", "qualys",
    
    # ========== DATA SCIENCE & AI/ML ==========
    # Programming & Math
    "python", "r", "julia", "matlab", "octave", "sas", "spss", "stata",
    "statistics", "probability", "linear-algebra", "calculus", "discrete-math",
    
    # Data Manipulation
    "pandas", "numpy", "polars", "dask", "modin", "vaex",
    "data-cleaning", "data-wrangling", "data-transformation",
    "feature-engineering", "feature-selection", "dimensionality-reduction",
    
    # Machine Learning
    "scikit-learn", "tensorflow", "pytorch", "keras", "mxnet",
    "xgboost", "lightgbm", "catboost", "h2o", "mlflow",
    "supervised-learning", "unsupervised-learning", "semi-supervised",
    "reinforcement-learning", "deep-learning", "neural-networks",
    
    # ML Algorithms
    "linear-regression", "logistic-regression", "decision-trees",
    "random-forest", "svm", "knn", "k-means", "hierarchical-clustering",
    "dbscan", "pca", "t-sne", "lda", "naive-bayes", "gradient-boosting",
    
    # Deep Learning
    "cnn", "rnn", "lstm", "gru", "transformer", "attention-mechanism",
    "gan", "autoencoder", "vae", "bert", "gpt", "transfer-learning",
    "fine-tuning", "model-serving", "onnx", "tensorrt",
    
    # NLP
    "nltk", "spacy", "gensim", "transformers", "huggingface",
    "tokenization", "stemming", "lemmatization", "pos-tagging",
    "named-entity-recognition", "sentiment-analysis", "topic-modeling",
    "text-classification", "machine-translation", "text-generation",
    
    # Computer Vision
    "opencv", "pillow", "scikit-image", "yolo", "faster-rcnn",
    "mask-rcnn", "object-detection", "image-segmentation",
    "image-classification", "face-recognition", "ocr",
    
    # Big Data
    "hadoop", "hdfs", "mapreduce", "yarn", "spark", "pyspark",
    "spark-sql", "spark-streaming", "hive", "pig", "hbase",
    "kafka", "flink", "storm", "beam", "airflow", "luigi",
    "presto", "trino", "druid", "clickhouse",
    
    # Data Platforms
    "databricks", "snowflake", "bigquery", "redshift", "synapse",
    "data-lake", "data-warehouse", "data-mesh", "data-fabric",
    
    # Visualization
    "matplotlib", "seaborn", "plotly", "bokeh", "ggplot2", "d3js",
    "tableau", "powerbi", "looker", "superset", "metabase", "redash",
    
    # ========== CYBERSECURITY ==========
    # Security Domains
    "network-security", "application-security", "cloud-security",
    "endpoint-security", "mobile-security", "iot-security",
    
    # Offensive Security
    "penetration-testing", "ethical-hacking", "red-teaming",
    "vulnerability-assessment", "security-auditing", "pentest-frameworks",
    
    # Defensive Security
    "soc", "security-operations-center", "incident-response",
    "threat-hunting", "threat-intelligence", "digital-forensics",
    "malware-analysis", "reverse-engineering",
    
    # Cryptography
    "cryptography", "encryption", "symmetric", "asymmetric", "hashing",
    "digital-signatures", "pki", "ssl-tls", "certificates",
    
    # Network Security
    "firewalls", "ids", "ips", "waf", "vpn", "zero-trust",
    "network-segmentation", "microsegmentation",
    
    # Tools
    "burp-suite", "metasploit", "wireshark", "nmap", "nessus",
    "qualys", "openvas", "sqlmap", "john-the-ripper", "hashcat",
    
    # Standards & Compliance
    "owasp", "nist", "iso-27001", "gdpr", "hipaa", "pci-dss",
    "sox", "fedramp", "cis-benchmarks",
    
    # ========== BLOCKCHAIN & WEB3 ==========
    "blockchain", "ethereum", "bitcoin", "solidity", "smart-contracts",
    "web3js", "ethersjs", "hardhat", "truffle", "foundry", "ganache",
    "defi", "decentralized-finance", "nft", "non-fungible-tokens",
    "dapp", "decentralized-apps", "ipfs", "filecoin", "arweave",
    "cryptocurrency", "tokenomics", "consensus-mechanisms",
    "proof-of-work", "proof-of-stake", "layer2", "rollups",
    "hyperledger", "fabric", "besu", "cordapp", "quorum",
    
    # ========== GAME DEVELOPMENT ==========
    "unity", "csharp", "unreal-engine", "cplusplus", "blueprints",
    "godot", "game-maker", "construct", "rpg-maker", "phaser",
    "game-design", "level-design", "game-mechanics", "balancing",
    "3d-modeling", "blender", "maya", "3ds-max", "zbrush",
    "substance-painter", "substance-designer", "marvelous-designer",
    "shaders", "hlsl", "glsl", "shader-graph", "visual-shader",
    "vfx", "particle-systems", "physics", "ragdoll", "animation",
    "rigging", "skinning", "mocap", "sound-design", "fmode", "wwise",
    "vr", "ar", "mixed-reality", "oculus", "htc-vive", "hololens",
    
    # ========== EMBEDDED SYSTEMS & IOT ==========
    "embedded-c", "c", "cplusplus", "assembly", "rtos", "freertos",
    "zephyr", "contiki", "micropython", "circuitpython",
    "arduino", "raspberry-pi", "esp32", "esp8266", "stm32",
    "microcontroller", "microprocessor", "fpga", "verilog", "vhdl",
    "systemc", "embedded-linux", "yocto", "buildroot",
    "iot", "mqtt", "coap", "modbus", "opc-ua", "lora", "zigbee",
    "bluetooth-low-energy", "nb-iot", "ltem", "industrial-iot",
    "sensors", "actuators", "plc", "scada", "hmi", "industrial-automation",
    
    # ========== ENTERPRISE SYSTEMS ==========
    # ERP Systems
    "sap", "sap-fico", "sap-mm", "sap-sd", "sap-pp", "sap-hr",
    "sap-bw", "sap-bpc", "sap-cpi", "sap-btp", "sap-s4hana",
    "oracle-erp", "oracle-fusion", "peoplesoft", "ebs", "jdedwards",
    "microsoft-dynamics", "dynamics-365", "dynamics-nav", "dynamics-ax",
    "netsuite", "infor", "workday", "sage", "epicor",
    
    # CRM
    "salesforce", "salesforce-lightning", "apex", "visualforce",
    "salesforce-cpq", "salesforce-marketing-cloud", "salesforce-service-cloud",
    "hubspot", "zoho-crm", "microsoft-dynamics-crm", "sugar-crm",
    "pipedrive", "freshsales", "insightly",
    
    # Business Intelligence
    "sap-bw", "sap-bobj", "sap-analytics-cloud",
    "oracle-bi", "obiee", "oracle-analytics",
    "ibm-cognos", "microstrategy", "qlik", "qlikview", "qliksense",
    "tableau", "powerbi", "looker", "thoughtspot",
    
    # EPM & CPM
    "hyperion", "oracle-hyperion", "anaplan", "adaptive-insights",
    "tm1", "ibm-planning-analytics", "one-stream",
    
    # ========== FINANCE & ACCOUNTING ==========
    "accounting", "financial-accounting", "managerial-accounting",
    "financial-modeling", "financial-analysis", "financial-forecasting",
    "quickbooks", "xero", "sage", "tally", "oracle-financials",
    "sap-fico", "ifrs", "gaap", "us-gaap", "ind-as", "taxation",
    "gst", "vat", "auditing", "internal-audit", "external-audit",
    "risk-management", "fraud-detection", "anti-money-laundering",
    "sox-compliance", "financial-risk", "credit-risk", "market-risk",
    "treasury-management", "cash-management", "investment-banking",
    
    # ========== HEALTHCARE IT ==========
    "healthcare-it", "epic", "cerner", "meditech", "allscripts",
    "athenahealth", "eclinicalworks", "nextgen", "greenway",
    "hl7", "fhir", "dicom", "icd-10", "cpt", "hcpcs", "loinc",
    "snomed", "hipaa", "hitech", "meaningful-use", "ehr", "emr",
    "telemedicine", "telehealth", "clinical-informatics",
    "health-data-analytics", "population-health", "healthcare-interoperability",
    
    # ========== LEGAL TECH ==========
    "legal-tech", "legal-research", "westlaw", "lexisnexis",
    "contract-management", "contract-lifecycle-management",
    "e-discovery", "document-review", "case-management",
    "legal-analytics", "compliance", "regulatory-compliance",
    "clio", "leap", "mycase", "smokeball", "filevine",
    
    # ========== EDUCATION TECH ==========
    "edtech", "lms", "learning-management-system",
    "moodle", "blackboard", "canvas", "schoology",
    "google-classroom", "brightspace", "sakai",
    "instructional-design", "e-learning", "online-learning",
    "scorm", "xapi", "cmi5", "learning-analytics",
    "articulate", "storyline", "rise", "captivate",
    "kahoot", "quizlet", "nearpod", "peardeck",
    
    # ========== RETAIL & E-COMMERCE ==========
    "ecommerce", "magento", "shopify", "woocommerce", "bigcommerce",
    "prestashop", "demandware", "salesforce-commerce-cloud",
    "oracle-commerce", "ibm-websphere-commerce", "sap-commerce-cloud",
    "inventory-management", "order-management", "supply-chain-management",
    "pos", "point-of-sale", "omnichannel", "retail-analytics",
    "customer-experience", "personalization", "recommendation-engines",
    
    # ========== SUPPLY CHAIN & LOGISTICS ==========
    "supply-chain", "logistics", "sap-scm", "oracle-scm",
    "manhattan-wms", "blue-yonder", "jda", "oracle-transportation-management",
    "warehouse-management", "inventory-optimization", "demand-forecasting",
    "procurement", "sourcing", "vendor-management", "logistics-management",
    "transportation-management", "freight-management", "last-mile-delivery",
    
    # ========== MANUFACTURING ==========
    "manufacturing", "mes", "manufacturing-execution-system",
    "scada", "supervisory-control", "plc", "programmable-logic-controller",
    "industry-4.0", "industrial-iot", "smart-factory", "digital-twin",
    "predictive-maintenance", "quality-control", "spc", "statistical-process-control",
    "lean-manufacturing", "six-sigma", "tpm", "total-productive-maintenance",
    "process-optimization", "production-planning", "mrp", "material-requirements-planning",
    
    # ========== MEDIA & ENTERTAINMENT ==========
    "media", "entertainment", "video-editing", "premiere-pro", "final-cut-pro",
    "davinci-resolve", "avid", "audio-production", "pro-tools", "logic-pro",
    "ableton", "vfx", "visual-effects", "after-effects", "nuke",
    "motion-graphics", "cinema-4d", "color-grading", "broadcast",
    "ott", "over-the-top", "streaming", "video-on-demand",
    "cms", "content-management-system", "dam", "digital-asset-management",
    
    # ========== REAL ESTATE TECH ==========
    "proptech", "real-estate-tech", "property-management",
    "real-estate-crm", "zillow", "redfin", "realtorcom",
    "virtual-tours", "3d-tours", "gis", "geographic-information-systems",
    "real-estate-analytics", "market-analysis", "property-valuation",
    "mortgage-tech", "loan-origination", "title-management",
    
    # ========== METHODOLOGIES & FRAMEWORKS ==========
    "agile", "scrum", "kanban", "lean", "devops", "devsecops",
    "dataops", "mlops", "aiops", "gitops", "waterfall",
    "saFe", "scaled-agile", "less", "spotify-model",
    "design-thinking", "human-centered-design",
    "pmp", "prince2", "itil", "cobit", "togaf",
    "six-sigma", "dmaic", "dmadv", "kaizen", "tqm",
    
    # ========== SOFT SKILLS ==========
    "communication", "verbal-communication", "written-communication",
    "presentation-skills", "public-speaking", "active-listening",
    "leadership", "team-leadership", "people-management",
    "teamwork", "collaboration", "cross-functional-collaboration",
    "problem-solving", "critical-thinking", "analytical-thinking",
    "creativity", "innovation", "design-thinking",
    "adaptability", "flexibility", "resilience",
    "time-management", "prioritization", "multitasking",
    "project-management", "stakeholder-management", "risk-management",
    "conflict-resolution", "negotiation", "influence",
    "emotional-intelligence", "empathy", "self-awareness",
    "mentoring", "coaching", "knowledge-sharing",
    
    # ========== LANGUAGES ==========
    "english", "spanish", "mandarin", "hindi", "french",
    "german", "japanese", "arabic", "portuguese", "russian",
    "bengali", "korean", "italian", "dutch", "turkish",
    "vietnamese", "thai", "persian", "polish", "ukrainian",
    
    # ========== PRODUCT MANAGEMENT ==========
    "product-management", "product-strategy", "product-roadmapping",
    "user-research", "user-interviews", "surveys", "usability-testing",
    "market-research", "competitive-analysis", "swot-analysis",
    "product-metrics", "kpis", "okrs", "north-star-metric",
    "a-b-testing", "multivariate-testing", "feature-flagging",
    "user-stories", "user-personas", "journey-mapping",
    "prioritization", "rice", "moSCoW", "value-effort-matrix",
    "go-to-market", "product-launch", "product-marketing",
    
    # ========== UX/UI DESIGN ==========
    "ux-design", "user-experience", "ui-design", "user-interface",
    "user-research", "usability-testing", "user-testing",
    "wireframing", "prototyping", "mockups", "information-architecture",
    "interaction-design", "visual-design", "design-systems",
    "accessibility", "wcag", "inclusive-design", "figma",
    "sketch", "adobe-xd", "invision", "framer", "principle",
    "zeplin", "abstract", "protopie", "axure",
    
    # ========== QA & TESTING ==========
    "quality-assurance", "software-testing", "test-planning",
    "test-strategy", "test-cases", "test-scenarios",
    "test-automation", "performance-testing", "load-testing",
    "stress-testing", "security-testing", "penetration-testing",
    "api-testing", "mobile-testing", "web-testing",
    "exploratory-testing", "regression-testing", "smoke-testing",
    "bdd", "behavior-driven-development", "cucumber",
    "test-management", "jira", "testrail", "qtest",
    "defect-tracking", "bug-tracking", "root-cause-analysis",
    
    # ========== TECHNICAL WRITING ==========
    "technical-writing", "documentation", "api-documentation",
    "user-guides", "technical-guides", "knowledge-bases",
    "markdown", "asciidoc", "rst", "docusaurus", "gitbook",
    "readme", "wiki", "confluence", "notion",
    
    # ========== HARDWARE & NETWORKING ==========
    "networking", "ccna", "ccnp", "juniper", "cisco",
    "tcp-ip", "dns", "dhcp", "http", "https", "ftp",
    "routing", "switching", "vlan", "vpn", "firewall",
    "wireless", "wifi", "bluetooth", "network-security",
    "server-administration", "windows-server", "linux-server",
    "active-directory", "ldap", "dns-management",
    "virtualization", "vmware", "hyper-v", "kvm", "xen",
    "storage", "san", "nas", "raid", "backup-solutions",
    
    # ========== AEROSPACE & DEFENSE ==========
    "aerospace", "defense", "do-178c", "do-254",
    "missile-guidance", "radar-systems", "satellite-systems",
    "avionics", "flight-control", "simulation",
    "systems-engineering", "model-based-systems-engineering",
    
    # ========== AUTOMOTIVE ==========
    "automotive", "adas", "autonomous-vehicles",
    "can-bus", "lin-bus", "flexray", "automotive-spice",
    "ecu", "embedded-automotive", "vehicle-dynamics",
    
    # ========== ENERGY & UTILITIES ==========
    "energy", "utilities", "scada-energy", "smart-grid",
    "renewable-energy", "solar", "wind", "energy-trading",
    
    # ========== PHARMACEUTICAL & LIFE SCIENCES ==========
    "pharma", "life-sciences", "gxp", "gmp", "glp",
    "clinical-trials", "clinical-data-management",
    "lims", "laboratory-information-management-system",
    "bioinformatics", "computational-biology",
    
    # ========== CONSTRUCTION TECH ==========
    "construction-tech", "bim", "building-information-modeling",
    "cad", "autocad", "revit", "construction-management",
    "project-management-construction",
    
    # ========== TRAVEL & HOSPITALITY ==========
    "travel-tech", "hospitality", "gds", "global-distribution-system",
    "crs", "central-reservation-system", "hotel-management",
    "revenue-management", "yield-management",
    
    # ========== INSURANCE TECH ==========
    "insurtech", "insurance", "policy-administration",
    "claims-processing", "underwriting", "actuarial-science",
    
    # ========== TELECOMMUNICATIONS ==========
    "telecom", "5g", "4g-lte", "voip", "sip", "telephony",
    "network-function-virtualization", "software-defined-networking",
    
    # ========== GOVERNMENT & PUBLIC SECTOR ==========
    "government", "public-sector", "digital-government",
    "e-governance", "citizen-services", "public-policy",
}

# backward-compatible alias
skills = SKILLS