from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
import os
import stat
import requests
from zipfile import ZipFile

URL = "https://chromedriver.storage.googleapis.com/104.0.5112.79/chromedriver_linux64.zip"
response = requests.get(URL)
open("/app/webdriver", "wb").write(response.content)

ZipFile("webdriver", "r").extractall()

os.system("chmod a+rx /app/chromedriver")

options = Options()
option = webdriver.ChromeOptions()

options.headless = True
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(executable_path=r'/app/chromedriver',options=option)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.get('https://aternos.org/server')

# log in
text_area = driver.find_element_by_id('user')
text_area.send_keys(os.environ['uname'])
time.sleep(3)
text_area = driver.find_element_by_id('password')
text_area.send_keys(os.environ['pswd'])
time.sleep(3)
login = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[4]/div[3]/div[4]')
login.click()
time.sleep(3)
driver.get('https://aternos.org/server')
time.sleep(3)

# accept cookie privacy prompt
cookieaccept = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/div[2]/div[2]')
cookieaccept.click()

# select server
select = driver.find_element_by_xpath('/html/body/div/main/section/div/div[2]/div/div[2]')
select.click()

# wait for the page to load
time.sleep(5)

# click start button
start = driver.find_element_by_xpath('/html/body/div[2]/main/section/div[3]/div[4]/div[1]')
start.click()

time.sleep(5)

# click cancel
cancel = driver.find_element_by_xpath('/html/body/div[2]/main/div/div/div/main/div/a[2]')
cancel.click()

time.sleep(3)

#close chromium and python
os.system("killall chromium")
sys.exit()
