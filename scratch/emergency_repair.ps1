$templatesDir = "c:\Users\Admin\vjs-website-\templates"
$files = Get-ChildItem -Path $templatesDir -Filter "*.html"

# Corrected 3x2 Grid Structure
$newMenuContent = @'
												<div class="mega-menu-content mega-3-col">
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

$replacement = @"
										<a class="nav-link dropdown-toggle" href="#" role="button"
											data-bs-toggle="dropdown" data-bs-auto-close="outside"
											aria-expanded="false">Businesses
										</a>
										<ul class="dropdown-menu biz-dropdown">
											<li>
$newMenuContent
											</li>
										</ul>
"@

foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName)
    
    # This regex is designed to catch the start of the Businesses menu and EVERYTHING 
    # up until the next main nav-item (Sustainability). This effectively wipes out the corruption.
    $regex = '(?s)<a[^>]*>Businesses\s*</a>.*?<li[^>]*dropdown[^>]*mega-dropdown[^>]*>\s*<a[^>]*>Sustainability'
    
    if ($content -match $regex) {
        Write-Host "Repairing $($file.Name)..."
        # We replace the whole block but keep the Sustainability start tag
        $newBlock = $replacement + "`n									<li class=`"nav-item dropdown mega-dropdown`">`n										<a class=`"nav-link dropdown-toggle`" href=`"javascript:void(0)`" role=`"button`"`n											data-bs-toggle=`"dropdown`" data-bs-auto-close=`"outside`"`n											aria-expanded=`"false`">Sustainability"
        
        $content = $content -replace $regex, $newBlock
        $content = $content.Replace("''", "'")
        [System.IO.File]::WriteAllText($file.FullName, $content, (New-Object System.Text.UTF8Encoding($false)))
    }
}

Write-Host "Emergency Repair Complete. Navbar structure restored."
