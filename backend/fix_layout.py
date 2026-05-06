import os
import re

TEMPLATES_DIR = r'c:\Users\ELCOT\vjs-website-\templates'

def fix_endifs(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Fix At a Glance
    # We want to move {% endif %} from inside the first card to the very end of the row.
    # The row ends with `</div>` right before `</div>\n\t\t\t</section>`
    
    # Let's find the At a Glance section
    glance_pattern = re.compile(r'(<section class="glance-section-v3">.*?)({% else %}.*?)(</section>)', re.DOTALL)
    
    def glance_replacer(match):
        prefix = match.group(1)
        else_block = match.group(2)
        suffix = match.group(3)
        
        # Remove any {% endif %} inside the else_block
        clean_else = else_block.replace('{% endif %}', '')
        
        # Add {% endif %} right before the last closing </div> of the row.
        # The else_block contains the hardcoded cards and ends with </div> (for the row) and </div> (for container).
        # We can just put {% endif %} before the </div>\n\t\t\t\t</div> that closes the row and container.
        # Actually, simpler: replace the whole At a Glance else block with just the CMS loop, dropping the fallback?
        # Let's just drop the fallback to make it clean, since DB has the data!
        return prefix + suffix

    # Actually, if we just drop the else block, the HTML will be pristine.
    # Let's drop the `{% else %}` and all its contents, and just close the `{% if %}`.
    
    # Wait, let's just find `{% else %}` ... `{% endif %}` and the extra cards and remove them?
    # No, the extra cards are OUTSIDE the `{% endif %}`! That's the problem.
    pass

# A safer approach: replace the entire row content with just the CMS loop.
def wipe_and_replace_row(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # At a Glance
    glance_row = r'(<h2 class="section-title">At a Glance.</h2>\s*<div class="row justify-content-center g-4">).*?(</div>\s*</div>\s*</section>)'
    
    def glance_rep(match):
        return match.group(1) + """
						{% if cms['At a Glance'] and cms['At a Glance'].content %}
							{% for card in cms['At a Glance'].content %}
							<div class="col-lg-4 col-md-6 d-flex wow fadeInUp" data-wow-delay="{{ loop.index0 * 0.1 }}s">
								<div class="vjs-glance-card-v3">
									<div class="img-wrap"><img src="{{ card.image_url }}" alt="{{ card.title }}" style="width:100%;height:100%;object-fit:cover;"></div>
									<div class="content">
										<h4 class="card-title">{{ card.title }}</h4>
										<p class="card-desc">{{ card.description }}</p>
									</div>
								</div>
							</div>
							{% endfor %}
						{% endif %}
					""" + match.group(2)

    content = re.sub(glance_row, glance_rep, content, flags=re.DOTALL)
    
    # Our Business
    # The title varies: "Our Learning Programs", "Our Energy Businesses", etc.
    # So we match the section class and the row.
    biz_row = r'(<section class="biz-section-v2">.*?<div class="row g-4">).*?(</div>\s*</div>\s*</section>)'
    
    def biz_rep(match):
        return match.group(1) + """
						{% if cms['Our Business'] and cms['Our Business'].content %}
							{% for card in cms['Our Business'].content %}
							<div class="col-lg-3 col-md-6 d-flex wow fadeInUp" data-wow-delay="{{ loop.index0 * 0.1 }}s">
								<a href="#" class="vjs-biz-card-v2">
									<div class="img-wrap"><img src="{{ card.image_url }}" alt="{{ card.title }}"></div>
									<div class="content">
										<h4 class="card-title">{{ card.title }}</h4>
										<p class="card-desc">{{ card.description }}</p>
									</div>
								</a>
							</div>
							{% endfor %}
						{% endif %}
					""" + match.group(2)

    content = re.sub(biz_row, biz_rep, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


files = ['plantations.html', 'it-training.html', 'yoga-wellness.html', 'property-services.html', 'green-energy.html', 'logistics-services.html', 'export-import.html', 'data-centers-hosting.html', 'it-consulting.html', 'travel-rentals.html']

for f in files:
    wipe_and_replace_row(os.path.join(TEMPLATES_DIR, f))
    print(f"Fixed {f}")
