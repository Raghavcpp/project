# import datetime

# print(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))

import time
from selenium import webdriver

chrome = webdriver.Chrome()
chrome.get("https://www.google.com")
time.sleep(2)
chrome.save_screenshot(f'Screenshots/tiktok/{time.strftime("%Y%m%d-%H%M%S")}.png')
