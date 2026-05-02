import os

replacements = {
    "â€™": "'",
    "â€”": "—",
    "Ã¢â‚¬â€”": "—",
    "Ã¢â‚¬Å“": "“",
    "Ã¢â‚¬Â": "”",
    "Ã¢â€ â€™": "→",
    "Ã°Å¸â€ Â¥": "🔥",
    "Ã°Å¸â€™Â¡": "💡",
    "Ã°Å¸Å¡\x80": "🚀",
    "Ã¢â‚¬": "—", # catch-all for partial em-dash
}

def fix_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        new_content = content
        for search, replace in replacements.items():
            new_content = new_content.replace(search, replace)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed: {filepath}")
    except Exception as e:
        print(f"Error fixing {filepath}: {e}")

# Process templates
template_dir = r"c:\Users\Admin\.gemini\antigravity\scratch\final-vjgc\templates"
for root, dirs, files in os.walk(template_dir):
    for file in files:
        if file.endswith(".html"):
            fix_file(os.path.join(root, file))

# Process CSS
css_dir = r"c:\Users\Admin\.gemini\antigravity\scratch\final-vjgc\static\css"
for root, dirs, files in os.walk(css_dir):
    for file in files:
        if file.endswith(".css"):
            fix_file(os.path.join(root, file))

print("Cleanup complete.")
