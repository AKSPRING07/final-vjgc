import requests
import os

templates_dir = r"c:\Users\Admin\vjs-website-\templates"
base_url = "http://127.0.0.1:5000/"

files = [f for f in os.listdir(templates_dir) if f.endswith('.html')]
results = []

print(f"Testing {len(files)} pages...")

for file in files:
    url = f"{base_url}{file}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            results.append((file, "PASS"))
        else:
            results.append((file, f"FAIL ({response.status_code})"))
    except Exception as e:
        results.append((file, f"ERROR ({str(e)})"))

failed = [r for r in results if r[1] != "PASS"]
if not failed:
    print("ALL PAGES PASSED (200 OK)")
else:
    print(f"FAILED PAGES: {len(failed)}")
    for f in failed:
        print(f" - {f[0]}: {f[1]}")
