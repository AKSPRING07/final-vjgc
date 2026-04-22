$content = [System.IO.File]::ReadAllText((Resolve-Path 'public\about-us-v1.html'), [System.Text.Encoding]::UTF8)

# 1. ADD IMAGES TO EACH CARD
$content = $content -replace '(<div class="card-year-badge">2005</div>)', '$1<img src="images/media/hero_foundation_1.png" alt="Lakshmi Travels" class="card-img">'
$content = $content -replace '(<div class="card-year-badge green">2007</div>)', '$1<img src="images/media/hero_foundation_2.png" alt="NVRS Logistics" class="card-img">'
$content = $content -replace '(<div class="card-year-badge">2009</div>)', '$1<img src="images/media/hero_foundation_3.png" alt="Lakshmi Gardens" class="card-img">'
$content = $content -replace '(<div class="card-year-badge green">2011</div>)', '$1<img src="images/media/hero_foundation_4.png" alt="Vijay Anjenya Traders" class="card-img">'
$content = $content -replace '(<div class="card-year-badge">2015</div>)', '$1<img src="images/media/hero_foundation_5.png" alt="Aditya Powers" class="card-img">'
$content = $content -replace '(<div class="card-year-badge green">2018</div>)', '$1<img src="images/media/csr_solutions.png" alt="Springreen" class="card-img">'
$content = $content -replace '(<div class="card-year-badge">2019</div>)', '$1<img src="images/media/solutions_new.png" alt="Aditya Solutions" class="card-img">'
$content = $content -replace '(<div class="card-year-badge green">2022</div>)', '$1<img src="images/media/csr_education.png" alt="Aditya Institute" class="card-img">'
$content = $content -replace '(<div class="card-year-badge">2025</div>)', '$1<img src="images/media/csr_wellness.png" alt="Aham Graham" class="card-img">'

# 2. REPLACE CARD CSS with enhanced version (images + fonts)
$oldCSS = '/* ===== TIMELINE CARD ===== */
				.timeline-card {
					background: #fff;
					border-radius: 20px;
					overflow: hidden;
					border: 1px solid #e8f0e0;
					transition: transform 0.3s ease, box-shadow 0.3s ease;
				}
				.timeline-card:hover {
					transform: translateY(-4px);
					box-shadow: 0 20px 50px rgba(8, 32, 27, 0.12) !important;
				}
				.card-year-badge {
					background: #08201b;
					color: #dfff7c;
					font-size: 13px;
					font-weight: 700;
					padding: 8px 20px;
					letter-spacing: 1px;
				}
				.card-year-badge.green { background: #9ec008; color: #08201b; }
				.card-body { padding: 24px; }
				.card-brand {
					font-size: 20px;
					font-weight: 700;
					color: #08201b;
					margin-bottom: 6px;
				}
				.card-tagline {
					font-size: 13px;
					color: #888;
					margin-bottom: 18px;
					font-style: italic;
				}
				.card-details { display: flex; flex-direction: column; gap: 10px; }
				.detail-row {
					display: flex;
					gap: 10px;
					align-items: flex-start;
					font-size: 13.5px;
					color: #444;
					line-height: 1.5;
				}
				.detail-icon { font-size: 16px; flex-shrink: 0; margin-top: 1px; }
				.detail-row strong { color: #08201b; }'

$newCSS = '/* ===== INTER FONT ===== */
				@import url(''https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'');

				/* ===== TIMELINE CARD ===== */
				.timeline-card {
					background: #fff;
					border-radius: 20px;
					overflow: hidden;
					border: 1px solid #e8f0e0;
					transition: transform 0.4s cubic-bezier(0.22,1,0.36,1), box-shadow 0.4s ease;
					position: relative;
				}
				.timeline-card:hover {
					transform: translateY(-8px) scale(1.01);
					box-shadow: 0 24px 60px rgba(8, 32, 27, 0.15) !important;
				}
				.timeline-card .card-img {
					width: 100%;
					height: 180px;
					object-fit: cover;
					display: block;
					transition: transform 0.6s ease;
				}
				.timeline-card:hover .card-img {
					transform: scale(1.06);
				}
				.card-year-badge {
					background: #08201b;
					color: #dfff7c;
					font-family: ''Inter'', ''Segoe UI'', sans-serif;
					font-size: 12px;
					font-weight: 700;
					padding: 6px 18px;
					letter-spacing: 2px;
					text-transform: uppercase;
					position: relative;
					z-index: 2;
				}
				.card-year-badge.green { background: #9ec008; color: #08201b; }
				.card-body { padding: 28px; }
				.card-brand {
					font-family: ''Inter'', ''Segoe UI'', sans-serif;
					font-size: 22px;
					font-weight: 800;
					color: #08201b;
					margin-bottom: 8px;
					letter-spacing: -0.3px;
				}
				.card-brand i { margin-right: 6px; }
				.card-tagline {
					font-family: ''Inter'', ''Segoe UI'', sans-serif;
					font-size: 13px;
					color: #999;
					margin-bottom: 20px;
					font-style: italic;
					letter-spacing: 0.2px;
				}
				.card-details {
					display: flex;
					flex-direction: column;
					gap: 12px;
					border-top: 1px solid #f0f0f0;
					padding-top: 16px;
				}
				.detail-row {
					display: flex;
					gap: 12px;
					align-items: flex-start;
					font-family: ''Inter'', ''Segoe UI'', sans-serif;
					font-size: 14px;
					color: #333;
					line-height: 1.6;
					letter-spacing: 0.1px;
				}
				.detail-icon {
					font-size: 18px;
					flex-shrink: 0;
					margin-top: 2px;
					width: 22px;
					text-align: center;
				}
				.detail-row strong {
					color: #08201b;
					font-weight: 700;
				}

				/* ===== ALL SECTION FONTS ===== */
				.phase-title, .phase-desc, .phase-tag {
					font-family: ''Inter'', ''Segoe UI'', sans-serif;
				}
				.vjs-positioning-header h3, .vjs-positioning-header p,
				.vjs-future-header h3, .future-card h4, .future-card p,
				.vertical-chip {
					font-family: ''Inter'', ''Segoe UI'', sans-serif;
				}

				/* ===== FLOATING PARTICLES BG ===== */
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
				.vjs-bubble:nth-child(1) { width: 200px; height: 200px; left: 5%; background: radial-gradient(circle, rgba(158,192,8,0.12), transparent 70%); animation-duration: 22s; animation-delay: 0s; }
				.vjs-bubble:nth-child(2) { width: 300px; height: 300px; left: 70%; background: radial-gradient(circle, rgba(8,32,27,0.08), transparent 70%); animation-duration: 28s; animation-delay: -4s; }
				.vjs-bubble:nth-child(3) { width: 120px; height: 120px; left: 40%; background: radial-gradient(circle, rgba(158,192,8,0.15), transparent 70%); animation-duration: 18s; animation-delay: -8s; }
				.vjs-bubble:nth-child(4) { width: 250px; height: 250px; left: 85%; background: radial-gradient(circle, rgba(25,97,100,0.08), transparent 70%); animation-duration: 32s; animation-delay: -12s; }
				.vjs-bubble:nth-child(5) { width: 160px; height: 160px; left: 20%; background: radial-gradient(circle, rgba(158,192,8,0.10), transparent 70%); animation-duration: 24s; animation-delay: -2s; }
				.vjs-bubble:nth-child(6) { width: 180px; height: 180px; left: 55%; background: radial-gradient(circle, rgba(8,32,27,0.06), transparent 70%); animation-duration: 26s; animation-delay: -6s; }
				@keyframes vjsBubbleFloat {
					0%   { transform: translateY(100vh) scale(0.4) rotate(0deg); opacity: 0; }
					10%  { opacity: 0.7; }
					90%  { opacity: 0.7; }
					100% { transform: translateY(-120vh) scale(1.2) rotate(180deg); opacity: 0; }
				}'

$content = $content.Replace($oldCSS, $newCSS)

# 3. UPGRADE BACKGROUND GRADIENT
$content = $content.Replace('background: #f8f8f8; color: #081c17; position: relative; overflow: hidden;', 'background: linear-gradient(180deg, #f0f7ec 0%, #f8f8f8 40%, #eef5e8 100%); color: #081c17; position: relative; overflow: hidden;')

[System.IO.File]::WriteAllText((Resolve-Path 'public\about-us-v1.html'), $content, [System.Text.Encoding]::UTF8)
Write-Host 'ALL DONE: Images + Fonts + Background Animation applied'
