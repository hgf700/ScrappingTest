import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL strony, z której pobierasz iframe
url = 'https://www.scrapethissite.com/pages/frames/'
# Pobranie głównej strony
response = requests.get(url)
if response.status_code == 200:
    # Parsowanie zawartości strony
    soup = BeautifulSoup(response.content, 'html.parser')
    # Znalezienie pierwszego iframe
    iframe = soup.find('iframe')
    if iframe:
        # Pobranie URL pierwszego iframe
        iframe_url = iframe['src']
        full_iframe_url = urljoin(url, iframe_url)
        
        # Pobranie zawartości pierwszego iframe
        iframe_response = requests.get(full_iframe_url)
        if iframe_response.status_code == 200:
            iframe_soup = BeautifulSoup(iframe_response.content, 'html.parser')
            
            # Znalezienie sekcji z kartą żółwia (np. Cheloniidae)
            turtle_cards = iframe_soup.find_all('div', class_='turtle-family-card')
            
            for card in turtle_cards:
                # Wyświetlenie nazwy rodziny żółwia
                family_name = card.find('h3', class_='family-name').text
                print(f"Rodzina żółwia: {family_name}")
                
                # Pobranie URL przycisku "Learn more"
                learn_more_link = card.find('a', class_='btn btn-default btn-xs')
                learn_more_url = learn_more_link['href']
                full_learn_more_url = urljoin(full_iframe_url, learn_more_url)
                
                # Pobranie zawartości strony z informacjami o żółwiu
                learn_more_response = requests.get(full_learn_more_url)
                if learn_more_response.status_code == 200:
                    learn_more_soup = BeautifulSoup(learn_more_response.content, 'html.parser')
                    
                    # Znalezienie opisu żółwia
                    turtle_info = learn_more_soup.find('p', class_='lead').text
                    print(f"Opis: {turtle_info}")
                else:
                    print(f"Błąd podczas pobierania szczegółów żółwia: {learn_more_response.status_code}")
        else:
            print(f"Błąd podczas pobierania iframe: {iframe_response.status_code}")
    else:
        print("Nie znaleziono iframe.")
else:
    print(f"Błąd podczas pobierania strony: {response.status_code}")