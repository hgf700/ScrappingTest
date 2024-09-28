import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://www.scrapethissite.com/pages/advanced/'

# Spoofing nagłówki, aby wyglądać jak przeglądarka
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "utf-8",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Znajdź link po tekście "Spoofing Headers"
link_tag = soup.find('a', string='Spoofing Headers')

if link_tag:
    link_tag_url = link_tag.get('href')  # Pobierz URL z atrybutu href
    joinlink_tag_url = urljoin(url, link_tag_url)

    # Pobierz nową stronę, na którą prowadzi link "Spoofing Headers"
    spoofing_response = requests.get(joinlink_tag_url, headers=headers)

    spoof_soup = BeautifulSoup(spoofing_response.text, 'html.parser')
    
    # Znajdź tekst z odpowiedniego diva
    spoof = spoof_soup.find('div', class_='col-md-4 col-md-offset-4')
    
    if spoof:
        print(spoof.text.strip())  # Wyświetl tekst bez zbędnych białych znaków
    else:
        print("Nie znaleziono odpowiedniego div'a na stronie.")
else:
    print("Nie znaleziono linku 'Spoofing Headers'.")
