$sustainabilityMegaHtml = '									<li class="nav-item dropdown mega-dropdown">
										<a class="nav-link dropdown-toggle" href="sustainability.html" role="button"
											data-bs-toggle="dropdown" data-bs-auto-close="outside"
											aria-expanded="false">Sustainability
										</a>
										<ul class="dropdown-menu">
											<li>
												<div class="mega-menu-content mega-4-col">
													<div class="mega-column">
														<div class="mega-section">
															<span class="mega-title">Core Services</span>
															<ul class="mega-list">
																<li><a href="digital-transformation-sustainability.html">Digital Transformation & IT Consulting</a></li>
																<li><a href="cloud-infrastructure-sustainability.html">Cloud, Hosting & Infrastructure</a></li>
																<li><a href="renewable-energy-solutions.html">Renewable Energy Solutions</a></li>
																<li><a href="logistics-trade-sustainability.html">Logistics & Trade Enablement</a></li>
																<li><a href="education-skill-sustainability.html">Education & Skill Development</a></li>
															</ul>
														</div>
													</div>
													<div class="mega-column">
														<div class="mega-section">
															<span class="mega-title">Environmental Initiatives</span>
															<ul class="mega-list">
																<li><a href="tree-plantation-sustainability.html">Tree Plantation & Green Cover</a></li>
																<li><a href="eco-tech-solutions.html">Eco-conscious Technology Solutions</a></li>
																<li><a href="renewable-energy-adoption.html">Renewable Energy Adoption</a></li>
																<li><a href="sustainable-business-practices.html">Sustainable Business Practices</a></li>
															</ul>
														</div>
													</div>
													<div class="mega-column">
														<div class="mega-section">
															<span class="mega-title">Social Responsibility</span>
															<ul class="mega-list">
																<li><a href="educational-support-csr.html">Educational Support</a></li>
																<li><a href="financial-material-aid.html">Financial & Material Aid</a></li>
																<li><a href="skill-building-youth.html">Skill-Building Programs</a></li>
															</ul>
														</div>
													</div>
													<div class="mega-column">
														<div class="mega-section">
															<span class="mega-title">Community Development</span>
															<ul class="mega-list">
																<li><a href="rural-semi-urban-engagement.html">Rural & Semi-Urban Engagement</a></li>
																<li><a href="awareness-programs-community.html">Awareness Programs</a></li>
																<li><a href="local-infrastructure-support.html">Local Infrastructure Support</a></li>
															</ul>
														</div>
													</div>
												</div>
											</li>
										</ul>
									</li>'

# Use a more generic regex that captures the whole Sustainability dropdown block
$sustainabilityRegex = '(?si)<li class="nav-item dropdown mega-dropdown">\s*<a[^>]*sustainability\.html[^>]*>Sustainability</a>.*?<!--\s*/\.theme-main-menu\s*-->'
# Wait, this regex might be too broad if it captures until the end of the menu.
# Let's try to capture until the end of the dropdown-menu ul.
$sustainabilityRegex = '(?si)<li class="nav-item dropdown mega-dropdown">\s*<a[^>]*sustainability\.html[^>]*>Sustainability</a>.*?</ul>\s*</li>'

Write-Host "Starting update..."

Get-ChildItem -Path "c:\Users\Admin\vjs-website-\public\*.html" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    
    if ($content -match $sustainabilityRegex) {
        Write-Host "Found mega dropdown in $($_.Name)"
        $newContent = $content -replace $sustainabilityRegex, $sustainabilityMegaHtml
        [System.IO.File]::WriteAllText($_.FullName, $newContent, [System.Text.Encoding]::UTF8)
        Write-Host "Updated $($_.Name)"
    } elseif ($content -match 'href="sustainability\.html"') {
        Write-Host "Found simple link in $($_.Name)"
        $simpleRegex = '(?si)<li class="nav-item">\s*<a[^>]*sustainability\.html[^>]*>Sustainability</a>\s*</li>'
        $newContent = $content -replace $simpleRegex, $sustainabilityMegaHtml
        if ($newContent -ne $content) {
            [System.IO.File]::WriteAllText($_.FullName, $newContent, [System.Text.Encoding]::UTF8)
            Write-Host "Updated $($_.Name) (simple link)"
        } else {
            Write-Host "Could not match simple link pattern in $($_.Name)"
        }
    } else {
        Write-Host "No sustainability link found in $($_.Name)"
    }
}

# Update template
$templatePath = "c:\Users\Admin\vjs-website-\sustainability_page_template_v2.html"
if (Test-Path $templatePath) {
    $content = Get-Content $templatePath -Raw
    if ($content -match $sustainabilityRegex) {
        $newContent = $content -replace $sustainabilityRegex, $sustainabilityMegaHtml
        [System.IO.File]::WriteAllText($templatePath, $newContent, [System.Text.Encoding]::UTF8)
        Write-Host "Updated template"
    }
}
