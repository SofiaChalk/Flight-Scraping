from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import getpass
import time
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
# options.add_argument('--headless')

# Path where chromedriver is saved
chromedriver = 'C:\\Users\\' + user + '\\Documents\\Python\\Python Scripts\\Flight Scrapping\\chromedriver.exe'

url = 'https://www.kayak.co.uk/flights'

driver = webdriver.Chrome(executable_path=chromedriver, options=options)
driver.get(url)
time.sleep(5)

# Click No thanks on cookies pop-up
try:
    driver.find_element_by_xpath('/html/body/div[37]/div/div[3]/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/button').click()
except:
    pass
time.sleep(5)

# Origin Airport
# Click on the origin airport cell
driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[1]/div/div/div[1]/div/div/section[2]/div/div/div[2]/form[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div/div[1]').click()
# Delete any origin location that might be there already
try:
    driver.switch_to.frame('__cmpLocator')
    driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[1]/div[2]/div/div[2]/button/svg/use//svg/path').click()
except:
    pass
# Type the origin airport
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[1]/div[3]/input').send_keys(from_airport)
# Click on empty space
driver.find_element_by_xpath("//body").click()
time.sleep(3)

# Destination airport
# Click on the destination airport cell
driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[1]/div/div/div[1]/div/div/section[2]/div/div/div[2]/form[1]/div[1]/div/div[1]/div/div[3]/div/div/div').click()
# Type the origin airport
driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[1]/div[3]/input').send_keys(to_airport)
# Click on empty space
driver.find_element_by_xpath("//body").click()

# Date
# Click on the departure date cell
driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[1]/div/div/div[1]/div/div/section[2]/div/div/div[2]/form[1]/div[1]/div/div[1]/div/div[4]/div/div[1]/div/div/div[1]').click()
# Type date
driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[1]/div/div[2]/div[1]').send_keys(departure_date)
# Type date for return date cell
driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[3]/div[1]/div/div[2]/div[1]').send_keys(return_date)
# Click on empty space
driver.find_element_by_xpath("//body").click()

# Click on Search button
driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[1]/div/div/div[1]/div/div/section[2]/div/div/div[2]/form[1]/div[1]/div/div[2]/button/span/span[1]/svg').click()

# Finds the username of the PC in use
user = getpass.getuser()

# Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--headless')
agents = ["Firefox/66.0.3","Chrome/73.0.3683.68","Edge/16.16299"]
options.add_argument('--user-agent=' + agents[(requests%len(agents))] + '"')
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome("chromedriver.exe", options=chrome_options, desired_capabilities=chrome_options.to_capabilities())
driver.implicitly_wait(20)
driver.get(url)