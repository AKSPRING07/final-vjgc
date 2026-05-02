from flask import Flask, render_template, request, abort
import os

app = Flask(__name__)

# Primary Routes
@app.route('/')
def home():
    return render_template('index-2.html')

@app.route('/<path:path>')
def dynamic_route(path):
    # 1. Try exact path (e.g. index-2.html)
    if os.path.exists(os.path.join(app.template_folder, path)):
        return render_template(path)
    
    # 2. Try path + .html (e.g. it-training -> it-training.html)
    html_path = f"{path}.html"
    if os.path.exists(os.path.join(app.template_folder, html_path)):
        return render_template(html_path)
    
    # 3. Handle special cases or default to home
    if path == 'index' or path == 'home':
        return render_template('index-2.html')
    
    # If nothing found, return home or 404
    return render_template('index-2.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
