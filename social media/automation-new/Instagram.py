from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import pyautogui

from selenium.webdriver.support.ui import Select
import pandas as pd
import os


# username, password = "vivek.ajath", "Ajath@123"

class InstagramBot:
    comments = ["Hello"]

    def __init__(self, username, password):
        self.driver = webdriver.Chrome()

        self.driver.get('https://www.instagram.com/accounts/login/')
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys(username)
        sleep(1)
        password_login = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input').send_keys(password)
        sleep(1)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button').click()
        sleep(10)

        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/span/div/a/div').click()
        sleep(1)

# Like section
    def like(self):
        self.driver.get('https://www.instagram.com/reel/C1oH10nRzhs/?utm_source=ig_web_copy_links')
        sleep(1)

        # Like
        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[3]/div[1]/div[1]/span[1]/div/div').click()
        sleep(5)

        try:
            # Clicking on the "Following" button
            follo = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div[2]/div')
            follo.click()
            sleep(2)

            # Check if "Following" is in the text
            div_text = follo.text
            if "Following" in div_text:
                # If following, click the "Unfollow" button
                self.driver.find_element(by=By.XPATH, value='/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/button[2]').click()
                sleep(5)
        except NoSuchElementException:
            print("Element not found or action failed.")

        # Clicking on the like button (Assuming this was the intended action)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[3]/div[1]/div[1]/span[2]/div/div').click()


# Follow section in new tab
    def follow(self, url):
        self.driver.get(url)
        sleep(5)

        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button').click()
        sleep(2)

        try:
            # Clicking on the "Following" button
            follo = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button')
            # follo.click()
            sleep(2)

            # Check if "Following" is in the text
            div_text = follo.text
            if "Following" in div_text:
                # If following, click the "Unfollow" button
                self.driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div').click()
                sleep(5)
        except NoSuchElementException:
            print("Element not found or action failed.")

        # Clicking on the like button (Assuming this was the intended action)
        # self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div").click()
        sleep(5)


# Comments
    def comment(self, url, comments):
        self.driver.get(url)
        sleep(5)

        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[3]/div[1]/div[1]/span[2]/div').click()
        sleep(2)

        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[2]/span').click()
        sleep(2)

        # Comment

        com = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea').click()
        sleep(5)

        textarea_text = com.text
        textarea_text = textarea_text + " " + comments[0]

        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea').clear()
        sleep(5)

        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea').click()
        sleep(5)
        

        pyautogui.write(comments[0])
        sleep(1)

        pyautogui.press('enter')
        sleep(2)


# Comments
def comment(self, url, comments):
    self.driver.get(url)
    sleep(5)

    self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[3]/div[1]/div[1]/span[2]/div').click()
    sleep(2)

    self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[2]/span').click()
    sleep(2)

    # Comment
    try:
        textarea = self.driver.find_element(by=By.XPATH, value='//textarea[@placeholder="Add a comment…"]')
        textarea.clear()
        textarea.send_keys(comments[0])
        sleep(2)

        # Post the comment
        textarea.submit()
        sleep(2)
    except NoSuchElementException:
        print("Textarea not found or action failed.")       



# Create an instance of the InstagramBot
bot = InstagramBot("canan34_1994", "OL0Bqt9ieKW2")

# Call the like method
bot.like()

# Call the follow method
bot.follow(url="https://www.instagram.com/tpmjuferraz/")

# Call the comment method
bot.comment(url="https://www.instagram.com/p/C109ogKxJdX/?utm_source=ig_web_copy_link", comments=bot.comments)