import sys
import requests
from bs4 import BeautifulSoup as bs
from lxml import etree
from datetime_controller import is_within_next_10_days
from email_controller import format_message, send_email
from classes import Match


headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

url = "https://www.espn.com.ar/futbol/equipo/calendario/_/id/5/boca-juniors"


response = requests.get(url, headers=headers)
soup = bs(response.content, features='html.parser')
dom = etree.HTML(str(soup))

lista_de_fechas = dom.xpath('//tbody[@class="Table__TBODY"]//tr[contains(@class, "Table__TR")]')

list_of_matches = []

for index, element in enumerate(lista_de_fechas):
    # Obtain all text elements from xpath
    lista = element.xpath('.//td//text()')
    # Create new object
    match = Match(*lista)
    list_of_matches.append(match)

# Check if the next match happens during the next ten days
this_week_matches = []
for m in list_of_matches:
    if is_within_next_10_days(m.date_obj) and m.local == 'Boca Juniors':
        this_week_matches.append(m)

if this_week_matches:
    # Format message
    message = format_message(this_week_matches)
    # Send Email
    send_email(message=message)