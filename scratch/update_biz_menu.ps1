$templatesDir = "c:\Users\Admin\vjs-website-\templates"
$files = Get-ChildItem -Path $templatesDir -Filter "*.html"

$newMenuContent = @'
												<div class="mega-menu-content mega-3-col">
													<div class="mega-column">
														<div class="mega-section">
															<span class="mega-title">IT Infrastructure</span>
															<ul class="mega-list">
																<li><a href="{{ url_for(''catch_all'', filename=''it-consulting.html'') }}">IT Consulting</a></li>
																<li><a href="{{ url_for(''catch_all'', filename=''data-centers-hosting.html'') }}?v=1.0">Enterprise Data Centers & Hosting Services</a></li>
															</ul>
														</div>
														<div class="mega-section">
															<span class="mega-title">Agri & Trade</span>
															<ul class="mega-list">
																<li><a href="{{ url_for(''catch_all'', filename=''export-import.html'') }}">Export & Import</a></li>
																<li><a href="{{ url_for(''catch_all'', filename=''plantations.html'') }}">Plantations & Exotic Trees</a></li>
															</ul>
														</div>
													</div>
													<div class="mega-column">
														<div class="mega-section">
															<span class="mega-title">Education & Skills</span>
															<ul class="mega-list">
																<li><a href="{{ url_for(''catch_all'', filename=''it-training.html'') }}">IT Training</a></li>
																<li><a href="{{ url_for(''catch_all'', filename=''yoga-wellness.html'') }}?v=1.0">Yoga & Wellness</a></li>
															</ul>
														</div>
														<div class="mega-section">
															<span class="mega-title">Real Estate</span>
															<ul class="mega-list">
																<li><a href="{{ url_for(''catch_all'', filename=''property-services.html'') }}">Property Services</a></li>
															</ul>
														</div>
													</div>
													<div class="mega-column">
														<div class="mega-section">
															<span class="mega-title">Energy & Sustainability</span>
															<ul class="mega-list">
																<li><a href="{{ url_for(''catch_all'', filename=''green-energy.html'') }}?v=1.0">Green Energy & Solar Manufacturing</a></li>
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
												</div>
'@

# Note: We use a regex that looks for the biz-dropdown container and replaces its internal mega-6-col block.
# We use [regex]::Escape for parts and then flexible whitespace matches.
# But since the structure is very consistent, a simple replace on the block works well.

foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName)
    
    # Target the mega-6-col block specifically within the biz-dropdown area
    # This regex matches the entire div from mega-6-col to its closing div, 
    # but we need to be careful with nesting. Since our mega-menu-content has a known structure:
    
    $regex = '(?s)<ul class="dropdown-menu biz-dropdown">.*?<div class="mega-menu-content mega-6-col">.*?</div>\s*</li>\s*</ul>'
    
    if ($content -match $regex) {
        Write-Host "Updating $($file.Name)..."
        $newFullMenu = "<ul class=`"dropdown-menu biz-dropdown`">`n											<li>`n$newMenuContent`n											</li>`n										</ul>"
        $content = $content -replace $regex, $newFullMenu
        [System.IO.File]::WriteAllText($file.FullName, $content, (New-Object System.Text.UTF8Encoding($false)))
    }
}

Write-Host "All Businesses menus updated to 3x3 grid structure."
