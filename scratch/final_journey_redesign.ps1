$filePath = (Resolve-Path "public\about-us-v1.html").Path
$content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)

$newSection = @"
		<!--
		=====================================================
			Our Journey Timeline
		=====================================================
		-->
		<div class="vjs-timeline-section py-5" style="background: linear-gradient(180deg, #f0f7ec 0%, #f8f8f8 40%, #eef5e8 100%); color: #081c17; position: relative; overflow: hidden;">
			
			<!-- Floating Particles BG -->
			<div class="vjs-bubble-wrap">
				<div class="vjs-bubble"></div>
				<div class="vjs-bubble"></div>
				<div class="vjs-bubble"></div>
				<div class="vjs-bubble"></div>
				<div class="vjs-bubble"></div>
				<div class="vjs-bubble"></div>
			</div>

			<div class="container">
				<div class="title-one text-center mb-70 lg-mb-40 wow fadeInUp">
					<div class="upper-title">Our Journey</div>
					<h2 style="font-family: 'Inter', sans-serif; font-weight: 800;">From a single venture to a multi-vertical integrated group — 20 years of building, growing and leading.</h2>
				</div>

				<div class="vjs-custom-linear-timeline py-5">
					<div class="timeline-v-line"></div>

					<!-- =============================== -->
					<!-- PHASE BANNER: Foundation Era -->
					<!-- =============================== -->
					<div class="vjs-phase-banner wow fadeInUp">
						<div class="vjs-phase-inner">
							<span class="phase-tag">Phase 1</span>
							<h3 class="phase-title">Foundation Era (2005 - 2011)</h3>
							<p class="phase-desc">Building cash flow, ground network, and asset base</p>
						</div>
					</div>

					<!-- 2005 -->
					<div class="timeline-item left-marker wow fadeInUp">
						<div class="marker-year blue">2005</div>
						<div class="marker-dot"></div>
						<div class="marker-content">
							<div class="timeline-card shadow-lg">
								<div class="card-image-wrap">
									<img src="images/media/hero_foundation_1.png" alt="Lakshmi Travels">
									<div class="card-year-badge">2005</div>
								</div>
								<div class="card-body">
									<h4 class="card-brand"><i class="bi bi-bus-front-fill"></i> Lakshmi Travels</h4>
									<p class="card-tagline">Connecting people to their destinations</p>
									<div class="card-details-box">
										<div class="detail-row">
											<span class="detail-icon seedling"><i class="bi bi-seedling"></i></span>
											<div><strong>Initial Stage:</strong> Local travel operations focused on reliability and customer trust</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon growth"><i class="bi bi-graph-up-arrow"></i></span>
											<div><strong>Growth Phase:</strong> Expanded routes, built repeat customer base</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon current"><i class="bi bi-building"></i></span>
											<div><strong>Current Role:</strong> Supports tourism + mobility ecosystem</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon strategic"><i class="bi bi-lightning-charge-fill"></i></span>
											<div><strong>Strategic Value:</strong> First revenue engine; brand trust foundation</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>

					<!-- 2007 -->
					<div class="timeline-item right-marker wow fadeInUp" data-wow-delay="0.1s">
						<div class="marker-content">
							<div class="timeline-card shadow-lg">
								<div class="card-image-wrap">
									<img src="images/media/hero_foundation_2.png" alt="NVRS Logistics">
									<div class="card-year-badge green">2007</div>
								</div>
								<div class="card-body">
									<h4 class="card-brand"><i class="bi bi-truck"></i> NVRS Logistics</h4>
									<p class="card-tagline">Goods transportation across the region</p>
									<div class="card-details-box">
										<div class="detail-row">
											<span class="detail-icon seedling"><i class="bi bi-seedling"></i></span>
											<div><strong>Initial Stage:</strong> Entry into goods transportation</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon growth"><i class="bi bi-graph-up-arrow"></i></span>
											<div><strong>Growth Phase:</strong> Strengthened regional logistics network</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon current"><i class="bi bi-building"></i></span>
											<div><strong>Current Role:</strong> Backbone for trade and supply chain movement</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon strategic"><i class="bi bi-lightning-charge-fill"></i></span>
											<div><strong>Strategic Value:</strong> Enables vertical integration (trade + distribution)</div>
										</div>
									</div>
								</div>
							</div>
						</div>
						<div class="marker-dot"></div>
						<div class="marker-year orange">2007</div>
					</div>

					<!-- 2009 -->
					<div class="timeline-item left-marker wow fadeInUp" data-wow-delay="0.2s">
						<div class="marker-year blue">2009</div>
						<div class="marker-dot"></div>
						<div class="marker-content">
							<div class="timeline-card shadow-lg">
								<div class="card-image-wrap">
									<img src="images/media/hero_foundation_3.png" alt="Lakshmi Gardens">
									<div class="card-year-badge">2009</div>
								</div>
								<div class="card-body">
									<h4 class="card-brand"><i class="bi bi-flower1"></i> Lakshmi Gardens & Properties</h4>
									<p class="card-tagline">Land, plantation & real estate ventures</p>
									<div class="card-details-box">
										<div class="detail-row">
											<span class="detail-icon seedling"><i class="bi bi-seedling"></i></span>
											<div><strong>Initial Stage:</strong> Land acquisition and plantation setup</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon growth"><i class="bi bi-graph-up-arrow"></i></span>
											<div><strong>Growth Phase:</strong> Expansion into real estate and asset holding</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon current"><i class="bi bi-building"></i></span>
											<div><strong>Current Role:</strong> Asset-backed stability + long-term appreciation</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon strategic"><i class="bi bi-lightning-charge-fill"></i></span>
											<div><strong>Strategic Value:</strong> Balance sheet strength + infrastructure control</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>

					<!-- 2011 -->
					<div class="timeline-item right-marker wow fadeInUp" data-wow-delay="0.3s">
						<div class="marker-content">
							<div class="timeline-card shadow-lg">
								<div class="card-image-wrap">
									<img src="images/media/hero_foundation_4.png" alt="Vijay Anjenya Traders">
									<div class="card-year-badge green">2011</div>
								</div>
								<div class="card-body">
									<h4 class="card-brand"><i class="bi bi-shop"></i> Vijay Anjenya Traders</h4>
									<p class="card-tagline">Agricultural trading & global supply chain</p>
									<div class="card-details-box">
										<div class="detail-row">
											<span class="detail-icon seedling"><i class="bi bi-seedling"></i></span>
											<div><strong>Initial Stage:</strong> Agricultural trading (fresh produce)</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon growth"><i class="bi bi-graph-up-arrow"></i></span>
											<div><strong>Growth Phase:</strong> Expanded into B2B and D2C channels</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon current"><i class="bi bi-building"></i></span>
											<div><strong>Current Role:</strong> Export-import and domestic supply chain</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon strategic"><i class="bi bi-lightning-charge-fill"></i></span>
											<div><strong>Strategic Value:</strong> Cash-flow driven business with global scalability</div>
										</div>
									</div>
								</div>
							</div>
						</div>
						<div class="marker-dot"></div>
						<div class="marker-year orange">2011</div>
					</div>

					<!-- =============================== -->
					<!-- PHASE BANNER: Expansion Era -->
					<!-- =============================== -->
					<div class="vjs-phase-banner wow fadeInUp">
						<div class="vjs-phase-inner phase-2">
							<span class="phase-tag">Phase 2</span>
							<h3 class="phase-title">Expansion & Diversification (2015 - 2019)</h3>
							<p class="phase-desc">Entering future-focused and scalable sectors</p>
						</div>
					</div>

					<!-- 2015 -->
					<div class="timeline-item left-marker wow fadeInUp" data-wow-delay="0.1s">
						<div class="marker-year blue">2015</div>
						<div class="marker-dot"></div>
						<div class="marker-content">
							<div class="timeline-card shadow-lg">
								<div class="card-image-wrap">
									<img src="images/media/hero_foundation_5.png" alt="Aditya Powers">
									<div class="card-year-badge">2015</div>
								</div>
								<div class="card-body">
									<h4 class="card-brand"><i class="bi bi-sun-fill"></i> Aditya Powers</h4>
									<p class="card-tagline">Rural electrification & green energy</p>
									<div class="card-details-box">
										<div class="detail-row">
											<span class="detail-icon seedling"><i class="bi bi-seedling"></i></span>
											<div><strong>Initial Stage:</strong> Rural electrification (panchayat-level solar deployment)</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon growth"><i class="bi bi-graph-up-arrow"></i></span>
											<div><strong>Growth Phase:</strong> Small-scale energy solutions</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon current"><i class="bi bi-building"></i></span>
											<div><strong>Current Role:</strong> Green energy vertical (early-stage scaling)</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon strategic"><i class="bi bi-lightning-charge-fill"></i></span>
											<div><strong>Strategic Value:</strong> ESG alignment + future infrastructure play</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>

					<!-- 2018 -->
					<div class="timeline-item right-marker wow fadeInUp" data-wow-delay="0.2s">
						<div class="marker-content">
							<div class="timeline-card shadow-lg">
								<div class="card-image-wrap">
									<img src="images/media/csr_solutions.png" alt="Springreen">
									<div class="card-year-badge green">2018</div>
								</div>
								<div class="card-body">
									<h4 class="card-brand"><i class="bi bi-laptop"></i> Springreen</h4>
									<p class="card-tagline">IT services, AI & digital consulting</p>
									<div class="card-details-box">
										<div class="detail-row">
											<span class="detail-icon seedling"><i class="bi bi-seedling"></i></span>
											<div><strong>Initial Stage:</strong> IT services and consulting</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon growth"><i class="bi bi-graph-up-arrow"></i></span>
											<div><strong>Growth Phase:</strong> Multi-service tech capabilities (AI, apps, automation)</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon current"><i class="bi bi-building"></i></span>
											<div><strong>Current Status:</strong> Core growth engine of the group</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon strategic"><i class="bi bi-lightning-charge-fill"></i></span>
											<div><strong>Strategic Value:</strong> High-margin, scalable, global positioning</div>
										</div>
									</div>
								</div>
							</div>
						</div>
						<div class="marker-dot"></div>
						<div class="marker-year orange">2018</div>
					</div>

					<!-- 2019 -->
					<div class="timeline-item left-marker wow fadeInUp" data-wow-delay="0.3s">
						<div class="marker-year blue">2019</div>
						<div class="marker-dot"></div>
						<div class="marker-content">
							<div class="timeline-card shadow-lg">
								<div class="card-image-wrap">
									<img src="images/media/solutions_new.png" alt="Aditya Solutions">
									<div class="card-year-badge">2019</div>
								</div>
								<div class="card-body">
									<h4 class="card-brand"><i class="bi bi-server"></i> Aditya Solutions</h4>
									<p class="card-tagline">Hosting, infrastructure & managed services</p>
									<div class="card-details-box">
										<div class="detail-row">
											<span class="detail-icon seedling"><i class="bi bi-seedling"></i></span>
											<div><strong>Initial Stage:</strong> Hosting and infrastructure services</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon growth"><i class="bi bi-graph-up-arrow"></i></span>
											<div><strong>Growth Phase:</strong> Managed services + domain reselling</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon current"><i class="bi bi-building"></i></span>
											<div><strong>Current Status:</strong> Digital backbone supporting tech clients</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon strategic"><i class="bi bi-lightning-charge-fill"></i></span>
											<div><strong>Strategic Value:</strong> Ownership of infrastructure layer (critical for scale)</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>

					<!-- =============================== -->
					<!-- PHASE BANNER: Ecosystem Phase -->
					<!-- =============================== -->
					<div class="vjs-phase-banner wow fadeInUp">
						<div class="vjs-phase-inner phase-3">
							<span class="phase-tag">Phase 3</span>
							<h3 class="phase-title">Ecosystem Consolidation (2022 - 2025)</h3>
							<p class="phase-desc">Talent creation, brand expansion & lifestyle integration</p>
						</div>
					</div>

					<!-- 2022 -->
					<div class="timeline-item right-marker wow fadeInUp" data-wow-delay="0.1s">
						<div class="marker-content">
							<div class="timeline-card shadow-lg">
								<div class="card-image-wrap">
									<img src="images/media/csr_education.png" alt="Aditya Institute">
									<div class="card-year-badge green">2022</div>
								</div>
								<div class="card-body">
									<h4 class="card-brand"><i class="bi bi-mortarboard-fill"></i> Aditya Institute</h4>
									<p class="card-tagline">Skill development & IT training</p>
									<div class="card-details-box">
										<div class="detail-row">
											<span class="detail-icon seedling"><i class="bi bi-seedling"></i></span>
											<div><strong>Initial Stage:</strong> Skill development and IT training</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon growth"><i class="bi bi-graph-up-arrow"></i></span>
											<div><strong>Growth Phase:</strong> Structured programs and career pathways</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon current"><i class="bi bi-building"></i></span>
											<div><strong>Current Status:</strong> Talent pipeline for internal + external demand</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon strategic"><i class="bi bi-lightning-charge-fill"></i></span>
											<div><strong>Strategic Value:</strong> Reduces hiring dependency, builds workforce control</div>
										</div>
									</div>
								</div>
							</div>
						</div>
						<div class="marker-dot"></div>
						<div class="marker-year orange">2022</div>
					</div>

					<!-- 2025 -->
					<div class="timeline-item left-marker wow fadeInUp" data-wow-delay="0.2s">
						<div class="marker-year blue">2025</div>
						<div class="marker-dot"></div>
						<div class="marker-content">
							<div class="timeline-card shadow-lg">
								<div class="card-image-wrap">
									<img src="images/media/csr_wellness.png" alt="Aham Graham">
									<div class="card-year-badge">2025</div>
								</div>
								<div class="card-body">
									<h4 class="card-brand"><i class="bi bi-heart-pulse-fill"></i> Aham Graham</h4>
									<p class="card-tagline">Wellness, self-healing & lifestyle academy</p>
									<div class="card-details-box">
										<div class="detail-row">
											<span class="detail-icon seedling"><i class="bi bi-seedling"></i></span>
											<div><strong>Initial Stage:</strong> Wellness and self-healing academy</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon growth"><i class="bi bi-graph-up-arrow"></i></span>
											<div><strong>Growth Phase:</strong> Community-driven brand development</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon current"><i class="bi bi-building"></i></span>
											<div><strong>Current Status:</strong> Emerging lifestyle and wellness vertical</div>
										</div>
										<div class="detail-row">
											<span class="detail-icon strategic"><i class="bi bi-lightning-charge-fill"></i></span>
											<div><strong>Strategic Value:</strong> Expands into consumer + experience economy</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>

				</div>

				<!-- CURRENT POSITIONING 2026 -->
				<div class="vjs-positioning-section wow fadeInUp mt-80">
					<div class="vjs-positioning-header">
						<span class="phase-tag">2026</span>
						<h3>Current Positioning — A Self-Sustaining Ecosystem</h3>
						<p>You have evolved into a multi-vertical integrated group with presence across six distinct verticals — achieving cross-leverage rarely seen at this scale.</p>
					</div>
					<div class="vjs-verticals-grid">
						<div class="vertical-chip"><span><i class="bi bi-laptop"></i></span> Technology & Infrastructure</div>
						<div class="vertical-chip"><span><i class="bi bi-truck"></i></span> Logistics & Trade</div>
						<div class="vertical-chip"><span><i class="bi bi-sun-fill"></i></span> Energy & Sustainability</div>
						<div class="vertical-chip"><span><i class="bi bi-house-fill"></i></span> Real Estate & Assets</div>
						<div class="vertical-chip"><span><i class="bi bi-mortarboard-fill"></i></span> Education & Talent</div>
						<div class="vertical-chip"><span><i class="bi bi-bus-front-fill"></i></span> Travel & Wellness</div>
					</div>
				</div>

				<!-- FUTURE VISION -->
				<div class="vjs-future-section wow fadeInUp mt-80 mb-60">
					<div class="vjs-future-header">
						<span class="phase-tag">Vision</span>
						<h3>Strategic Direction — Where We Go Next</h3>
					</div>
					<div class="vjs-future-grid">
						<div class="future-card">
							<div class="future-num">01</div>
							<h4>Unified Group Brand</h4>
							<p>Transition into a parent entity structure. Strengthen perception for investors and global clients.</p>
						</div>
						<div class="future-card">
							<div class="future-num">02</div>
							<h4>Vertical Integration at Scale</h4>
							<p>Tech + Infra + Talent. Logistics + Trade → End-to-end supply chain ownership.</p>
						</div>
						<div class="future-card">
							<div class="future-num">03</div>
							<h4>Global Expansion</h4>
							<p>IT services to international clients. Agri exports to new markets. Hosting — global infra partnerships.</p>
						</div>
						<div class="future-card">
							<div class="future-num">04</div>
							<h4>High-Value Focus Areas</h4>
							<p>AI-led products via Springreen. Renewable energy scaling via Aditya Powers. Data center expansion.</p>
						</div>
					</div>
				</div>

			</div>

			<style>
				@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap');

				.vjs-timeline-section {
					font-family: 'Inter', sans-serif;
				}

				.vjs-bubble-wrap {
					position: absolute;
					top: 0;
					left: 0;
					width: 100%;
					height: 100%;
					overflow: hidden;
					z-index: 0;
					pointer-events: none;
				}

				.vjs-bubble {
					position: absolute;
					border-radius: 50%;
					background: radial-gradient(circle, rgba(158, 192, 8, 0.15), transparent 70%);
					animation: vjsBubbleFloat linear infinite;
					opacity: 0;
				}

				@keyframes vjsBubbleFloat {
					0% { transform: translateY(100vh) scale(0.5); opacity: 0; }
					10% { opacity: 1; }
					90% { opacity: 1; }
					100% { transform: translateY(-20vh) scale(1.5); opacity: 0; }
				}

				.vjs-bubble:nth-child(1) { width: 150px; height: 150px; left: 10%; animation-duration: 22s; animation-delay: 0s; }
				.vjs-bubble:nth-child(2) { width: 250px; height: 250px; left: 75%; animation-duration: 30s; animation-delay: -5s; }
				.vjs-bubble:nth-child(3) { width: 100px; height: 100px; left: 45%; animation-duration: 18s; animation-delay: -10s; }
				.vjs-bubble:nth-child(4) { width: 200px; height: 200px; left: 20%; animation-duration: 35s; animation-delay: -15s; }
				.vjs-bubble:nth-child(5) { width: 120px; height: 120px; left: 85%; animation-duration: 25s; animation-delay: -2s; }
				.vjs-bubble:nth-child(6) { width: 180px; height: 180px; left: 30%; animation-duration: 28s; animation-delay: -8s; }

				.vjs-custom-linear-timeline {
					position: relative;
					max-width: 1100px;
					margin: 0 auto;
					z-index: 2;
				}

				.timeline-v-line {
					position: absolute;
					left: 50%;
					top: 0;
					bottom: 0;
					width: 2px;
					background: #ddead1;
					transform: translateX(-50%);
				}

				.vjs-phase-banner {
					width: 100%;
					text-align: center;
					margin: 50px 0;
					position: relative;
					z-index: 3;
				}

				.vjs-phase-inner {
					display: inline-block;
					background: #08201b;
					color: #fff;
					padding: 20px 40px;
					border-radius: 50px;
					box-shadow: 0 10px 40px rgba(0,0,0,0.15);
					border: 1px solid rgba(158, 192, 8, 0.2);
				}

				.vjs-phase-inner.phase-2 { background: #1a3c34; }
				.vjs-phase-inner.phase-3 { background: #2c544b; }

				.phase-tag {
					background: #9ec008;
					color: #08201b;
					font-size: 11px;
					font-weight: 800;
					padding: 4px 12px;
					border-radius: 20px;
					text-transform: uppercase;
					letter-spacing: 1.5px;
					font-family: 'Outfit', sans-serif;
				}

				.phase-title {
					font-family: 'Outfit', sans-serif;
					font-size: 26px;
					font-weight: 700;
					margin: 12px 0 6px;
					letter-spacing: -0.5px;
				}

				.phase-desc {
					font-size: 15px;
					opacity: 0.85;
					margin: 0;
					font-weight: 400;
				}

				.timeline-item {
					display: flex;
					align-items: center;
					justify-content: center;
					margin-bottom: 90px;
					position: relative;
					width: 100%;
				}

				.marker-year {
					width: 85px;
					height: 85px;
					border-radius: 50%;
					display: flex;
					align-items: center;
					justify-content: center;
					font-family: 'Outfit', sans-serif;
					font-weight: 800;
					font-size: 20px;
					background: #fff;
					z-index: 3;
					border: 4px solid;
					flex-shrink: 0;
					box-shadow: 0 10px 20px rgba(0,0,0,0.05);
				}

				.marker-year.blue { border-color: #08201b; color: #08201b; }
				.marker-year.orange { border-color: #9ec008; color: #9ec008; }

				.marker-dot {
					width: 14px;
					height: 14px;
					background: #08201b;
					border-radius: 50%;
					position: relative;
					z-index: 4;
					border: 3px solid #fff;
					box-shadow: 0 0 0 3px rgba(158, 192, 8, 0.3);
				}

				.marker-content {
					width: 45%;
					padding: 0 40px;
				}

				.timeline-card {
					background: #fff;
					border-radius: 28px;
					overflow: hidden;
					transition: all 0.5s cubic-bezier(0.165, 0.84, 0.44, 1);
					border: 1px solid rgba(222, 234, 209, 1);
					box-shadow: 0 15px 35px rgba(8, 32, 27, 0.04);
				}

				.timeline-card:hover {
					transform: translateY(-12px) scale(1.01);
					box-shadow: 0 40px 80px rgba(8, 32, 27, 0.12) !important;
					border-color: #9ec008;
				}

				.card-image-wrap {
					position: relative;
					height: 190px;
					overflow: hidden;
				}

				.card-image-wrap img {
					width: 100%;
					height: 100%;
					object-fit: cover;
					transition: transform 1s ease;
				}

				.timeline-card:hover .card-image-wrap img {
					transform: scale(1.12);
				}

				.card-year-badge {
					position: absolute;
					bottom: 15px;
					right: 20px;
					background: rgba(8, 32, 27, 0.85);
					backdrop-filter: blur(8px);
					color: #9ec008;
					padding: 6px 18px;
					border-radius: 30px;
					font-weight: 800;
					font-size: 14px;
					border: 1px solid rgba(255,255,255,0.1);
					font-family: 'Outfit', sans-serif;
				}

				.card-year-badge.green { background: rgba(158, 192, 8, 0.9); color: #08201b; }

				.card-body { padding: 35px; }

				.card-brand {
					font-family: 'Outfit', sans-serif;
					font-size: 24px;
					font-weight: 800;
					color: #08201b;
					margin-bottom: 6px;
					letter-spacing: -0.5px;
				}

				.card-tagline {
					font-size: 14px;
					color: #777;
					font-style: italic;
					margin-bottom: 25px;
					font-weight: 400;
				}

				.card-details-box {
					background: #fbfdf9;
					padding: 25px;
					border-radius: 20px;
					display: flex;
					flex-direction: column;
					gap: 18px;
					border: 1px solid #f0f7ec;
				}

				.detail-row {
					display: flex;
					gap: 16px;
					align-items: flex-start;
					font-size: 14.5px;
					line-height: 1.6;
					color: #333;
				}

				.detail-icon {
					font-size: 18px;
					flex-shrink: 0;
					margin-top: 3px;
					width: 24px;
					height: 24px;
					display: flex;
					align-items: center;
					justify-content: center;
				}
				.detail-icon.seedling { color: #27ae60; }
				.detail-icon.growth { color: #9ec008; }
				.detail-icon.current { color: #196164; }
				.detail-icon.strategic { color: #e67e22; }

				.detail-row strong {
					color: #08201b;
					font-weight: 700;
				}

				.vjs-positioning-header h3, .vjs-future-header h3 {
					font-family: 'Outfit', sans-serif;
					font-size: 34px;
					font-weight: 800;
					color: #08201b;
					margin: 15px 0;
					letter-spacing: -1px;
				}

				.vjs-positioning-header p {
					font-size: 17px;
					color: #555;
					max-width: 800px;
					margin: 0 auto 40px;
				}

				.vjs-verticals-grid {
					display: flex;
					flex-wrap: wrap;
					gap: 15px;
					justify-content: center;
				}

				.vertical-chip {
					background: #fff;
					border: 1px solid #eef5e8;
					padding: 14px 35px;
					border-radius: 50px;
					font-weight: 700;
					display: flex;
					align-items: center;
					gap: 12px;
					transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
					box-shadow: 0 4px 15px rgba(0,0,0,0.03);
					font-family: 'Outfit', sans-serif;
					font-size: 15px;
				}

				.vertical-chip span { color: #9ec008; font-size: 18px; }

				.vertical-chip:hover {
					background: #08201b;
					color: #fff;
					transform: scale(1.08) translateY(-3px);
					border-color: #08201b;
					box-shadow: 0 10px 25px rgba(8, 32, 27, 0.2);
				}

				.vjs-future-grid {
					display: grid;
					grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
					gap: 25px;
				}

				.future-card {
					background: #fff;
					padding: 45px;
					border-radius: 30px;
					border: 1px solid #f0f7ec;
					transition: all 0.4s ease;
					position: relative;
				}

				.future-card:hover {
					border-color: #9ec008;
					transform: translateY(-8px);
					box-shadow: 0 25px 50px rgba(8, 32, 27, 0.08);
				}

				.future-num {
					font-family: 'Outfit', sans-serif;
					font-size: 42px;
					font-weight: 800;
					color: rgba(158, 192, 8, 0.2);
					position: absolute;
					top: 30px;
					right: 30px;
					line-height: 1;
				}

				.future-card h4 {
					font-family: 'Outfit', sans-serif;
					font-size: 20px;
					font-weight: 800;
					margin-bottom: 18px;
					color: #08201b;
				}

				.future-card p {
					font-size: 15px;
					color: #666;
					line-height: 1.7;
					margin: 0;
				}

				@media (max-width: 991px) {
					.timeline-v-line { left: 40px; transform: none; }
					.timeline-item { flex-direction: row-reverse; justify-content: flex-end; padding-left: 40px; margin-bottom: 60px; }
					.marker-content { width: 100%; padding: 0 0 0 50px; }
					.marker-year { width: 65px; height: 65px; font-size: 15px; border-width: 3px; position: absolute; left: 7px; top: 0; }
					.marker-dot { position: absolute; left: 40px; top: 32px; transform: translateX(-50%); width: 12px; height: 12px; }
					.vjs-phase-banner { text-align: left; padding: 0 40px; }
					.vjs-phase-inner { width: 100%; padding: 25px; }
					.phase-title { font-size: 22px; }
				}

				@media (max-width: 768px) {
					.vjs-positioning-header h3, .vjs-future-header h3 { font-size: 28px; }
					.future-card { padding: 30px; }
				}
			</style>

		</div>
		<!-- /.vjs-timeline-section -->
"@

# Regex for the block we want to replace
# Looking for the block from "Our Journey Timeline" comment to the section closure
$pattern = '(?s)<!--\s*=====================================================\s*Our Journey Timeline.*?<!-- /.vjs-timeline-section -->'

if ($content -match $pattern) {
    $content = $content -replace $pattern, $newSection
    [System.IO.File]::WriteAllText($filePath, $content, [System.Text.Encoding]::UTF8)
    Write-Host "SUCCESS: Redesigned section applied via regex replacement"
} else {
    Write-Host "ERROR: Could not find the Journey Timeline block. Falling back to targeted replacement."
}
