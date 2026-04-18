# sync_branding.ps1
# Synchronizes the finalized Chennai address, phone, and Footer Three branding across all HTML files in the public directory.

$footerThreeCode = @'
		<!--
		=====================================================
			Footer Three
		=====================================================
		-->
		<div class="footer-three">
			<div class="container">
				<div class="inner-wrapper position-relative">
					<div class="row justify-content-between">
						<div class="col-lg-4 footer-intro mb-30">
							<div class="round-bg rounded-circle text-center d-flex flex-column align-items-center justify-content-center m-auto">
								<div class="vjs-footer-brand">
									<img src="images/logo/vijayalakshmi-mark.png" alt="Vijayalakshmi Group" class="vjs-footer-logo-icon">
									<div class="vjs-footer-brand-name">Vijayalakshmi Group Of Companies</div>
								</div>
								<!-- /.vjs-footer-brand -->
								<p class="lh-sm mb-30">Headquartered in Chennai, India<br>Delivering Excellence Across Diverse Industries.</p>
								<p class="m0 fw-500"><a href="tel:+91 9943633443" class="text-dark">+91 9943633443</a></p>
							</div>
						</div>
						<div class="col-lg-2 col-sm-4 mb-20">
							<h5 class="footer-title">Links</h5>
							<ul class="footer-nav-link style-none">
								<li><a href="index.html">Home</a></li>
								<li><a href="pricing.html">Pricing Plan</a></li>
								<li><a href="about-us-v1.html">About us</a></li>
								<li><a href="service-v1.html">Our services</a></li>
								<li><a href="project-v2.html">Portfolio</a></li>
								<li><a href="service-v2.html">Features</a></li>
							</ul>
						</div>
						<div class="col-lg-2 col-sm-4 mb-20">
							<h5 class="footer-title">Company</h5>
							<ul class="footer-nav-link style-none">
								<li><a href="about-us-v2.html">About us</a></li>
								<li><a href="blog-v2.html">Blogs</a></li>
								<li><a href="faq.html">FAQ’s</a></li>
								<li><a href="contact.html">Contact</a></li>
							</ul>
						</div>
						<div class="col-xxl-2 col-lg-3 col-sm-4 mb-20">
							<h5 class="footer-title">Support</h5>
							<ul class="footer-nav-link style-none">
								<li><a href="contact.html">Terms of use</a></li>
								<li><a href="contact.html">Terms & conditions</a></li>
								<li><a href="contact.html">Privacy</a></li>
								<li><a href="contact.html">Cookie policy</a></li>
							</ul>
						</div>
					</div>
					<img src="images/lazy.svg" data-src="images/shape/shape_38.svg" alt="" class="lazy-img shapes shape_01">
					<img src="images/lazy.svg" data-src="images/shape/shape_39.svg" alt="" class="lazy-img shapes shape_02">
				</div> <!-- /.inner-wrapper -->
			</div>
			<div class="container">
				<div class="bottom-footer">
					<div class="row">
						<div class="col-xl-4 col-lg-3 order-lg-3 mb-15">
							<ul class="style-none d-flex align-items-center justify-content-center justify-content-lg-end social-icon">
								<li><a href="#"><i class="bi bi-facebook"></i></a></li>
								<li><a href="#"><i class="bi bi-dribbble"></i></a></li>
								<li><a href="#"><i class="bi bi-instagram"></i></a></li>
							</ul>
						</div>
						<div class="col-xl-4 col-lg-6 order-lg-2 mb-15">
							<ul class="style-none bottom-nav d-flex justify-content-center order-lg-last">
								<li><a href="contact.html">Privacy & Terms</a></li>
								<li><a href="contact.html">Cookies</a></li>
								<li><a href="contact.html">Contact Us</a></li>
							</ul>
						</div>
						<div class="col-xl-4 col-lg-3 order-lg-1 mb-15">
							<div class="copyright text-center text-lg-start order-lg-first">Copyright @2019 Vijayalakshmi Group Of Companies.</div>
						</div>
					</div>
				</div>
				<!-- /.bottom-footer -->
			</div>
		</div> <!-- /.footer-three -->
'@

$files = Get-ChildItem "public/*.html" -Exclude "about-us-v1.html"

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    
    # 1. Replace Address
    $content = $content -replace '2190 Urban Terrace, Mirpur,.*?Licensed in 50 states\.', 'Headquartered in Chennai, India<br>Delivering Excellence Across Diverse Industries.'
    
    # 2. Replace Phone
    $content = $content -replace 'tel:\+?757 699-4478', 'tel:+91 9943633443'
    $content = $content -replace '\+757 699-4478', '+91 9943633443'

    # 3. Handle specific Contact page address blocks
    if ($file.Name -eq "contact.html") {
        $content = $content -replace '1012 Pebda Parkway, Mirpur 2 <br>Dhaka, Bangladesh', 'Headquartered in Chennai, India <br>Delivering Excellence.'
        $content = $content -replace 'tel:310\.841\.5500', 'tel:+91 9943633443'
        $content = $content -replace '310\.841\.5500', '+91 9943633443'
        $content = $content -replace 'www\.babunlivechat\.com', 'www.vjsgroup.com'
    }

    # 4. Replace Footer (Two or Three) with Finalized Footer Three
    # Use a simpler regex to find the footer block
    $content = $content -replace '(?s)<!--\s+=====================================================\s+(Footer Two|Footer Three)\s+=====================================================\s+-->.*?<!-- /.footer-(two|three) -->', $footerThreeCode

    Set-Content $file.FullName $content
}

Write-Host "Branding synchronization complete across all pages."
