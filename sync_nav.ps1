# sync_nav.ps1
# This script synchronizes the navigation bar and its styles from index-2.html to all other HTML files.

$styleBlock = @'
	<style>
		@media (min-width: 992px) {

			.adani-nav-fx {
				padding: 0;
				align-self: top;
				margin: 0;
				background: #08201b;
				border: none !important;
				box-shadow: none !important;
				width: 100%;

				/* 🔥 FIX: lock to top */
				position: fixed;
				top: 0;
				left: 0;
				z-index: 9999;
			}

			.adani-nav-fx .inner-content {
				padding: 0;
				margin: 0;
				animation: adaniNavReveal 0.75s cubic-bezier(0.22, 1, 0.36, 1);
			}

			.adani-nav-fx .top-header {
				position: relative;
				padding: 18px 20px;

				/* ❌ REMOVE this (causes line) */
				/* margin: -1px 0; */

				margin: 0;

				width: 100%;
				border-radius: 0;
				transition: padding 0.45s cubic-bezier(0.22, 1, 0.36, 1);

				transform: translateZ(0);
				backface-visibility: hidden;
				isolation: isolate;
			}
		}

		/* ================= GLASS EFFECT ================= */

		.adani-nav-fx .top-header::before {
			content: "";
			position: absolute;

			/* 🔥 STRONG FIX */
			top: -4px;
			bottom: -3px;
			left: 0;
			right: 0;

			border-radius: inherit;

			background: linear-gradient(135deg,
					rgba(8, 32, 27, 0.88) 0%,
					rgba(8, 32, 27, 0.82) 50%,
					rgba(8, 32, 27, 0.88) 100%);

			backdrop-filter: blur(10px);
			-webkit-backdrop-filter: blur(10px);

			transform: translateZ(0);
			will-change: transform;

			z-index: 0;
		}

		/* 🔥 HARD TOP COVER (FINAL LINE KILLER) */
		.adani-nav-fx::before {
			content: "";
			position: absolute;
			top: 0;
			left: 0;
			width: 100%;
			height: 3px;
			background: #08201b;
			z-index: 10000;
			padding-top: 0%;
		}

		/* keep content above */
		.adani-nav-fx .top-header>.d-flex {
			position: relative;
			z-index: 2;
		}

		/* LOGO */
		.adani-nav-fx .logo img {
			transition: transform 0.45s ease;
			background-color: #9ec008;
			border-radius: 50%;
		}

		/* NAVBAR */
		.adani-nav-fx .navbar-nav {
			gap: 20px;
		}

		.adani-nav-fx .nav-item .nav-link {
			padding: 6px 16px;
			border-radius: 999px;
			font-size: 14px;
			color: rgba(255, 255, 255, 0.85);
			transition: all 0.35s ease;
		}

		/* HOVER */
		.adani-nav-fx .nav-item:hover>.nav-link,
		.adani-nav-fx .nav-item.nav-current>.nav-link {
			color: #dfff7c;
			transform: translateY(-0.5px);
		}

		/* HOVER INDICATOR */
		.adani-nav-fx .nav-hover-indicator {
			position: absolute;
			top: 0;
			left: 0;
			height: 100%;
			width: 0;
			border-radius: 999px;
			pointer-events: none;
			opacity: 0;
			transform: scale(0.92);

			background: linear-gradient(135deg,
					rgba(255, 255, 255, 0.18),
					rgba(255, 255, 255, 0.05));

			transition: all 0.45s cubic-bezier(0.22, 1, 0.36, 1);
		}

		/* DROPDOWN */
		.adani-nav-fx .navbar .dropdown-menu {
			margin-top: 14px;
			padding: 14px 8px;
			border-radius: 24px;
			border: 1px solid rgba(255, 255, 255, 0.05);
			background: rgba(253, 253, 253, 0.719);

			transform: translateY(18px) scale(0.96);
			clip-path: inset(0 0 100% 0 round 24px);

			transition: transform 0.45s cubic-bezier(0.22, 1, 0.36, 1),
				opacity 0.3s ease,
				visibility 0.3s ease,
				clip-path 0.45s cubic-bezier(0.22, 1, 0.36, 1);
		}

		.adani-nav-fx .navbar .dropdown:hover>.dropdown-menu {
			transform: translateY(0) scale(1);
			clip-path: inset(0 0 0 0 round 24px);
		}

		/* ================= STICKY STATE ================= */

		.adani-nav-fx.fixed {
			padding-top: 12px;
			background: #08201b;
		}

		.adani-nav-fx.fixed .top-header {
			padding: 12px 0;
		}

		.adani-nav-fx.fixed .top-header::before {
			top: -4px;
			bottom: -3px;

			background: linear-gradient(135deg,
					rgba(8, 32, 27, 0.96) 0%,
					rgba(8, 32, 27, 0.92) 50%,
					rgba(8, 32, 27, 0.96) 100%);

			backdrop-filter: blur(12px);
			-webkit-backdrop-filter: blur(12px);
		}

		/* LOGO SCALE */
		.adani-nav-fx.fixed .logo img {
			transform: scale(0.94);
		}

		/* MOBILE */
		@media (max-width: 991px) {
			.adani-nav-fx .top-header {
				position: relative;
				z-index: 5;
				margin: 0;
				background: #08201b;
			}
		}

		/* BODY FIX */
		html,
		body {
			margin: 0;
			padding: 0;
			background: #08201b;
		}

		/* ANIMATION */
		@keyframes adaniNavReveal {
			from {
				opacity: 0;
				transform: translateY(-18px);
			}

			to {
				opacity: 1;
				transform: translateY(0);
			}
		}
	</style>
'@

$headerBlock = @'
		<header class="theme-main-menu menu-overlay menu-style-one white-vr sticky-menu adani-nav-fx">
			<div class="inner-content position-relative">
				<div class="top-header">
					<div class="d-flex align-items-center justify-content-between">
						<div class="logo" style="flex: 1; display: flex; justify-content: flex-start;">
							<a href="index-2.html" class="d-flex align-items-center">
								<span class="site-brand-lockup" aria-label="Vijayalakshmi Group Of Companies">
									<span class="site-brand-lockup__mark-wrap"><img
											src="images/logo/vijayalakshmi-mark.png" alt=""
											class="site-brand-lockup__mark"></span>
									<span class="site-brand-lockup__text">
										<span class="site-brand-lockup__title">Vijayalakshmi&nbsp;Groups</span>
										<span class="site-brand-lockup__subtitle">Of Companies</span>
									</span>
								</span>
							</a>
						</div>
						<!-- logo -->

						<nav class="navbar navbar-expand-lg p0" style="flex: 0 0 auto; margin-right: 60px;">
							<button class="navbar-toggler d-block d-lg-none" type="button" data-bs-toggle="collapse"
								data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false"
								aria-label="Toggle navigation">
								<span></span>
							</button>
							<div class="collapse navbar-collapse" id="navbarNav">
								<ul class="navbar-nav align-items-lg-center">
									<li class="d-block d-lg-none">
										<div class="logo">
											<a href="index-2.html" class="d-block">
												<span class="site-brand-lockup"
													aria-label="Vijayalakshmi Group Of Companies">
													<span class="site-brand-lockup__mark-wrap"><img
															src="images/logo/vijayalakshmi-mark.png" alt=""
															class="site-brand-lockup__mark"></span>
													<span class="site-brand-lockup__text">
														<span class="site-brand-lockup__title">Vijayalakshmi
															Groups</span>
														<span class="site-brand-lockup__subtitle">OF COMPANIES</span>
													</span>
												</span>
											</a>
										</div>
									</li>
									<li class="nav-item dropdown">
										<a class="nav-link dropdown-toggle" href="#" role="button"
											data-bs-toggle="dropdown" data-bs-auto-close="outside"
											aria-expanded="false">About Us
										</a>
										<ul class="dropdown-menu">
											<li><a href="about-us-v2.html" class="dropdown-item"><span>Our
														Group</span></a></li>
											<li><a href="about-us-v1.html" class="dropdown-item"><span>Our Mission and
														Vision</span></a></li>
											<li><a href="service-v1.html" class="dropdown-item"><span>Leadership and
														Awards</span></a></li>
										</ul>
									</li>
									<li class="nav-item dropdown">
										<a class="nav-link dropdown-toggle" href="#" role="button"
											data-bs-toggle="dropdown" data-bs-auto-close="outside"
											aria-expanded="false">Businesses
										</a>
										<ul class="dropdown-menu">
											<li><a href="index.html" class="dropdown-item"><span>Finance</span></a></li>
											<li><a href="index-2.html" class="dropdown-item"><span>Business
														Consultancy</span></a></li>
											<li><a href="index-3.html" class="dropdown-item"><span>Banking</span></a>
											</li>
											<li><a href="index-4.html" class="dropdown-item"><span>Payment
														Solution</span></a></li>
											<li><a href="index-5.html" class="dropdown-item"><span>Digital
														Agency</span></a></li>
											<li><a href="index-6.html" class="dropdown-item"><span>Marketing</span></a>
											</li>
											<li><a href="index-7.html" class="dropdown-item"><span>Insurance</span></a>
											</li>
											<li><a href="index-8.html" class="dropdown-item"><span>Insurance
														Two</span></a></li>
										</ul>
									</li>
									<li class="nav-item dropdown">
										<a class="nav-link dropdown-toggle" href="#" role="button"
											data-bs-toggle="dropdown" data-bs-auto-close="outside"
											aria-expanded="false">Sustainability
										</a>
										<ul class="dropdown-menu">
											<li><a href="shop-grid.html" class="dropdown-item"><span>Shop
														Grid</span></a></li>
											<li><a href="shop-details.html" class="dropdown-item"><span>Shop
														Details</span></a></li>
											<li><a href="cart.html" class="dropdown-item"><span>Cart</span></a></li>
											<li><a href="checkout.html" class="dropdown-item"><span>Checkout</span></a>
											</li>
										</ul>
									</li>
									<li class="nav-item">
										<a class="nav-link" href="blog-v1.html" role="button">Vijayalakshmi Foundation</a>
									</li>
									<li class="nav-item dropdown">
										<a class="nav-link dropdown-toggle" href="#" role="button"
											data-bs-toggle="dropdown" data-bs-auto-close="outside"
											aria-expanded="false">Newsroom
										</a>
										<ul class="dropdown-menu">
											<li><a href="media-release.html" class="dropdown-item"><span>Media Release</span></a></li>
											<li><a href="media-kit.html" class="dropdown-item"><span>Media Kit</span></a></li>
										</ul>
									</li>
								</ul>
							</div>
						</nav>

						<div class="right-widget d-none d-lg-flex align-items-center">
							<!-- Accessibility Dropdown -->
							<div class="vjs-nav-action dropdown ps-3 ps-xl-4">
								<button class="dropdown-toggle d-flex align-items-center style-none" type="button"
									data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside">
									<i class="bi bi-universal-access fs-5 text-white"></i>
									<i class="bi bi-chevron-down ms-1 text-white opacity-50"
										style="font-size: 10px;"></i>
								</button>
								<div class="dropdown-menu dropdown-menu-end vjs-accessibility-panel">
									<h5>Accessibility Adjustments</h5>
									<p>Choose the right accessibility profile for you</p>
									<div class="vjs-divider"></div>
									<div class="vjs-adjust-grid">
										<button class="vjs-adjust-btn" onclick="vjsSetMode('light')">Light Mode</button>
										<button class="vjs-adjust-btn" onclick="vjsSetMode('dark')">Dark Mode</button>
									</div>
									<div class="vjs-divider"></div>
									<div class="vjs-font-grid">
										<button class="vjs-adjust-btn" onclick="vjsSetFontSize('small')">-A</button>
										<button class="vjs-adjust-btn" onclick="vjsSetFontSize('normal')">A</button>
										<button class="vjs-adjust-btn" onclick="vjsSetFontSize('large')">+A</button>
									</div>
									<div class="vjs-divider"></div>
									<div class="text-center">
										<button class="vjs-reset-btn" onclick="vjsResetSettings()">Reset
											Settings</button>
									</div>
								</div>
							</div>
							<!-- Language Dropdown -->
							<div class="vjs-nav-action dropdown ps-3 ps-xl-4">
								<button class="dropdown-toggle d-flex align-items-center style-none" type="button"
									data-bs-toggle="dropdown" aria-expanded="false">
									<span class="text-white fw-500 fs-6 vjs-lang-label">ENG</span>
									<i class="bi bi-chevron-down ms-1 text-white opacity-50"
										style="font-size: 10px;"></i>
								</button>
								<ul class="dropdown-menu dropdown-menu-end">
									<li><a class="dropdown-item" href="javascript:translateTo('ta')">Tamil</a></li>
									<li><a class="dropdown-item" href="javascript:translateTo('en')">English</a></li>
									<li><a class="dropdown-item" href="javascript:translateTo('hi')">Hindi</a></li>
								</ul>
							</div>
						</div>
					</div> <!--/.top-header-->
				</div> <!-- /.inner-content -->
		</header>
'@

$scriptBlock = @'
		<script src="js/site-utils.js"></script>
		<!-- Google Translate Element -->
		<div id="google_translate_element" style="display:none;"></div>
		<script type="text/javascript"
			src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
'@

$files = Get-ChildItem "public/*.html" -Exclude "index-2.html"

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    
    # 1. Replace Nav Style Block
    # Look for the style block containing adani-nav-fx
    $content = $content -replace '(?s)<style>.*?\.adani-nav-fx.*?</style>', $styleBlock
    
    # 2. Replace Header Block
    # Look for the header block with adani-nav-fx
    $content = $content -replace '(?s)<header class="[^"]*adani-nav-fx[^"]*">.*?</header>', $headerBlock
    
    # 3. Ensure site-utils.js and translate scripts are present at the bottom
    if ($content -notlike "*site-utils.js*") {
        $content = $content -replace '</body>', "$scriptBlock`n</body>"
    }

    Set-Content $file.FullName $content
}

Write-Host "Navigation synchronization complete across $($files.Count) pages."
