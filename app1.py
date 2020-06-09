import requests
import getpass
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup

from_airport = 'London'
to_airport = 'Athens'
departure_date = '05/07/2020'
return_date = '20/08/2020'

# Finds the username of the PC in use
user = getpass.getuser()

# Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

# Path where chromedriver is saved
chromedriver = 'C:\\Users\\schalkiadaki\\Downloads\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chromedriver, options=options)
url ='https://www.momondo.co.uk/flight-search/LON-ATH/2020-07-08/2020-07-15?sort=bestflight_a&fs=stops=0'
url = 'https://www.kayak.com/flights/LON-ATH/2020-07-08/2020-07-15?sort=bestflight_a&fs=stops=0'

# Try to  to fetch the content from the given url
response = requests.get(url)
# Check if the status code is 200 = successful
if not response.status_code == 200:
    print('HTTP error', response.status_code)
else:
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    dep_time = soup.find_all('span', class_= 'depart-time base-time')
    arr_time = soup.find_all('span', attrs={'class': 'arrival-time base-time'})
    duration = soup.find_all('span', attrs={'class': 'section duration allow-multi-modal-icons'})
    deptime = []
    for div in dep_time:
        deptime.append(div.getText()[:-1])
s = driver.page_source
s = response.content
from urllib.request import urlopen
page = urllib.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
driver = webdriver.Chrome()
html_source_code = driver.execute_script("return document.body.innerHTML;")
html_soup: BeautifulSoup = BeautifulSoup(html_source_code, 'html.parser')