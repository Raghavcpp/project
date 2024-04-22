from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import pyautogui
import pickle
from selenium.webdriver.support.ui import Select
import pandas as pd
import os


# username, password = "vivek.ajath", "Ajath@123"

class FacebookBot:
    comments = ["hello"]
    # driver.maximize_window()
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()

        self.driver.get('https://www.facebook.com/')
        sleep(1)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input').send_keys(username)
        sleep(1)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input').send_keys(password)
        sleep(1)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
        sleep(5)

        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[2]/div').click()
        sleep(3)

        self.driver.find_element(By.XPATH, value='/html/body/div[3]/div[2]/div/div/div/div[2]/ul/li[2]/div/div[1]').click()
        sleep(3)

        self.driver.find_element(By.XPATH, value='/html/body/div[3]/div[2]/div/div/div/div[2]/ul/li[2]/div/div[2]/ul/li/div/div/div[2]/button').click()
        sleep(3)

        self.driver.find_element(By.XPATH, value='/html/body/div[3]/div[2]/div/div/div/div/div/div/div[3]/span[2]/div/div').click()
        sleep(3)

        self.driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div[2]/span/input').send_keys("oenvgw735374@hotmail.com")
        sleep(3)
        
        self.driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[4]/div/div/span/input').send_keys("oenvgw735374@hotmail.com")
        sleep(3)

        self.driver.find_element(By.XPATH, value='/html/body/div[4]/div[2]/div/div/div/div/div/div/div[3]/span[2]/div/div[2]').click()
        sleep(3)

    def email_check(self, email, password):
        self.driver.execute_script("window.open('');") 
        self.driver.switch_to.window(self.driver.window_handles[1]) 
        self.driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=19&ct=1704704863&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fcobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26nlp%3d1%26deeplink%3dowa%252f0%252f%253fstate%253d1%26redirectTo%3daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC8%26RpsCsrfState%3dc8fb4362-e2f6-ef73-b652-f904fa47b9fc&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c')
        sleep(3)

        self.driver.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]').send_keys(email)
        sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div').click()
        sleep(2)

        # sleep(200)
        self.driver.find_element(By.ID, 'i0118').send_keys(password)
        sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div').click()
        sleep(5)
        try:
            self.driver.find_element(By.XPATH, '/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input').click()
            sleep(2)
            pickle.dump(self.driver.get_cookies(), open(f"outlook\\{email}.pkl", "wb"))
            sleep(1000)
        except NoSuchElementException:
            sleep(1000)


    # def update_profile(self):
    #     self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div').click()
    #     sleep(26)
        
    #     # Edit profile
    #     self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[4]/div/div/div[2]/div/div/div').click()
    #     sleep(1)

        
    #     # Add button
    #     self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/span/div/div[2]/div/div[2]/div/div/span/span').click()
    #     sleep(1)

    #     # Upload Photo
    #     self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[4]/div/div[2]/div[1]/div/div[2]/div/div/div/div[3]/div[1]/div/div[1]/div/div').click()
    #     sleep(5)


    #     self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[4]/div/div[2]/div[1]/div/div[2]/div/div/div/div[3]/div[1]/div/div[1]/input').send_keys("E:\\image.jpg")
    #     sleep(10)
        
    #     self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[4]/div/div[2]/div[1]/div/div[2]/div/div/div/div[3]/div[5]/div[2]/div/div').click()
    #     sleep(20)

    # def like(self,comments):
    #     self.driver.get('https://www.facebook.com/groups/1200351056971790/?hoisted_section_header_type=recently_seen&multi_permalinks=2118548688485351')
    #     sleep(5)

    #     self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1]').click()
    #     sleep(5)

    #     self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[2]/div/div[1]').click()
    #     sleep(5)

    #     pyautogui.write(comments[0])
    #     sleep(1)

    #     pyautogui.press('enter')
    #     sleep(2)



bot = FacebookBot("100040142383607","1vhe8N6W")
# bot = FacebookBot.update_profile(self=bot)
# bot = FacebookBot.like(self=bot, comments=bot.comments)
bot = FacebookBot.email_check(self=bot, email="oenvgw735374@hotmail.com", password="jfNES2gQ6")