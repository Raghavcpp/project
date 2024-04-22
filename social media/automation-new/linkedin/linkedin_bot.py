import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
import pyautogui
from selenium.webdriver.support.ui import Select
import pandas as pd
import os
from selenium_stealth import stealth
from selenium.webdriver.support.ui import WebDriverWait
# import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
import json

with open('config.json') as f:
    data = json.load(f)
    user_agent_strings = data['user_agent_strings']


class linkedinBot:
    def __init__(self, username, password,email):
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument('--no-sandbox')
        # self.options.add_argument('--single-process')
        # self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument("--incognito")
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_argument("disable-infobars")
        self.driver = webdriver.Chrome(options=self.options)
        stealth(self.driver,
        user_agent= random.choice(user_agent_strings),
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
        # self.driver.get('https://linkedin.com')
        # sleep(2)
        # # cookie = {
        # #     "domain": ".linkedin.com",
        # #     "name": "auth_token",
        # #     "path": "/",
        # #     "secure": True,
        # #     "value": token,
        # #         }
        # # self.driver.add_cookie(cookie)
        # sleep(2)
        self.driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
        sleep(2)
        self.driver.maximize_window()
        sleep(2)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[1]/input'))).send_keys(email)
        sleep(2)        
        # self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
        # sleep(2)
        # try:
        #     useridenty = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        #     useridenty.send_keys(username)
        #     sleep(2)
        #     self.driver.find_element(By.XPATH , '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div').click()
        #     sleep(1)
        # except:
        #     pass
        password_login = self.driver.find_element(by=By.XPATH, value='/html/body/div/main/div[2]/div[1]/form/div[2]/input')
        sleep(2)
        password_login.send_keys(password)
        sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[3]/button').click()
        sleep(6)
        # try:
        #     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="ocfEnterTextTextInput"][inputmode="text"]'))).send_keys("0000")
        # except (NoSuchElementException, TimeoutException):
        #     pass

    def update_profile(self, full_name, bio, dp_path=None, banner_path=None):
        sleep(2)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[aria-label="Profile"]'))).click()
        # self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[10]/div').click()
        sleep(2)
        # self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div[2]/a').click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="editProfileButton"]'))).click()
        sleep(2)
        if banner_path:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Add banner photo"]'))).click()
            sleep(2)
            pyautogui.write(banner_path)
            sleep(1)
            pyautogui.press("enter")
            sleep(4)
            self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="applyButton"]').click()
            sleep(2)

        
        if dp_path:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Add avatar photo"]'))).click()
            sleep(2)
            pyautogui.write(dp_path)
            sleep(1)
            pyautogui.press("enter")
            sleep(4)
            self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="applyButton"]').click()
            sleep(2)

        name_fld = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="displayName"]')))
        name_fld.clear()
        name_fld.send_keys(full_name)
        sleep(2)

        b_fld = self.driver.find_element(By.CSS_SELECTOR, 'textarea[name="description"]')
        b_fld.clear()
        b_fld.send_keys(bio)
        sleep(12)
        # save
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="Profile_Save_Button"]'))).click()
    
    def like(self, url, reply=None, retweet=False, save=False):
        self.driver.get(url)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="like"][tabindex="0"]'))).click()
            sleep(2)
        except TimeoutException:
            print("Already Liked")

        # reply
        if reply:
            rbox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="textbox"][contenteditable="true"][tabindex="0"]')))
            # sleep(2)
            rbox.click()
            sleep(2)
            rbox.send_keys(reply)
            sleep(2)
            try:
                WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="tweetButtonInline"]'))).click()
            except TimeoutException:
                WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="tweetButton"]'))).click()
            sleep(4)

                # 
        # retweet
        if retweet:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="retweet"]'))).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="retweetConfirm"]'))).click()            
            sleep(4)

        # save/bookmark
        if save:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="bookmark"]'))).click()
            sleep(3)

    def post(self, caption, path=None):
        self.driver.refresh()
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetTextarea_0RichTextInputContainer"]').click()
        pyautogui.write(caption)
        sleep(3)
        
        if path:
            self.driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Add photos or video"]').click()
            sleep(1)
            pyautogui.write(path)
            sleep(2)
            pyautogui.press('enter')
            sleep(3)
        
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="tweetButtonInline"]'))).click()



    def close(self):
        self.driver.close()



# linkedin_bot = linkedinBot("guptaxvivek", "Vivek@9540")
# linkedin_bot.update_profile("Vivek Gupta", "I am no one")