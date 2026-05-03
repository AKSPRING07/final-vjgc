import os
import re

# Directory containing the templates
directory = 'templates'

# Patterns to match the navbar link for Mission & Vision
# We target the link that points to 'about-us-v1' and has the specific text variations.
patterns = [
    # Pattern 1: Simple single line with &
    (re.compile(r'(<a\s+href="{{ url_for\(\'dynamic_route\',\s+path=\'about-us-v1\'\)\s*}}">)\s*Mission\s+&\s+Vision\s*(</a>)', re.IGNORECASE), r'\1Our Journey\2'),
    # Pattern 2: Simple single line with 'and'
    (re.compile(r'(<a\s+href="{{ url_for\(\'dynamic_route\',\s+path=\'about-us-v1\'\)\s*}}">)\s*Mission\s+and\s+Vision\s*(</a>)', re.IGNORECASE), r'\1Our Journey\2'),
    # Pattern 3: With 'Our' prefix
    (re.compile(r'(<a\s+href="{{ url_for\(\'dynamic_route\',\s+path=\'about-us-v1\'\)\s*}}">)\s*Our\s+Mission\s+and\s+Vision\s*(</a>)', re.IGNORECASE), r'\1Our Journey\2'),
    # Pattern 4: Split line with newline after '&'
    (re.compile(r'(<a\s+href="{{ url_for\(\'dynamic_route\',\s+path=\'about-us-v1\'\)\s*}}">)\s*Mission\s+&\s*\n\s*Vision\s*(</a>)', re.IGNORECASE), r'\1Our Journey\2'),
    # Pattern 5: Split line with newline after 'Our'
    (re.compile(r'(<a\s+href="{{ url_for\(\'dynamic_route\',\s+path=\'about-us-v1\'\)\s*}}">)\s*Our\s*\n\s*Mission\s+and\s+Vision\s*(</a>)', re.IGNORECASE), r'\1Our Journey\2'),
]

files_updated = 0

if not os.path.exists(directory):
    print(f"Directory {directory} not found.")
    exit(1)

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            for pattern, replacement in patterns:
                new_content = pattern.sub(replacement, new_content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")
                files_updated += 1
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print(f"Total files updated: {files_updated}")
