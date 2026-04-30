$templatesDir = "c:\Users\Admin\vjs-website-\templates"
$files = Get-ChildItem -Path $templatesDir -Filter "*.html"

# New 3x2 Grid Structure (Directly into mega-menu-content)
$newMenuContent = @'
												<div class="mega-menu-content mega-3-col">
													<!-- Row 1 Headings -->
													<div class="mega-section">
														<span class="mega-title">IT Infrastructure</span>
														<ul class="mega-list">
															<li><a href="{{ url_for(''catch_all'', filename=''it-consulting.html'') }}">IT Consulting</a></li>
															<li><a href="{{ url_for(''catch_all'', filename=''data-centers-hosting.html'') }}?v=1.0">Enterprise Data Centers & Hosting Services</a></li>
														</ul>
													</div>
													<div class="mega-section">
														<span class="mega-title">Education & Skills</span>
														<ul class="mega-list">
															<li><a href="{{ url_for(''catch_all'', filename=''it-training.html'') }}">IT Training</a></li>
															<li><a href="{{ url_for(''catch_all'', filename=''yoga-wellness.html'') }}?v=1.0">Yoga & Wellness</a></li>
														</ul>
													</div>
													<div class="mega-section">
														<span class="mega-title">Energy & Sustainability</span>
														<ul class="mega-list">
															<li><a href="{{ url_for(''catch_all'', filename=''green-energy.html'') }}?v=1.0">Green Energy & Solar Manufacturing</a></li>
														</ul>
													</div>

													<!-- Row 2 Headings (Perfectly Aligned) -->
													<div class="mega-section">
														<span class="mega-title">Agri & Trade</span>
														<ul class="mega-list">
															<li><a href="{{ url_for(''catch_all'', filename=''export-import.html'') }}">Export & Import</a></li>
															<li><a href="{{ url_for(''catch_all'', filename=''plantations.html'') }}">Plantations & Exotic Trees</a></li>
														</ul>
													</div>
													<div class="mega-section">
														<span class="mega-title">Real Estate</span>
														<ul class="mega-list">
															<li><a href="{{ url_for(''catch_all'', filename=''property-services.html'') }}">Property Services</a></li>
														</ul>
													</div>
													<div class="mega-section">
														<span class="mega-title">Logistics & Travel</span>
														<ul class="mega-list">
															<li><a href="{{ url_for(''catch_all'', filename=''logistics-services.html'') }}">Logistics Services</a></li>
															<li><a href="{{ url_for(''catch_all'', filename=''travel-rentals.html'') }}">Travel & Rentals</a></li>
														</ul>
													</div>
												</div>
'@

foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName)
    
    # Target the entire biz-dropdown container
    $regex = '(?s)<ul class="dropdown-menu biz-dropdown">.*?</ul>'
    
    if ($content -match $regex) {
        $newFullMenu = "<ul class=`"dropdown-menu biz-dropdown`">`n											<li>`n$newMenuContent`n											</li>`n										</ul>"
        $content = $content -replace $regex, $newFullMenu
        
        # Ensure url_for single quotes are correct (fix previous mistake if it exists)
        $content = $content.Replace("''", "'")
        
        [System.IO.File]::WriteAllText($file.FullName, $content, (New-Object System.Text.UTF8Encoding($false)))
    }
}

Write-Host "All Businesses menus updated to a perfectly aligned 3x2 grid structure."
