import requests
from bs4 import BeautifulSoup

# URL strony, którą chcesz scrapować
url = 'https://www.scrapethissite.com/pages/simple/'

# Wysyłanie żądania HTTP do serwera
response = requests.get(url)

# Sprawdzenie statusu odpowiedzi
if response.status_code == 200:
    # Tworzenie obiektu BeautifulSoup do parsowania HTML
    soup = BeautifulSoup(response.content, 'lxml')

    # Znajdowanie wszystkich elementów div z klasą country
    countries = soup.find_all('div', class_='country')
    #print(countries)

for country in countries:
    country_name = country.find('h3', class_='country-name').text.strip()
    country_population = country.find('span', class_='country-population').text.strip()  
    country_capitol = country.find('span', class_='country-capital').text.strip()  
    country_area = country.find('span', class_='country-area').text.strip()  

    print(f"Nazwa kraju: {country_name}")
    print(f"Stolica: {country_capitol}")
    print(f"Populacja: {country_population}")
    print(f"Powierzchnia (km²): {country_area}")
    print("-" * 40)  


    

else:
    print("Błąd: Nie udało się pobrać strony")