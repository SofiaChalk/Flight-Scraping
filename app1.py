import requests
from bs4 import BeautifulSoup
url ='https://www.kayak.co.uk/flights/LON-ATH/2020-07-08/2020-07-15?sort=bestflight_a&fs=stops=0'

try:
    # Try to  to fetch the content from the given url
    response = requests.get(url)
    # Check if the status code is 200 = successful
    if not response.status_code == 200:
        print('HTTP error', response.status_code)
    else:
        txt = response.text
        soup = BeautifulSoup(driver.page_source, 'lxml')
except:
    print('Something went wrong with requests.get')

