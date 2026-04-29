$template = Get-Content "c:\Users\Admin\vjs-website-\sustainability_page_template_v2.html" -Raw
$mainPage = Get-Content "c:\Users\Admin\vjs-website-\public\sustainability.html" -Raw

$headerRegex = '(?si)<header.*?</header>'
$headerMatch = [regex]::Match($mainPage, $headerRegex)
$header = $headerMatch.Value

$footerRegex = '(?si)<footer.*?</footer>'
$footerMatch = [regex]::Match($mainPage, $footerRegex)
$footer = $footerMatch.Value

$pages = @(
    # TECHNOLOGY & INFRASTRUCTURE
    @{
        File = "digital-transformation-sustainability.html"
        Title = "Digital Transformation & IT Consulting"
        Subtitle = "Building modern, efficient, and sustainable digital ecosystems through Springreen."
        Category = "Core Services"
        Overview = "Springreen drives digital transformation by enabling organizations to shift from traditional systems to modern, efficient, and sustainable digital ecosystems. By leveraging intelligent automation and scalable technologies, we reduce physical resource usage and enhance operational performance across industries. Our focus is on creating a 'Zero-Waste' digital culture."
        StrategicPositioning = "End-to-end digital transformation + infrastructure ownership = control over client lifecycle (build â†’ host â†’ scale). We don't just build software; we build sustainable digital assets."
        Offers = @(
            "Web, mobile, and enterprise application development",
            "AI/ML-powered intelligent systems",
            "Automation solutions including RPA",
            "CRM platforms and advanced data analytics",
            "Cloud-native application re-engineering",
            "Digital workflow optimization"
        )
        ApproachDesc = "Our approach focuses on 'Efficiency by Design'. We build digital-first ecosystems that eliminate manual inefficiencies and reduce dependency on physical resources through automation and scalable architectures."
        Impacts = @(
            "Paperless workflows reducing physical waste significantly",
            "Automation solutions minimizing operational inefficiencies",
            "Energy-efficient system architectures tailored for scale",
            "Reduced carbon footprint through optimized digital operations",
            "Long-term digital sustainability via modular code"
        )
        Stats = @(
            @{ Num = "85%"; Label = "Waste Reduction" }
            @{ Num = "40k+"; Label = "Hours Automated" }
            @{ Num = "120+"; Label = "Eco-Systems Built" }
        )
        FAQs = @(
            @{ Q = "How does digital transformation reduce physical waste?"; A = "By digitizing manual workflows, we eliminate the need for paper, physical storage, and transportation of documents. Automation further reduces the resource footprint of repetitive tasks." }
            @{ Q = "What are energy-efficient architectures?"; A = "These are software designs optimized to run with minimal CPU and memory usage, directly reducing the power consumption of data centers and end-user devices." }
            @{ Q = "Is sustainable IT more expensive?"; A = "Initially, optimization requires investment, but long-term savings in energy, hardware maintenance, and operational efficiency lead to a significantly lower Total Cost of Ownership (TCO)." }
        )
        Commitment = "We are committed to enabling sustainable digital transformation that balances innovation, efficiency, and environmental responsibility."
        Icon = "bi-cpu"
    },
    @{
        File = "cloud-infrastructure-sustainability.html"
        Title = "Cloud, Hosting & Infrastructure"
        Subtitle = "Scalable infrastructure designed to optimize performance and energy usage."
        Category = "Core Services"
        Overview = "Aditya Solutions provides the digital backbone for the group and its clients. We deliver scalable cloud and infrastructure services designed to optimize performance while minimizing environmental impact through efficient resource allocation."
        StrategicPositioning = "Ownership of the infrastructure layer is critical for scale. We control the build, host, and scale phases, ensuring high-performance with minimal footprint."
        Offers = @(
            "Managed hosting and domain services",
            "Scalable cloud deployments",
            "Infrastructure optimization and security",
            "Enterprise Data Center solutions",
            "Green hosting initiatives",
            "Hybrid cloud management"
        )
        ApproachDesc = "We focus on infrastructure ownership and optimization. By designing centralized systems, we reduce redundancy and improve resource efficiency, leading to lower energy consumption."
        Impacts = @(
            "Optimized server usage leading to lower energy consumption",
            "Efficient resource allocation reducing overall carbon footprint",
            "Reduced hardware dependency through cloud-based architectures",
            "High uptime coupled with sustainable power management",
            "Scalable resources that match demand without waste"
        )
        Stats = @(
            @{ Num = "30%"; Label = "Energy Saved" }
            @{ Num = "99.9%"; Label = "Uptime Efficiency" }
            @{ Num = "500+"; Label = "Servers Optimized" }
        )
        FAQs = @(
            @{ Q = "What is green hosting?"; A = "It involves using energy-efficient hardware and data centers powered by renewable energy sources, significantly reducing the carbon footprint of digital operations." }
            @{ Q = "How do you optimize server usage?"; A = "Through virtualization and containerization, we ensure that every server runs at optimal capacity, preventing idle power consumption." }
            @{ Q = "Is cloud more sustainable than on-premise?"; A = "Generally, yes. Cloud providers can achieve higher economies of scale and better resource utilization than individual on-premise setups." }
        )
        Commitment = "We deliver infrastructure solutions that support both business growth and environmental sustainability at every layer."
        Icon = "bi-cloud-check"
    },

    # ENERGY & SUSTAINABILITY
    @{
        File = "renewable-energy-solutions.html"
        Title = "Renewable Energy Solutions"
        Subtitle = "Accelerating the transition to clean energy through Aditya Powers."
        Category = "Core Services"
        Overview = "Aditya Powers focuses on delivering renewable energy solutions that support sustainable development. We are a government-aligned sector focusing on high-impact energy transition projects."
        StrategicPositioning = "Aligns with global ESG trends, unlocking subsidies and global partnerships while positioning the group as future-ready in the energy sector."
        Offers = @(
            "Solar energy deployment and manufacturing",
            "Rural electrification and micro-grid projects",
            "Sustainable energy consultancy",
            "Clean energy infrastructure development",
            "Energy storage solutions",
            "Smart grid integration"
        )
        ApproachDesc = "We promote clean energy adoption by expanding access to sustainable energy systems, particularly in underserved rural areas and panchayats."
        Impacts = @(
            "Reduced dependency on traditional fossil fuels",
            "Increased clean energy usage across rural communities",
            "Lower environmental pollution through renewable adoption",
            "Support for decentralized and resilient power systems",
            "Empowerment of rural economies through reliable energy"
        )
        Stats = @(
            @{ Num = "250+"; Label = "Homes Electrified" }
            @{ Num = "1.2MW"; Label = "Solar Capacity" }
            @{ Num = "15+"; Label = "Rural Projects" }
        )
        FAQs = @(
            @{ Q = "What is rural electrification?"; A = "It is the process of bringing electrical power to rural and remote areas, often using localized renewable sources like solar micro-grids." }
            @{ Q = "Why focus on solar?"; A = "Solar is highly scalable, requires low maintenance, and is abundant in our operational regions, making it the most viable renewable source." }
            @{ Q = "Do you manufacture solar panels?"; A = "Yes, through our manufacturing arm, we produce high-efficiency solar components tailored for various environmental conditions." }
        )
        Commitment = "We are dedicated to building a cleaner energy future and contributing to long-term environmental sustainability."
        Icon = "bi-sun"
    },

    # LOGISTICS & TRADE
    @{
        File = "logistics-trade-sustainability.html"
        Title = "Logistics & Trade Enablement"
        Subtitle = "Optimized and sustainable logistics for a greener supply chain."
        Category = "Core Services"
        Overview = "NVRS Logistics enhances supply chain efficiency through optimized and sustainable logistics solutions. We integrate trade and supply chain movement to reduce environmental impact."
        StrategicPositioning = "Vertical integration across trade, tourism, and supply chain. Diversifies revenue into real assets and global trade, hedging against tech volatility."
        Offers = @(
            "Transportation and supply chain management",
            "Export-import of agricultural goods (B2B & D2C)",
            "Route optimization and logistics analytics",
            "Cold chain management for fresh produce",
            "Last-mile delivery optimization",
            "Eco-friendly packaging solutions"
        )
        ApproachDesc = "We use smart logistics planning and route optimization to improve efficiency and reduce environmental impact while ensuring the freshest produce reaches global markets."
        Impacts = @(
            "Improved fuel efficiency through advanced route optimization",
            "Reduction in supply chain wastage for agricultural products",
            "Promotion of fresh, natural, and locally sourced produce",
            "Lower carbon emissions per ton of goods moved",
            "Strengthened local farmer ecosystems through direct trade"
        )
        Stats = @(
            @{ Num = "20%"; Label = "Fuel Efficiency" }
            @{ Num = "1k+ Tons"; Label = "Produce Moved" }
            @{ Num = "50+"; Label = "Partner Farmers" }
        )
        FAQs = @(
            @{ Q = "How does route optimization help?"; A = "By using data analytics to find the shortest and most efficient paths, we reduce fuel consumption and emissions significantly." }
            @{ Q = "What is Cold Chain management?"; A = "It is a temperature-controlled supply chain that ensures fresh produce stays high-quality from the farm to the consumer, reducing food waste." }
            @{ Q = "Do you work with small farmers?"; A = "Yes, we partner with local farmers to bring their natural produce to global markets through our export-import channels." }
        )
        Commitment = "We strive to create logistics systems that are efficient, sustainable, and environmentally responsible."
        Icon = "bi-truck"
    },

    # EDUCATION & TALENT
    @{
        File = "education-skill-sustainability.html"
        Title = "Education & Skill Development"
        Subtitle = "Empowering individuals for the digital economy through Aditya Institute."
        Category = "Core Services"
        Overview = "Aditya Institute empowers individuals through education and skill development. We create a talent pipeline that reduces hiring dependency and builds workforce control."
        StrategicPositioning = "Creates in-house talent supply, reduces hiring costs, and builds a community-led brand moat through talent and human capital development."
        Offers = @(
            "IT skilling and digital literacy programs",
            "Career readiness and professional development",
            "Digital-first learning pathways",
            "Industry-aligned technical training",
            "Corporate leadership workshops",
            "Grassroots educational support"
        )
        ApproachDesc = "We promote digital learning platforms that reduce physical resource usage while providing industry-relevant skills for long-term employability."
        Impacts = @(
            "Digital-first learning reducing physical resource usage",
            "Long-term social sustainability via improved employability",
            "Creation of a skilled workforce for the digital economy",
            "Grassroots talent development for sustainable growth",
            "Lower hiring costs through in-house talent supply"
        )
        Stats = @(
            @{ Num = "1200+"; Label = "Students Trained" }
            @{ Num = "85%"; Label = "Placement Rate" }
            @{ Num = "30+"; Label = "Skill Programs" }
        )
        FAQs = @(
            @{ Q = "What are digital-first pathways?"; A = "These are learning models that prioritize online and interactive digital content, reducing the need for physical books and travel." }
            @{ Q = "How do you ensure employability?"; A = "By aligning our curriculum with the actual needs of our group companies and industry partners, ensuring students learn high-demand skills." }
            @{ Q = "Is there a scholarship program?"; A = "Yes, through our Lakshmi Trust Initiative, we provide scholarships to deserving students from underserved communities." }
        )
        Commitment = "We are committed to building a skilled and sustainable future through knowledge and talent empowerment."
        Icon = "bi-mortarboard"
    },

    # ENVIRONMENTAL INITIATIVES
    @{
        File = "tree-plantation-sustainability.html"
        Title = "Tree Plantation & Green Cover"
        Subtitle = "Expanding natural assets through Lakshmi Gardens."
        Category = "Environmental Initiatives"
        Overview = "Our environmental initiatives focus on preserving natural resources and expanding green cover. Lakshmi Gardens leads our effort in plantation and preservation of exotic trees."
        StrategicPositioning = "Diversifies revenue into real assets and asset-backed stability. Aligns the group with global environmental preservation standards."
        Offers = @(
            "Tree plantation and green cover expansion",
            "Preservation of exotic and native tree species",
            "Sustainable plantation management",
            "Biodiversity enhancement programs",
            "Community plantation drives",
            "Natural asset preservation"
        )
        ApproachDesc = "We integrate environmental sustainability into our asset holdings, focusing on long-term appreciation and ecological balance."
        Impacts = @(
            "Increased green cover and local biodiversity enhancement",
            "Carbon sequestration through large-scale plantations",
            "Promotion of sustainable land use and natural assets",
            "Restoration of local ecosystems through native species",
            "Improved local climate resilience through green buffers"
        )
        Stats = @(
            @{ Num = "5000+"; Label = "Trees Planted" }
            @{ Num = "50+ Acres"; Label = "Green Cover" }
            @{ Num = "12"; Label = "Native Species" }
        )
        FAQs = @(
            @{ Q = "What trees do you plant?"; A = "We plant a mix of native species for biodiversity and exotic trees for specific natural asset goals, ensuring a balanced ecosystem." }
            @{ Q = "How do you ensure tree survival?"; A = "We use sustainable plantation management techniques, including drip irrigation and regular health monitoring by experts." }
            @{ Q = "Can the community participate?"; A = "Absolutely. We conduct regular community plantation drives to encourage local participation in environmental preservation." }
        )
        Commitment = "We are committed to protecting the environment and building a sustainability-driven natural ecosystem."
        Icon = "bi-tree"
    },
    @{
        File = "eco-tech-solutions.html"
        Title = "Eco-conscious Technology"
        Subtitle = "Reducing environmental footprint through smart tech."
        Category = "Environmental Initiatives"
        Overview = "We promote eco-conscious technology solutions across our client base, helping them adopt sustainable digital practices that reduce their environmental footprint."
        StrategicPositioning = "Transitioning from a technology-driven company to a sustainability-driven ecosystem through IP-led product innovation."
        Offers = @(
            "Green IT consultancy and audits",
            "Implementation of energy-efficient software",
            "Digital waste reduction strategies",
            "Eco-friendly technical architecture design",
            "Sustainable data management",
            "Renewable-powered IT infra"
        )
        ApproachDesc = "We focus on building software and systems that require less energy and fewer hardware resources to operate effectively."
        Impacts = @(
            "Reduced energy requirements for enterprise systems",
            "Minimized electronic waste through software longevity",
            "Lower carbon footprint for digital-first businesses",
            "Adoption of sustainable engineering practices",
            "High efficiency with minimal resource consumption"
        )
        Stats = @(
            @{ Num = "45%"; Label = "Efficiency Gain" }
            @{ Num = "25+"; Label = "Eco-Audits Done" }
            @{ Num = "15k"; Label = "CO2 Tons Saved" }
        )
        FAQs = @(
            @{ Q = "What is an eco-audit?"; A = "It is a comprehensive review of a company's IT infrastructure to identify energy wastage and propose sustainable alternatives." }
            @{ Q = "How can software be energy-efficient?"; A = "By optimizing algorithms to use fewer CPU cycles and better memory management, software consumes less power." }
            @{ Q = "What is digital waste?"; A = "It refers to unnecessary data storage, inefficient code, and redundant digital processes that consume energy without providing value." }
        )
        Commitment = "Our commitment is to lead the tech industry toward a more sustainable and eco-conscious future."
        Icon = "bi-laptop"
    },
    @{
        File = "renewable-energy-adoption.html"
        Title = "Renewable Energy Adoption"
        Subtitle = "Leading by example in energy transition."
        Category = "Environmental Initiatives"
        Overview = "We actively adopt renewable energy systems across all group operations, reducing our reliance on traditional power and lowering our collective footprint."
        StrategicPositioning = "Aligns the entire group with ESG targets and future-proofs our infrastructure against energy volatility."
        Offers = @(
            "Internal solar grid implementation",
            "Energy transition strategy for all verticals",
            "Monitoring and optimization of power usage",
            "Investment in clean energy technologies",
            "Electric vehicle charging infra",
            "Smart energy monitoring"
        )
        ApproachDesc = "We lead by example, transforming our offices, data centers, and farms into renewable-powered hubs."
        Impacts = @(
            "Significantly lower reliance on fossil fuel energy",
            "Direct reduction in operational greenhouse gas emissions",
            "Promotion of clean energy culture within the workforce",
            "Sustainable power management for critical infrastructure",
            "Resilient energy operations during grid outages"
        )
        Stats = @(
            @{ Num = "60%"; Label = "Solar Powered" }
            @{ Num = "40%"; Label = "Cost Reduction" }
            @{ Num = "10"; Label = "Net-Zero Hubs" }
        )
        FAQs = @(
            @{ Q = "How much of the group is solar-powered?"; A = "Currently, 60% of our operations are powered by solar, with a goal to reach 100% by 2030." }
            @{ Q = "Do you sell excess energy?"; A = "Our primary focus is internal sustainability, but we explore net-metering options to support the local grid." }
            @{ Q = "What are Net-Zero Hubs?"; A = "These are facilities that produce as much renewable energy as they consume over the course of a year." }
        )
        Commitment = "We are dedicated to achieving 100% renewable energy adoption across our group operations by 2030."
        Icon = "bi-lightning-charge"
    },
    @{
        File = "sustainable-business-practices.html"
        Title = "Sustainable Business Practices"
        Subtitle = "Operationalizing ethics and environmental responsibility."
        Category = "Environmental Initiatives"
        Overview = "We integrate sustainable business practices into every operational layer, from procurement to delivery, ensuring long-term ecological balance."
        StrategicPositioning = "Positions the group as a responsible corporate citizen, strengthening brand value and investor confidence."
        Offers = @(
            "Sustainable procurement and supply chain ethics",
            "Waste management and recycling programs",
            "Ethical business conduct and transparency",
            "Environmental compliance and reporting",
            "Green office policies",
            "Sustainability training for staff"
        )
        ApproachDesc = "We establish rigorous standards for sustainability that apply to our employees, partners, and vendors alike."
        Impacts = @(
            "Minimized operational waste and increased recycling",
            "Strengthened ethical culture across the organization",
            "Reduced environmental impact through smart procurement",
            "Enhanced transparency and corporate governance",
            "Long-term stability through ethical operations"
        )
        Stats = @(
            @{ Num = "100%"; Label = "Compliance" }
            @{ Num = "0"; Label = "Ethical Breaches" }
            @{ Num = "75%"; Label = "Sourcing Local" }
        )
        FAQs = @(
            @{ Q = "What is sustainable procurement?"; A = "It involves choosing vendors and partners who follow ethical and environmentally friendly practices in their own operations." }
            @{ Q = "How do you manage waste?"; A = "We have strict recycling and waste segregation policies in all offices, aimed at achieving zero-waste-to-landfill." }
            @{ Q = "Is sustainability part of staff training?"; A = "Yes, every employee undergoes sustainability awareness training to ensure they understand their role in our collective goals." }
        )
        Commitment = "Sustainability is not just a policy for us; it is the foundation of how we do business every day."
        Icon = "bi-shield-check"
    },

    # SOCIAL RESPONSIBILITY
    @{
        File = "educational-support-csr.html"
        Title = "Educational Support"
        Subtitle = "Lakshmi Trust Initiative: Uplifting students through education."
        Category = "Social Responsibility Initiatives"
        Overview = "The Lakshmi Trust Initiative, powered by Springreen's CSR efforts, provides educational support for students from underserved communities to drive community upliftment."
        StrategicPositioning = "Building future-ready talent at the grassroots level. Investing in human capital and long-term social sustainability."
        Offers = @(
            "Assistance for students from underserved communities",
            "Learning resources and basic digital exposure",
            "Skill awareness and career guidance initiatives",
            "Scholarships for higher technical education",
            "Local school infrastructure support",
            "Digital literacy workshops"
        )
        ApproachDesc = "We identify deserving students and provide them with the resources they need to succeed in a digital-first world."
        Impacts = @(
            "Improved access to quality education for the underprivileged",
            "Enhanced digital literacy among rural youth",
            "Reduced dropout rates through financial and material aid",
            "Stronger social foundation for community growth",
            "Empowerment of future leaders from rural areas"
        )
        Stats = @(
            @{ Num = "250+"; Label = "Students Helped" }
            @{ Num = "15"; Label = "Schools Partnered" }
            @{ Num = "5"; Label = "Scholarships" }
        )
        FAQs = @(
            @{ Q = "How are students selected?"; A = "Selection is based on financial need, academic potential, and community recommendations through our local outreach teams." }
            @{ Q = "What kind of resources do you provide?"; A = "We provide everything from school uniforms and books to tablets and internet access for digital learning." }
            @{ Q = "Is there long-term support?"; A = "Yes, we often support students throughout their primary and secondary education, and sometimes into technical training." }
        )
        Commitment = "We are dedicated to uplifting communities and promoting inclusive growth through the power of education."
        Icon = "bi-book"
    },
    @{
        File = "financial-material-aid.html"
        Title = "Financial & Material Aid"
        Subtitle = "Providing resilience through support in critical times."
        Category = "Social Responsibility Initiatives"
        Overview = "Through the Lakshmi Trust Initiative, we provide financial and material assistance during critical needs and emergencies to strengthen community resilience."
        StrategicPositioning = "Strengthening community resilience and building a supportive social moat for the group's operations."
        Offers = @(
            "Emergency financial assistance for families",
            "Material aid including food and essential supplies",
            "Support for rural healthcare and wellness",
            "Crisis management and community relief",
            "Rural medical camp support",
            "Essential sanitation kits"
        )
        ApproachDesc = "We respond swiftly to critical community needs, ensuring that basic requirements are met during challenging times."
        Impacts = @(
            "Immediate relief for families in critical situations",
            "Enhanced community trust and social stability",
            "Reduction in hardship for semi-urban and rural populations",
            "Stronger social support systems at the grassroots level",
            "Quick recovery for local economies after crisis"
        )
        Stats = @(
            @{ Num = "100+"; Label = "Families Aided" }
            @{ Num = "20"; Label = "Relief Drives" }
            @{ Num = "10"; Label = "Districts Covered" }
        )
        FAQs = @(
            @{ Q = "How do you identify families in need?"; A = "We work with local community leaders and volunteers who help us identify the most vulnerable families during emergencies." }
            @{ Q = "What does material aid include?"; A = "It typically includes food rations, clean water, medical supplies, and basic household items needed for survival." }
            @{ Q = "Do you provide medical support?"; A = "Yes, we often partner with local clinics to provide financial aid for medical emergencies and conduct rural health camps." }
        )
        Commitment = "Our commitment is to be a reliable pillar of support for our communities whenever they need us most."
        Icon = "bi-cash-coin"
    },
    @{
        File = "skill-building-youth.html"
        Title = "Youth Skill-Building"
        Subtitle = "Preparing the next generation for long-term employability."
        Category = "Social Responsibility Initiatives"
        Overview = "We focus on youth skill-building programs through our CSR initiatives, ensuring that the next generation is equipped for economic independence."
        StrategicPositioning = "Reduces hiring dependency for the group while building a community-led brand moat through workforce control."
        Offers = @(
            "Technical skill development workshops",
            "Soft skills and career readiness training",
            "Digital literacy for semi-urban populations",
            "Mentorship programs with group leaders",
            "Vocational training partnerships",
            "Internship opportunities"
        )
        ApproachDesc = "We bridge the gap between education and employment by providing industry-relevant skills and practical training."
        Impacts = @(
            "Improved employability for local and rural youth",
            "Creation of economic opportunities within communities",
            "Enhanced career confidence and professional growth",
            "Development of a future-ready workforce pipeline",
            "Reduction in youth unemployment in our operational regions"
        )
        Stats = @(
            @{ Num = "500+"; Label = "Youth Trained" }
            @{ Num = "70%"; Label = "Placement Success" }
            @{ Num = "12"; Label = "Training Hubs" }
        )
        FAQs = @(
            @{ Q = "What skills do you focus on?"; A = "We focus on a mix of technical skills (IT, logistics, energy) and soft skills like communication, teamwork, and problem-solving." }
            @{ Q = "Is there a cost for the training?"; A = "No, most of our CSR-led skill-building programs are provided free of cost to eligible youth." }
            @{ Q = "Who are the mentors?"; A = "Mentors are experienced professionals and leaders from across the Vijayalakshmi Group of Companies." }
        )
        Commitment = "We are committed to empowering the youth with the skills they need to build a sustainable future for themselves."
        Icon = "bi-tools"
    },

    # COMMUNITY DEVELOPMENT
    @{
        File = "rural-semi-urban-engagement.html"
        Title = "Rural & Semi-Urban Engagement"
        Subtitle = "Strengthening grassroots ecosystems for long-term growth."
        Category = "Community Development Programs"
        Overview = "Our community development programs focus on rural and semi-urban engagement, driving sustainable growth at the grassroots level."
        StrategicPositioning = "Creates a self-sustaining ecosystem with cross-leverage across industries and deep community roots."
        Offers = @(
            "Rural and semi-urban engagement initiatives",
            "Awareness programs for health and environment",
            "Local infrastructure and support activities",
            "Stakeholder engagement with community leaders",
            "Self-help group support",
            "Local festival and cultural support"
        )
        ApproachDesc = "We engage directly with communities to identify their unique challenges and collaborate on solutions that drive long-term prosperity."
        Impacts = @(
            "Improved living conditions in semi-urban and rural areas",
            "Increased awareness of health, environment, and tech",
            "Stronger local ecosystems supporting sustainable growth",
            "Enhanced community participation in development",
            "Better social cohesion and community resilience"
        )
        Stats = @(
            @{ Num = "30+"; Label = "Villages Reached" }
            @{ Num = "15"; Label = "Infra Projects" }
            @{ Num = "10k+"; Label = "Lives Impacted" }
        )
        FAQs = @(
            @{ Q = "How do you engage with local communities?"; A = "We conduct regular town-hall style meetings and work closely with panchayats and local leaders to understand their needs." }
            @{ Q = "What kind of local infrastructure do you support?"; A = "We support projects like community center renovations, local road repairs, and sanitation improvements." }
            @{ Q = "Do you support local culture?"; A = "Yes, we believe cultural heritage is a part of social sustainability and support local festivals and traditions." }
        )
        Commitment = "We are committed to empowering communities and building a sustainable future through collective growth."
        Icon = "bi-house-heart"
    },
    @{
        File = "awareness-programs-community.html"
        Title = "Community Awareness"
        Subtitle = "Knowledge sharing for a healthier and greener world."
        Category = "Community Development Programs"
        Overview = "We conduct awareness programs on digital literacy, environment, and health to empower community members with vital knowledge."
        StrategicPositioning = "Builds brand authority and community-led brand moat through education and transparency."
        Offers = @(
            "Digital literacy and safety workshops",
            "Environmental awareness and tree plantation drives",
            "Health and wellness awareness initiatives",
            "Sustainable living and resource management programs",
            "Government scheme awareness",
            "Social rights education"
        )
        ApproachDesc = "We believe that knowledge is the foundation of sustainability. We educate to empower community members to take control of their own future."
        Impacts = @(
            "Informed communities making better environmental choices",
            "Increased digital safety and literacy among rural users",
            "Better health outcomes through preventive awareness",
            "Broad adoption of sustainable practices at the household level",
            "Better access to government resources through awareness"
        )
        Stats = @(
            @{ Num = "50+"; Label = "Drives Conducted" }
            @{ Num = "5000+"; Label = "Awareness Packs" }
            @{ Num = "25"; Label = "Partner Orgs" }
        )
        FAQs = @(
            @{ Q = "What are digital safety workshops?"; A = "They educate community members on how to use the internet safely, avoiding scams and protecting their personal information." }
            @{ Q = "How do you conduct health drives?"; A = "We partner with medical professionals to provide information on nutrition, hygiene, and preventive care." }
            @{ Q = "Is the content available in local languages?"; A = "Yes, all our awareness materials are designed to be accessible and are often provided in local languages." }
        )
        Commitment = "Our commitment is to spread knowledge that drives meaningful and lasting change in the world."
        Icon = "bi-megaphone"
    },
    @{
        File = "local-infrastructure-support.html"
        Title = "Local Infrastructure Support"
        Subtitle = "Building the physical foundations of sustainable growth."
        Category = "Community Development Programs"
        Overview = "We support basic infrastructure needs in our communities, from local school repairs to digital hub setup, to enable development."
        StrategicPositioning = "Creates asset-backed valuation and supports other verticals like offices, farms, and data centers."
        Offers = @(
            "School and community center renovations",
            "Setup of rural digital learning hubs",
            "Basic infrastructure support (water, sanitation)",
            "Local transportation and mobility assistance",
            "Public lighting and safety improvements",
            "Common facility center support"
        )
        ApproachDesc = "We identify critical infrastructure gaps and provide the support needed to bridge them for community benefit."
        Impacts = @(
            "Improved physical environment for education and health",
            "Better access to digital resources through local hubs",
            "Enhanced quality of life through infrastructure support",
            "Foundational support for long-term economic growth",
            "Safer and more accessible community spaces"
        )
        Stats = @(
            @{ Num = "12"; Label = "Schools Refurbished" }
            @{ Num = "8"; Label = "Digital Hubs" }
            @{ Num = "5k"; Label = "Gallons/Day Water" }
        )
        FAQs = @(
            @{ Q = "How do you prioritize infrastructure projects?"; A = "Priority is given to projects that have the widest impact on the community, such as education and sanitation." }
            @{ Q = "What are digital learning hubs?"; A = "These are local spaces equipped with computers and internet, providing community members access to digital education and services." }
            @{ Q = "Do you maintain the infrastructure?"; A = "We often work with local committees to ensure there is a plan for long-term maintenance and upkeep of the facilities." }
        )
        Commitment = "We are committed to building the physical and digital infrastructure that communities need to thrive."
        Icon = "bi-bricks"
    }
)

# Icon Map for Offer Cards
$iconMap = @{
    "Web, mobile, and enterprise application development" = "bi-code-slash";
    "AI/ML-powered intelligent systems" = "bi-robot";
    "Automation solutions including RPA" = "bi-gear-wide-connected";
    "CRM platforms and advanced data analytics" = "bi-graph-up-arrow";
    "Cloud-native application re-engineering" = "bi-cloud-fill";
    "Digital workflow optimization" = "bi-diagram-3";
    "Managed hosting and domain services" = "bi-server";
    "Scalable cloud deployments" = "bi-cloud-arrow-up";
    "Infrastructure optimization and security" = "bi-shield-check";
    "Enterprise Data Center solutions" = "bi-database";
    "Green hosting initiatives" = "bi-tree-fill";
    "Hybrid cloud management" = "bi-share";
    "Solar energy deployment and manufacturing" = "bi-sun-fill";
    "Rural electrification and micro-grid projects" = "bi-plug-fill";
    "Sustainable energy consultancy" = "bi-lightbulb";
    "Clean energy infrastructure development" = "bi-lightning";
    "Energy storage solutions" = "bi-battery-charging";
    "Smart grid integration" = "bi-cpu";
    "Transportation and supply chain management" = "bi-box-seam";
    "Export-import of agricultural goods (B2B & D2C)" = "bi-globe";
    "Route optimization and logistics analytics" = "bi-map";
    "Cold chain management for fresh produce" = "bi-snow";
    "Last-mile delivery optimization" = "bi-truck";
    "Eco-friendly packaging solutions" = "bi-recycle";
    "IT skilling and digital literacy programs" = "bi-person-gear";
    "Career readiness and professional development" = "bi-briefcase";
    "Digital-first learning pathways" = "bi-laptop";
    "Industry-aligned technical training" = "bi-mortarboard";
    "Corporate leadership workshops" = "bi-people-fill";
    "Grassroots educational support" = "bi-book";
    "Tree plantation and green cover expansion" = "bi-tree-fill";
    "Preservation of exotic and native tree species" = "bi-flower1";
    "Sustainable plantation management" = "bi-potted-plant";
    "Biodiversity enhancement programs" = "bi-butterfly";
    "Community plantation drives" = "bi-people";
    "Natural asset preservation" = "bi-shield-shaded";
    "Green IT consultancy and audits" = "bi-check2-circle";
    "Implementation of energy-efficient software" = "bi-file-code";
    "Digital waste reduction strategies" = "bi-trash";
    "Eco-friendly technical architecture design" = "bi-building";
    "Sustainable data management" = "bi-hdd-network";
    "Renewable-powered IT infra" = "bi-sun";
    "Internal solar grid implementation" = "bi-grid-3x3-gap";
    "Energy transition strategy for all verticals" = "bi-arrow-repeat";
    "Monitoring and optimization of power usage" = "bi-activity";
    "Investment in clean energy technologies" = "bi-cash";
    "Electric vehicle charging infra" = "bi-ev-station";
    "Smart energy monitoring" = "bi-speedometer";
    "Sustainable procurement and supply chain ethics" = "bi-truck";
    "Waste management and recycling programs" = "bi-recycle";
    "Ethical business conduct and transparency" = "bi-eye";
    "Environmental compliance and reporting" = "bi-file-text";
    "Green office policies" = "bi-house-heart";
    "Sustainability training for staff" = "bi-mortarboard";
    "Assistance for students from underserved communities" = "bi-person-heart";
    "Learning resources and basic digital exposure" = "bi-tablet";
    "Skill awareness and career guidance initiatives" = "bi-compass";
    "Scholarships for higher technical education" = "bi-award";
    "Local school infrastructure support" = "bi-building-fill-up";
    "Digital literacy workshops" = "bi-display";
    "Emergency financial assistance for families" = "bi-currency-dollar";
    "Material aid including food and essential supplies" = "bi-basket";
    "Support for rural healthcare and wellness" = "bi-heart-pulse";
    "Crisis management and community relief" = "bi-bandaid";
    "Rural medical camp support" = "bi-hospital";
    "Essential sanitation kits" = "bi-droplet-fill";
    "Technical skill development workshops" = "bi-tools";
    "Soft skills and career readiness training" = "bi-chat-dots";
    "Digital literacy for semi-urban populations" = "bi-display-fill";
    "Mentorship programs with group leaders" = "bi-people";
    "Vocational training partnerships" = "bi-buildings";
    "Internship opportunities" = "bi-person-workspace";
    "Rural and semi-urban engagement initiatives" = "bi-geo-alt";
    "Awareness programs for health and environment" = "bi-megaphone";
    "Local infrastructure and support activities" = "bi-wrench-adjustable";
    "Stakeholder engagement with community leaders" = "bi-person-badge";
    "Self-help group support" = "bi-people-fill";
    "Local festival and cultural support" = "bi-music-note-beamed";
    "Digital literacy and safety workshops" = "bi-shield-lock";
    "Environmental awareness and tree plantation drives" = "bi-tree-fill";
    "Health and wellness awareness initiatives" = "bi-heart";
    "Sustainable living and resource management programs" = "bi-house-check";
    "Government scheme awareness" = "bi-info-square";
    "Social rights education" = "bi-journal-text";
    "School and community center renovations" = "bi-building-add";
    "Setup of rural digital learning hubs" = "bi-pc-display";
    "Basic infrastructure support (water, sanitation)" = "bi-droplet";
    "Local transportation and mobility assistance" = "bi-car-front";
    "Public lighting and safety improvements" = "bi-lightbulb-fill";
    "Common facility center support" = "bi-houses"
}

foreach ($p in $pages) {
    $c = $template -replace '\{\{PAGE_TITLE\}\}', $p.Title
    $c = $c -replace '\{\{PAGE_SUBTITLE\}\}', $p.Subtitle
    $c = $c -replace '\{\{CATEGORY\}\}', $p.Category
    $c = $c -replace '\{\{OVERVIEW\}\}', $p.Overview
    $c = $c -replace '\{\{STRATEGIC_POSITIONING\}\}', $p.StrategicPositioning
    $c = $c -replace '\{\{APPROACH_DESC\}\}', $p.ApproachDesc
    $c = $c -replace '\{\{COMMITMENT\}\}', $p.Commitment
    $c = $c -replace '\{\{HEADER\}\}', $header
    $c = $c -replace '\{\{FOOTER\}\}', $footer
    
    # Generate Stat Boxes
    $statBoxes = ""
    foreach ($s in $p.Stats) {
        $statBoxes += @"
                    <div class="col-lg-3 col-6">
                        <div class="stat-box">
                            <span class="stat-num">$($s.Num)</span>
                            <span class="stat-label">$($s.Label)</span>
                        </div>
                    </div>
"@
    }
    $c = $c -replace '\{\{STATS_BOXES\}\}', $statBoxes

    # Generate Offer Cards
    $offerCards = ""
    foreach ($o in $p.Offers) {
        $icon = $iconMap[$o]
        if (-not $icon) { $icon = $p.Icon }
        $offerCards += @"
					<div class="col-lg-3 col-md-6" data-aos="fade-up">
						<div class="offer-card">
							<div class="icon-circle-lg"><i class="bi $icon"></i></div>
							<h4>$o</h4>
						</div>
					</div>
"@
    }
    $c = $c -replace '\{\{OFFER_CARDS\}\}', $offerCards
    
    # Generate Accordion Items
    $accordionItems = ""
    $faqCount = 0
    foreach ($f in $p.FAQs) {
        $faqCount++
        $itemId = "faq-$($faqCount)"
        $showClass = if ($faqCount -eq 1) { "show" } else { "" }
        $collapsedClass = if ($faqCount -eq 1) { "" } else { "collapsed" }
        
        $accordionItems += @"
                            <div class="accordion-item">
                                <h2 class="accordion-header">
                                    <button class="accordion-button $collapsedClass" type="button" data-bs-toggle="collapse" data-bs-target="#$itemId">
                                        $($f.Q)
                                    </button>
                                </h2>
                                <div id="$itemId" class="accordion-collapse collapse $showClass" data-bs-parent="#susAccordion">
                                    <div class="accordion-body">
                                        $($f.A)
                                    </div>
                                </div>
                            </div>
"@
    }
    $c = $c -replace '\{\{ACCORDION_ITEMS\}\}', $accordionItems

    # Generate Approach Items (First 4 offers)
    $approachItems = ""
    foreach ($o in $p.Offers | Select-Object -First 4) {
        $icon = $iconMap[$o]
        if (-not $icon) { $icon = $p.Icon }
        $approachItems += @"
							<div class="col-md-6">
								<div class="approach-card">
									<div class="icon-circle"><i class="bi $icon"></i></div>
									<p>$o</p>
								</div>
							</div>
"@
    }
    $c = $c -replace '\{\{APPROACH_ITEMS\}\}', $approachItems
    
    # Generate Impact List
    $impactList = ""
    foreach ($i in $p.Impacts) {
        $impactList += "<li><i class='bi bi-check-circle-fill'></i> $i</li>"
    }
    $c = $c -replace '\{\{IMPACT_LIST\}\}', $impactList
    
    [System.IO.File]::WriteAllText("c:\Users\Admin\vjs-website-\public\$($p.File)", $c, [System.Text.Encoding]::UTF8)
    Write-Host "Generated $($p.File)"
}
