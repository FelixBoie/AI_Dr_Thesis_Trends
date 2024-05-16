
import urllib.request

def crawl(url):
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                return response.read().decode('utf-8')
            else:
                print("Fehler beim Abrufen der Seite:", response.status)
    except Exception as e:
        print("Fehler:", e)

# Beispiel-URL
url = "https://www.dart-europe.org/browse-list.php?country=Germany"

html_content = crawl(url)
if html_content:
    print(html_content)
