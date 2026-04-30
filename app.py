from flask import Flask, render_template

app = Flask(__name__)

# Primary Routes
@app.route('/')
def home():
    return render_template('index-2.html')

@app.route('/index-2.html')
def index2():
    return render_template('index-2.html')

@app.route('/about-us-v1.html')
def about_us_v1():
    return render_template('about-us-v1.html')

@app.route('/about-us-v2.html')
def about_us_v2():
    return render_template('about-us-v2.html')

@app.route('/sustainability.html')
def sustainability():
    return render_template('sustainability.html')

@app.route('/blog-v1.html')
def blog_v1():
    return render_template('blog-v1.html')

@app.route('/media-release.html')
def media_release():
    return render_template('media-release.html')

@app.route('/media-kit.html')
def media_kit():
    return render_template('media-kit.html')

# Businesses Routes
@app.route('/it-consulting.html')
def it_consulting():
    return render_template('it-consulting.html')

@app.route('/data-centers-hosting.html')
def data_centers_hosting():
    return render_template('data-centers-hosting.html')

@app.route('/it-training.html')
def it_training():
    return render_template('it-training.html')

@app.route('/yoga-wellness.html')
def yoga_wellness():
    return render_template('yoga-wellness.html')

@app.route('/green-energy.html')
def green_energy():
    return render_template('green-energy.html')

@app.route('/export-import.html')
def export_import():
    return render_template('export-import.html')

@app.route('/plantations.html')
def plantations():
    return render_template('plantations.html')

@app.route('/property-services.html')
def property_services():
    return render_template('property-services.html')

@app.route('/logistics-services.html')
def logistics_services():
    return render_template('logistics-services.html')

@app.route('/travel-rentals.html')
def travel_rentals():
    return render_template('travel-rentals.html')

# Sustainability Details
@app.route('/digital-transformation-sustainability.html')
def digital_transformation_sustainability():
    return render_template('digital-transformation-sustainability.html')

@app.route('/cloud-infrastructure-sustainability.html')
def cloud_infrastructure_sustainability():
    return render_template('cloud-infrastructure-sustainability.html')

@app.route('/renewable-energy-solutions.html')
def renewable_energy_solutions():
    return render_template('renewable-energy-solutions.html')

@app.route('/logistics-trade-sustainability.html')
def logistics_trade_sustainability():
    return render_template('logistics-trade-sustainability.html')

@app.route('/education-skill-sustainability.html')
def education_skill_sustainability():
    return render_template('education-skill-sustainability.html')

@app.route('/tree-plantation-sustainability.html')
def tree_plantation_sustainability():
    return render_template('tree-plantation-sustainability.html')

@app.route('/eco-tech-solutions.html')
def eco_tech_solutions():
    return render_template('eco-tech-solutions.html')

@app.route('/renewable-energy-adoption.html')
def renewable_energy_adoption():
    return render_template('renewable-energy-adoption.html')

@app.route('/sustainable-business-practices.html')
def sustainable_business_practices():
    return render_template('sustainable-business-practices.html')

@app.route('/educational-support-csr.html')
def educational_support_csr():
    return render_template('educational-support-csr.html')

@app.route('/financial-material-aid.html')
def financial_material_aid():
    return render_template('financial-material-aid.html')

@app.route('/skill-building-youth.html')
def skill_building_youth():
    return render_template('skill-building-youth.html')

@app.route('/rural-semi-urban-engagement.html')
def rural_semi_urban_engagement():
    return render_template('rural-semi-urban-engagement.html')

@app.route('/awareness-programs-community.html')
def awareness_programs_community():
    return render_template('awareness-programs-community.html')

@app.route('/local-infrastructure-support.html')
def local_infrastructure_support():
    return render_template('local-infrastructure-support.html')

@app.route('/service-v1.html')
def service_v1():
    return render_template('service-v1.html')

# Catch-all for any other .html files in templates
@app.route('/<path:filename>')
def catch_all(filename):
    if filename.endswith('.html'):
        return render_template(filename)
    return render_template('index-2.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
