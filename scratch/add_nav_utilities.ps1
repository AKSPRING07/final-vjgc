$path = Get-ChildItem -Path "public/*.html"
foreach ($file in $path) {
    if ($file.Name -eq "index-2.html") { continue } # Already updated manually
    
    $content = Get-Content $file.FullName -Raw
    
    # 1. Mobile Dropdowns Injection (After Contact Us)
    $mobileTarget = '(?s)<li class="nav-item">\s*<a class="nav-link" href="contact.html" role="button">Contact Us</a>\s*</li>'
    $mobileReplacement = '<li class="nav-item">
										<a class="nav-link" href="contact.html" role="button">Contact Us</a>
									</li>
									<li class="nav-item dropdown d-md-none mt-10">
										<a class="nav-link dropdown-toggle d-flex align-items-center" href="#" role="button"
											data-bs-toggle="dropdown" aria-expanded="false">
											<i class="bi bi-universal-access pe-2"></i> Accessibility
										</a>
										<ul class="dropdown-menu">
											<li><a class="dropdown-item" href="#">Screen Reader</a></li>
											<li><a class="dropdown-item" href="#">High Contrast</a></li>
										</ul>
									</li>
									<li class="nav-item dropdown d-md-none">
										<a class="nav-link dropdown-toggle d-flex align-items-center" href="#" role="button"
											data-bs-toggle="dropdown" aria-expanded="false">
											ENG
										</a>
										<ul class="dropdown-menu">
											<li><a class="dropdown-item" href="#">Tamil</a></li>
											<li><a class="dropdown-item" href="#">English</a></li>
											<li><a class="dropdown-item" href="#">Hindi</a></li>
										</ul>
									</li>'
    
    $newContent = [regex]::Replace($content, $mobileTarget, $mobileReplacement)

    # 2. Desktop Dropdowns Injection (Right Widget)
    $desktopTarget = '(?s)</nav>\s*</div>'
    $desktopReplacement = '</nav>

						<div class="right-widget d-none d-lg-flex align-items-center">
							<div class="vjs-nav-action dropdown ps-3 ps-xl-4">
								<button class="dropdown-toggle d-flex align-items-center style-none" type="button"
									data-bs-toggle="dropdown" aria-expanded="false">
									<i class="bi bi-universal-access fs-5 text-white"></i>
									<i class="bi bi-chevron-down ms-1 text-white opacity-50" style="font-size: 10px;"></i>
								</button>
								<ul class="dropdown-menu dropdown-menu-end">
									<li><a class="dropdown-item" href="#">Screen Reader</a></li>
									<li><a class="dropdown-item" href="#">High Contrast</a></li>
								</ul>
							</div>
							<div class="vjs-nav-action dropdown ps-3 ps-xl-4">
								<button class="dropdown-toggle d-flex align-items-center style-none" type="button"
									data-bs-toggle="dropdown" aria-expanded="false">
									<span class="text-white fw-500 fs-6">ENG</span>
									<i class="bi bi-chevron-down ms-1 text-white opacity-50" style="font-size: 10px;"></i>
								</button>
								<ul class="dropdown-menu dropdown-menu-end">
									<li><a class="dropdown-item" href="#">Tamil</a></li>
									<li><a class="dropdown-item" href="#">English</a></li>
									<li><a class="dropdown-item" href="#">Hindi</a></li>
								</ul>
							</div>
						</div>
					</div>'

    $newContent = [regex]::Replace($newContent, $desktopTarget, $desktopReplacement)

    if ($content -ne $newContent) {
        $newContent | Set-Content $file.FullName
        Write-Host "Updated $($file.Name)"
    }
}
