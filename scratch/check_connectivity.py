
import urllib.request
import urllib.error

def check_url(url):
    try:
        response = urllib.request.urlopen(url, timeout=5)
        print(f"URL: {url} - Status: {response.status}")
    except urllib.error.HTTPError as e:
        print(f"URL: {url} - Status: {e.code}")
    except Exception as e:
        print(f"URL: {url} - Error: {e}")

if __name__ == "__main__":
    check_url("http://localhost:3000/dashboard/crm/")
    check_url("http://localhost:5000/api/docs")
    check_url("http://localhost:5000/docs")
    check_url("http://localhost:5000/")
