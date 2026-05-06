import codecs
try:
    with codecs.open('scratch/old_index-2.html', 'r', 'utf-16') as f:
        content = f.read()
    start = content.find('<div class="footer-style-one')
    if start == -1:
        start = content.find('<footer')
    if start != -1:
        print(content[start:start+10000])
    else:
        print("Footer not found")
except Exception as e:
    print(f"Error: {e}")
