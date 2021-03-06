from urlparse import urljoin

from lxml.html import fromstring
import requests

def scrape_year_page(url):
    response = requests.get(url)

    doc = fromstring(response.content)

    data = {}

    # Year
    data['year'] = doc.cssselect('h2')[0].text

    # Registered runners
    cell = doc.cssselect('#registered')[0]
    data['registered_runners'] = int(cell.text.replace(',', ''))

    # Finished runners
    cell = doc.cssselect('#finished')[0]
    data['finished_runners'] = int(cell.text.replace(',', ''))

    # Wind
    cells = doc.cssselect('marquee')
    wind = cells[0].text

    if wind == 'calm':
        data['wind_dir'] = None
        data['wind_speed'] = 0
    else:  
        direction, speed = wind.split()

        data['wind_dir'] = direction
        data['wind_speed'] = int(speed)

    return data

BASE_URL = 'http://169.254.135.23/'
EXAMPLE_PATH = '1977.asp.html'
url = urljoin(BASE_URL, EXAMPLE_PATH)
print scrape_year_page(url)

