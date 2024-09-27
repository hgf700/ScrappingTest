import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

# URL strony, którą chcesz scrapować
url = 'https://www.scrapethissite.com/pages/forms/'

# Wysyłanie żądania HTTP do serwera
response = requests.get(url)

# Sprawdzenie statusu odpowiedzi
if response.status_code == 200:
    # Tworzenie obiektu BeautifulSoup do parsowania HTML
    soup = BeautifulSoup(response.content, 'lxml')

    # Znajdowanie wszystkich elementów table z klasą table
    teams = soup.find_all('tr', class_='team')

    # Tworzenie tabeli za pomocą PrettyTable
    table = PrettyTable()
    table.field_names = ["Team Name", "Year", "Wins", "Losses", "OT Losses", "Win %", "Goals For", "Goals Against", "+/-"]

    # Iterowanie po drużynach
    for team in teams:
        team_name = team.find('td', class_='name').text.strip()
        team_year = team.find('td', class_='year').text.strip()
        team_wins = team.find('td', class_='wins').text.strip()
        team_loses = team.find('td', class_='losses').text.strip()
        team_otloses = team.find('td', class_='ot-losses').text.strip()
        team_pct = team.find('td', class_='pct').text.strip()
        team_gf = team.find('td', class_='gf').text.strip()
        team_ga = team.find('td', class_='ga').text.strip()
        team_diff = team.find('td', class_='diff').text.strip()

        # Dodawanie wiersza do tabeli
        table.add_row([team_name, team_year, team_wins, team_loses, team_otloses, team_pct, team_gf, team_ga, team_diff])

    # Wyświetlanie tabeli
    print(table)

else:
    print("Błąd: Nie udało się pobrać strony")
