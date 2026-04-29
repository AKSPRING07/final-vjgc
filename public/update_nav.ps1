$megaMenuHtml = '									<li class="nav-item dropdown mega-dropdown">
										<a class="nav-link dropdown-toggle" href="#" role="button"
											data-bs-toggle="dropdown" data-bs-auto-close="outside"
											aria-expanded="false">Businesses
										</a>
										<ul class="dropdown-menu">
											<li>
												<div class="mega-menu-content">
													<div class="mega-column">
														<div class="mega-section">
															<span class="mega-title">IT Infrastructure</span>
															<ul class="mega-list">
																<li><a href="it-consulting.html">IT Consulting</a></li>
																<li><a href="data-centers-hosting.html">Enterprise Data Centers & Hosting Services</a></li>
															</ul>
														</div>
													</div>
													<div class="mega-column">
														<div class="mega-section">
															<span class="mega-title">Education & Skills</span>
															<ul class="mega-list">
																<li><a href="it-training.html">IT Training</a></li>
																<li><a href="yoga-wellness.html">Yoga & Wellness</a></li>
															</ul>
														</div>
													</div>
													<div class="mega-column">
														<div class="mega-section">
															<span class="mega-title">Energy & Sustainability</span>
															<ul class="mega-list">
																<li><a href="green-energy.html">Green Energy & Solar Manufacturing</a></li>
															</ul>
														</div>
													</div>
													<div class="mega-column">
														<div class="mega-section">
															<span class="mega-title">Agri & Trade</span>
															<ul class="mega-list">
																<li><a href="export-import.html">Export & Import</a></li>
																<li><a href="plantations.html">Plantations & Exotic Trees</a></li>
															</ul>
														</div>
													</div>
													<div class="mega-column">
														<div class="mega-section">
															<span class="mega-title">Real Estate</span>
															<ul class="mega-list">
																<li><a href="property-services.html">Property Services</a></li>
															</ul>
														</div>
													</div>
													<div class="mega-column">
														<div class="mega-section">
															<span class="mega-title">Logistics & Travel</span>
															<ul class="mega-list">
																<li><a href="logistics-services.html">Logistics Services</a></li>
																<li><a href="travel-rentals.html">Travel & Rentals</a></li>
															</ul>
														</div>
													</div>
												</div>
											</li>
										</ul>
									</li>'

$sustainabilityHtml = '									<li class="nav-item">
										<a class="nav-link" href="shop-grid.html" role="button">Sustainability</a>
									</li>'

$businessesRegex = '(?si)<li class="nav-item dropdown">[^<]*<a[^>]*>[^<]*Businesses[^<]*</a>\s*<ul class="dropdown-menu">.*?</ul>\s*</li>'
$sustainabilityRegex = '(?si)<li class="nav-item dropdown">[^<]*<a[^>]*>[^<]*Sustainability[^<]*</a>\s*<ul class="dropdown-menu">.*?</ul>\s*</li>'

Get-ChildItem -Path . -Include *.html | ForEach-Object {
    $content = [System.IO.File]::ReadAllText($_.FullName)
    $newContent = [regex]::Replace($content, $businessesRegex, $megaMenuHtml)
    $newContent = [regex]::Replace($newContent, $sustainabilityRegex, $sustainabilityHtml)
    
    if ($newContent -ne $content) {
        [System.IO.File]::WriteAllText($_.FullName, $newContent, [System.Text.Encoding]::UTF8)
        Write-Host "Updated $($_.Name)"
    }
}
