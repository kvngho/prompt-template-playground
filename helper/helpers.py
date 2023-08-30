import requests
from bs4 import BeautifulSoup

def test_crwal_func(urls) -> str:
    result = []
    for url in urls.split('\n'):
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        extracted_text = soup.get_text(strip=True)
        result.append(extracted_text)
    return "\n\n".join(result)
