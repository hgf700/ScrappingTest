import requests
from bs4 import BeautifulSoup

# Create a session to persist cookies and login data
session = requests.Session()

# URL of the login page
login_url = 'https://www.scrapethissite.com/login/'

# Get the login page to retrieve CSRF token or other hidden fields
login_page = session.get(login_url)
soup = BeautifulSoup(login_page.text, 'html.parser')

login_data = {
    'username': 'username',
    'password': 'password'
}

# Proceed with the login
login_response = session.post(login_url, data=login_data)

if login_response.ok:
    print("Logged in successfully!")
else:
    print("Login failed")
