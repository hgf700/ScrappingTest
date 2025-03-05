import requests
from prettytable import PrettyTable

# URL for the site (use the full URL of the page you're scraping)
url = 'https://scrapethissite.com/pages/ajax-javascript/'  # Example URL

# Parameters for the AJAX request
params = {
    'ajax': 'true',
    'year': '2015'  # Change year as needed
}

table = PrettyTable()
table.field_names = ["Title","Nominations","Awards","Best Picture"]

# Make the AJAX request
response = requests.get(url, params=params)

# Parse the JSON response
films = response.json()

# Extract and print films information
for film in films:
    title = film.get('title')
    nominations = film.get('nominations')
    awards = film.get('awards')
    best_picture = film.get('best_picture')
    table.add_row([title,nominations,awards,best_picture])
    
print(table)