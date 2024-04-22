import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep
import pyautogui
from selenium.webdriver.support.ui import Select
import pandas as pd
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

email = "oenvgw735374@hotmail.com"
email_pass = "jfNES2gQ6"
fa_code = "UDKTM3SCQD4FAYXETJDEPSG2VRJAODX4"
temp_mail="canan34_1994@hotmail.com"
temp_pass="mZO459or73"


driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=19&ct=1704704863&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fcobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26nlp%3d1%26deeplink%3dowa%252f0%252f%253fstate%253d1%26redirectTo%3daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC8%26RpsCsrfState%3dc8fb4362-e2f6-ef73-b652-f904fa47b9fc&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c")
driver.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]').send_keys(email)
sleep(2)
driver.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div').click()
sleep(2)

# sleep(200)
driver.find_element(By.ID, 'i0118').send_keys(email_pass)
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div').click()
sleep(5)
try:
    driver.find_element(By.ID, 'EmailAddress').send_keys(temp_mail)
    sleep(2)
    

except NoSuchElementException:
    pass


sleep(2000)