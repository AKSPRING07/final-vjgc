$filePath = (Resolve-Path 'public\about-us-v1.html').Path
$content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)

# ────────────────────────────────────────────────
# 1. ADD IMAGES after each card-year-badge
# ────────────────────────────────────────────────
$imgs = @{
    '>2005<' = '>2005<' + "`r`n`t`t`t`t`t`t`t`t<img src=""images/media/hero_foundation_1.png"" alt=""Lakshmi Travels"" class=""card-img"">"
    'green>2007<' = 'green>2007<' + "`r`n`t`t`t`t`t`t`t`t<img src=""images/media/hero_foundation_2.png"" alt=""NVRS Logistics"" class=""card-img"">"
    '>2009<' = '>2009<' + "`r`n`t`t`t`t`t`t`t`t<img src=""images/media/hero_foundation_3.png"" alt=""Lakshmi Gardens"" class=""card-img"">"
    'green>2011<' = 'green>2011<' + "`r`n`t`t`t`t`t`t`t`t<img src=""images/media/hero_foundation_4.png"" alt=""Vijay Anjenya Traders"" class=""card-img"">"
    '>2015<' = '>2015<' + "`r`n`t`t`t`t`t`t`t`t<img src=""images/media/hero_foundation_5.png"" alt=""Aditya Powers"" class=""card-img"">"
    'green>2018<' = 'green>2018<' + "`r`n`t`t`t`t`t`t`t`t<img src=""images/media/csr_solutions.png"" alt=""Springreen"" class=""card-img"">"
    '>2019<' = '>2019<' + "`r`n`t`t`t`t`t`t`t`t<img src=""images/media/solutions_new.png"" alt=""Aditya Solutions"" class=""card-img"">"
    'green>2022<' = 'green>2022<' + "`r`n`t`t`t`t`t`t`t`t<img src=""images/media/csr_education.png"" alt=""Aditya Institute"" class=""card-img"">"
    '>2025<' = '>2025<' + "`r`n`t`t`t`t`t`t`t`t<img src=""images/media/csr_wellness.png"" alt=""Aham Graham"" class=""card-img"">"
}

# Only add images where card-year-badge exists (not already added)
if ($content -notmatch 'card-img') {
    foreach ($key in $imgs.Keys) {
        $content = $content -replace [regex]::Escape($key), $imgs[$key]
    }
    Write-Host "Images added"
} else {
    Write-Host "Images already present - skipping"
}

# ────────────────────────────────────────────────
# 2. INJECT NEW CSS before closing </style> of timeline section
# ────────────────────────────────────────────────
$newCSS = @"

				/* ===== INTER FONT ===== */
				@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

				/* ===== CARD IMAGE HOVER ===== */
				.timeline-card {
					transition: transform 0.4s cubic-bezier(0.22,1,0.36,1), box-shadow 0.4s ease !important;
				}
				.timeline-card:hover {
					transform: translateY(-8px) scale(1.01) !important;
					box-shadow: 0 24px 60px rgba(8, 32, 27, 0.18) !important;
				}
				.card-img {
					width: 100%;
					height: 180px;
					object-fit: cover;
					display: block;
					transition: transform 0.6s ease;
				}
				.timeline-card:hover .card-img {
					transform: scale(1.06);
				}

				/* ===== FONT UPGRADE ===== */
				.card-brand {
					font-family: 'Inter', 'Segoe UI', sans-serif !important;
					font-size: 22px !important;
					font-weight: 800 !important;
					letter-spacing: -0.3px !important;
				}
				.card-brand i { margin-right: 6px; }
				.card-tagline {
					font-family: 'Inter', 'Segoe UI', sans-serif !important;
					font-size: 13px !important;
					color: #999 !important;
				}
				.card-year-badge {
					font-family: 'Inter', sans-serif !important;
					font-size: 12px !important;
					letter-spacing: 2px !important;
					text-transform: uppercase !important;
					padding: 6px 18px !important;
				}
				.detail-row {
					font-family: 'Inter', 'Segoe UI', sans-serif !important;
					font-size: 14px !important;
					color: #333 !important;
					line-height: 1.6 !important;
					letter-spacing: 0.1px !important;
				}
				.detail-row strong { font-weight: 700 !important; }
				.card-details {
					border-top: 1px solid #f0f0f0;
					padding-top: 16px;
					gap: 12px !important;
				}
				.phase-title, .phase-desc, .phase-tag,
				.vjs-positioning-header h3, .vjs-positioning-header p,
				.vjs-future-header h3, .future-card h4,
				.future-card p, .vertical-chip {
					font-family: 'Inter', 'Segoe UI', sans-serif !important;
				}

				/* ===== FLOATING PARTICLE BG ===== */
				.vjs-bubble-wrap {
					position: absolute;
					inset: 0;
					z-index: 0;
					pointer-events: none;
					overflow: hidden;
				}
				.vjs-bubble {
					position: absolute;
					border-radius: 50%;
					opacity: 0;
					animation: vjsBubbleFloat linear infinite;
				}
				.vjs-bubble:nth-child(1) { width:200px;height:200px;left:5%; background:radial-gradient(circle, rgba(158,192,8,0.14), transparent 70%); animation-duration:22s; }
				.vjs-bubble:nth-child(2) { width:300px;height:300px;left:70%; background:radial-gradient(circle, rgba(8,32,27,0.08), transparent 70%); animation-duration:28s; animation-delay:-4s; }
				.vjs-bubble:nth-child(3) { width:120px;height:120px;left:40%; background:radial-gradient(circle, rgba(158,192,8,0.16), transparent 70%); animation-duration:18s; animation-delay:-8s; }
				.vjs-bubble:nth-child(4) { width:260px;height:260px;left:85%; background:radial-gradient(circle, rgba(25,97,100,0.09), transparent 70%); animation-duration:32s; animation-delay:-12s; }
				.vjs-bubble:nth-child(5) { width:160px;height:160px;left:22%; background:radial-gradient(circle, rgba(158,192,8,0.11), transparent 70%); animation-duration:24s; animation-delay:-2s; }
				.vjs-bubble:nth-child(6) { width:180px;height:180px;left:55%; background:radial-gradient(circle, rgba(8,32,27,0.06), transparent 70%); animation-duration:26s; animation-delay:-6s; }

				@keyframes vjsBubbleFloat {
					0%   { transform:translateY(100vh) scale(0.4); opacity:0; }
					10%  { opacity:0.8; }
					90%  { opacity:0.8; }
					100% { transform:translateY(-120vh) scale(1.2); opacity:0; }
				}
"@

# Inject before the RESPONSIVE media query comment
$marker = "/* ===== RESPONSIVE ===== */"
if ($content -match [regex]::Escape($marker)) {
    $content = $content.Replace($marker, $newCSS + "`r`n`t`t`t`t" + $marker)
    Write-Host "CSS injected"
} else {
    Write-Host "WARNING: RESPONSIVE marker not found"
}

# ────────────────────────────────────────────────
# 3. UPGRADE BACKGROUND GRADIENT
# ────────────────────────────────────────────────
$content = $content.Replace(
    'background: #f8f8f8; color: #081c17; position: relative; overflow: hidden;',
    'background: linear-gradient(160deg, #eef7e8 0%, #f8faf5 50%, #e8f4ef 100%); color: #081c17; position: relative; overflow: hidden;'
)

[System.IO.File]::WriteAllText($filePath, $content, [System.Text.Encoding]::UTF8)
Write-Host "SUCCESS: All 3 updates applied"
