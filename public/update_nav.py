import os
import re

mega_menu_html = """									<li class="nav-item dropdown mega-dropdown">
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
									</li>"""

sustainability_link_html = """									<li class="nav-item">
										<a class="nav-link" href="shop-grid.html" role="button">Sustainability</a>
									</li>"""

# More flexible regex
businesses_regex = re.compile(r'<li class="nav-item dropdown">[^<]*<a[^>]*>[^<]*Businesses[^<]*</a>\s*<ul class="dropdown-menu">.*?</ul>\s*</li>', re.DOTALL | re.IGNORECASE)
sustainability_regex = re.compile(r'<li class="nav-item dropdown">[^<]*<a[^>]*>[^<]*Sustainability[^<]*</a>\s*<ul class="dropdown-menu">.*?</ul>\s*</li>', re.DOTALL | re.IGNORECASE)

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = businesses_regex.sub(mega_menu_html, content)
        new_content = sustainability_regex.sub(sustainability_link_html, new_content)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
