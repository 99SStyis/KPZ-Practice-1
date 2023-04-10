from bs4 import BeautifulSoup
import requests

def parse_ukd_data():
    url = "https://ukd.edu.ua/specialnosti-ta-osvitni-programi"
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    specialities = soup.find_all("div", class_="views-field views-field-title")
    for speciality in specialities:
        print(speciality.text.strip())
