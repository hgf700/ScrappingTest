import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

# URL strony do scrapowania
url = 'https://www.scrapethissite.com/pages/forms/'

# Wysyłanie żądania HTTP do serwera
response = requests.get(url)

# Sprawdzenie, czy żądanie zakończyło się sukcesem
if response.status_code == 200:
    # Tworzenie obiektu BeautifulSoup do parsowania HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Znajdowanie wszystkich wierszy z klasą "team"
    teams = soup.find_all('tr', class_='team')

    # Tworzenie tabeli za pomocą PrettyTable
    table = PrettyTable()
    table.field_names = ["Team Name", "Year", "Wins", "Losses", "OT Losses", "Win %", "Goals For", "Goals Against", "+/-"]

    # Iterowanie po drużynach
    for team in teams:
        team_name = team.find('td', class_='name')
        team_year = team.find('td', class_='year')
        team_wins = team.find('td', class_='wins')
        team_loses = team.find('td', class_='losses')
        team_otloses = team.find('td', class_='ot-losses')
        team_pct = team.find('td', class_='pct')
        team_gf = team.find('td', class_='gf')
        team_ga = team.find('td', class_='ga')
        team_diff = team.find('td', class_='diff')

        # Sprawdzamy, czy element istnieje, aby uniknąć błędów
        row = [
            team_name.text.strip() if team_name else "N/A",
            team_year.text.strip() if team_year else "N/A",
            team_wins.text.strip() if team_wins else "N/A",
            team_loses.text.strip() if team_loses else "N/A",
            team_otloses.text.strip() if team_otloses else "N/A",
            team_pct.text.strip() if team_pct else "N/A",
            team_gf.text.strip() if team_gf else "N/A",
            team_ga.text.strip() if team_ga else "N/A",
            team_diff.text.strip() if team_diff else "N/A",
        ]

        # Dodanie wiersza do tabeli
        table.add_row(row)

    # Wyświetlanie tabeli
    print(table)

else:
    print(f"Błąd: Nie udało się pobrać strony (status: {response.status_code})")
