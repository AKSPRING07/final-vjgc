$template = Get-Content "c:\Users\Admin\vjs-website-\sustainability_page_template.html" -Raw
$mainPage = Get-Content "c:\Users\Admin\vjs-website-\public\sustainability.html" -Raw

# Extract header and footer from sustainability.html
# Header is from <body> up to <!-- Hero Section -->
$headerRegex = '(?si)<header.*?</header>'
$headerMatch = [regex]::Match($mainPage, $headerRegex)
$header = $headerMatch.Value

# Footer is <footer ... </footer>
$footerRegex = '(?si)<footer.*?</footer>'
$footerMatch = [regex]::Match($mainPage, $footerRegex)
$footer = $footerMatch.Value

$pages = @(
    @{
        File = "digital-transformation-sustainability.html"
        Title = "Digital Transformation & IT Consulting"
        Desc = "Paperless workflows and energy-efficient system architectures."
        LongDesc = "Springreen focuses on digital transformation that reduces physical resource usage. By implementing paperless workflows and AI-driven automation, we significantly lower operational waste and energy consumption across enterprise application development."
        Category = "Core Services"
    },
    @{
        File = "cloud-infrastructure-sustainability.html"
        Title = "Cloud, Hosting & Infrastructure"
        Desc = "Optimized server usage and reduced carbon footprint."
        LongDesc = "Aditya Solutions provides managed hosting and cloud services designed for maximum efficiency. Our infrastructure optimization reduces the carbon footprint by ensuring efficient resource allocation and lower energy consumption in data center operations."
        Category = "Core Services"
    },
    @{
        File = "renewable-energy-solutions.html"
        Title = "Renewable Energy Solutions"
        Desc = "Solar energy deployment and rural electrification projects."
        LongDesc = "Aditya Powers is dedicated to the adoption of clean energy. Through wide-scale solar energy deployment and decentralized power systems, we support rural electrification and reduce global dependency on fossil fuels."
        Category = "Core Services"
    },
    @{
        File = "logistics-trade-sustainability.html"
        Title = "Logistics & Trade Enablement"
        Desc = "Route optimization and supply chain wastage reduction."
        LongDesc = "NVRS Logistics integrates sustainability into the supply chain. We use advanced route optimization to increase fuel efficiency and promote the trade of fresh, natural produce while minimizing wastage in global trade enablement."
        Category = "Core Services"
    },
    @{
        File = "education-skill-sustainability.html"
        Title = "Education & Skill Development"
        Desc = "Digital-first learning and social sustainability via employability."
        LongDesc = "Aditya Institute empowers the next generation with digital-first learning. By reducing physical resource usage and focusing on long-term employability, we create social sustainability and economic growth through skill development."
        Category = "Core Services"
    },
    @{
        File = "tree-plantation-sustainability.html"
        Title = "Tree Plantation & Green Cover"
        Desc = "Lakshmi Gardens initiative for green cover expansion."
        LongDesc = "Through Lakshmi Gardens, we lead massive tree plantation drives and green cover expansion projects. This environmental initiative is core to our commitment to ecosystem restoration and biodiversity support."
        Category = "Environmental Initiatives"
    },
    @{
        File = "eco-tech-solutions.html"
        Title = "Eco-conscious Technology Solutions"
        Desc = "Promoting technology that supports environmental health."
        LongDesc = "We advocate for and implement technology solutions that are fundamentally eco-conscious. From hardware choices to software efficiency, every solution is vetted for its environmental impact."
        Category = "Environmental Initiatives"
    },
    @{
        File = "renewable-energy-adoption.html"
        Title = "Renewable Energy Adoption"
        Desc = "Internal and external promotion of renewable systems."
        LongDesc = "Our commitment to renewable energy extends beyond our products. We actively adopt renewable systems in our own facilities and encourage our clients to transition to clean energy sources."
        Category = "Environmental Initiatives"
    },
    @{
        File = "sustainable-business-practices.html"
        Title = "Sustainable Business Practices"
        Desc = "Encouraging eco-friendly operations across our ecosystem."
        LongDesc = "We promote sustainable business practices across our entire network of clients and partners. This includes waste reduction, energy auditing, and sustainable procurement policies."
        Category = "Environmental Initiatives"
    },
    @{
        File = "educational-support-csr.html"
        Title = "Educational Support"
        Desc = "Lakshmi Trust Initiative for underprivileged students."
        LongDesc = "Social responsibility is at the heart of Lakshmi Trust. We provide comprehensive educational support, including scholarships and infrastructure, to underprivileged students to ensure equal opportunity for all."
        Category = "Social Responsibility Initiatives"
    },
    @{
        File = "financial-material-aid.html"
        Title = "Financial & Material Aid"
        Desc = "Support during critical situations and community needs."
        LongDesc = "We stand with communities during critical times. Our social responsibility programs include providing financial and material aid during emergencies, natural disasters, and to those in urgent need."
        Category = "Social Responsibility Initiatives"
    },
    @{
        File = "skill-building-youth.html"
        Title = "Skill-Building Programs"
        Desc = "Investing in human capital for social upliftment."
        LongDesc = "Our skill-building programs for youth are designed to bridge the gap between education and employability. We invest in human capital to drive social upliftment and long-term community impact."
        Category = "Social Responsibility Initiatives"
    },
    @{
        File = "rural-semi-urban-engagement.html"
        Title = "Rural & Semi-Urban Engagement"
        Desc = "Strengthening grassroots ecosystems for impact."
        LongDesc = "We engage deeply with rural and semi-urban communities to understand their needs. Our programs strengthen grassroots ecosystems through infrastructure support and direct community participation."
        Category = "Community Development Programs"
    },
    @{
        File = "awareness-programs-community.html"
        Title = "Awareness Programs"
        Desc = "Digital literacy, environment, and health awareness."
        LongDesc = "Education is the first step to change. We run extensive awareness programs covering digital literacy, environmental protection, and public health to empower community members with knowledge."
        Category = "Community Development Programs"
    },
    @{
        File = "local-infrastructure-support.html"
        Title = "Local Infrastructure Support"
        Desc = "Strengthening community facilities and support activities."
        LongDesc = "We contribute to the development of local infrastructure, including community centers, health facilities, and educational spaces, to ensure long-term stability and growth for the areas we serve."
        Category = "Community Development Programs"
    }
)

foreach ($p in $pages) {
    $c = $template -replace '\{\{PAGE_TITLE\}\}', $p.Title
    $c = $c -replace '\{\{PAGE_DESCRIPTION\}\}', $p.Desc
    $c = $c -replace '\{\{LONG_DESCRIPTION\}\}', $p.LongDesc
    $c = $c -replace '\{\{CATEGORY\}\}', $p.Category
    $c = $c -replace '\{\{HEADER\}\}', $header
    $c = $c -replace '\{\{FOOTER\}\}', $footer
    
    [System.IO.File]::WriteAllText("c:\Users\Admin\vjs-website-\public\$($p.File)", $c, [System.Text.Encoding]::UTF8)
    Write-Host "Generated $($p.File)"
}
