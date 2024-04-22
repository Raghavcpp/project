import pickle
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver import ActionChains
import pyautogui
# import undetected_chromedriver as uc
from selenium_stealth import stealth
import random
import json
from selenium.webdriver.support.ui import Select
import pandas as pd
import os

with open('config.json') as f:
    data = json.load(f)
    user_agent_strings = data['user_agent_strings']

# username, password = "vivek.ajath", "Ajath@123"

class FacebookBot:
    # driver.maximize_window()
    def __init__(self, username, password, verify_code=None):
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
        self.driver.maximize_window()
        stealth(self.driver,
        user_agent= random.choice(user_agent_strings),
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
        self.driver.get('https://www.facebook.com/')
        sleep(1)
        if os.path.exists(f'facebook/fb_cookies/fb_{username.split(".")[0]}.pkl'):
            cookies = pickle.load(open(f'facebook/fb_cookies/fb_{username.split(".")[0]}.pkl','rb'))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            sleep(1)
            self.driver.get("https://www.facebook.com/")
            sleep(3)
            try:
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input')))
                os.remove(f'facebook/fb_cookies/fb_{username.split(".")[0]}.pkl')
            except TimeoutException:
                pass
            # self.driver.close()
        else:
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input'))).send_keys(username)
            # self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input').send_keys(username)
            # sleep(1)
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input'))).send_keys(password)
            # sleep(1)
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button'))).click()
            # sleep(10000)
            try:
                otp_field = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'approvals_code')))
                otp_field.click()
                print("Not Working: ", username)
            except TimeoutException:
                pass
            # otp = self.otpgen(verify_code)
            # print("OTP GOT: ", otp)
            # otp_field.send_keys(otp)
            # WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.ID, 'checkpointSubmitButton'))).click()
            # WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.ID, 'checkpointSubmitButton'))).click()
            # WebDriverWait(self.driver, 100).until(EC.presence_of_all_elements_located())
            try:
                sleep(2)
                self.driver.find_element(By.ID, 'checkpointSubmitButton').click()
                sleep(2)
                self.driver.find_element(By.ID, 'checkpointSubmitButton').click()
                sleep(2)
                self.driver.find_element(By.ID, 'checkpointSubmitButton').click()
                sleep(5)
            except:
                sleep(5)
            
            # cookies = pickle.load(open(f'facebook/fb_cookies/fb_{username}.pkl','rb'))

            # pickle.dump(self.driver.get_cookies(), open(f'facebook/fb_cookies/fb_{username}.pkl', 'wb'))
            # self.driver.close()

            
            # sleep(1000)


            # WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[2]/div'))).click()
            # # sleep(1)

            # WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div[2]/ul/li[2]/div/div[1]'))).click()
            # # sleep(1)

            # self.driver.find_element(By.XPATH, value='/html/body/div[3]/div[2]/div/div/div/div[2]/ul/li[2]/div/div[2]/ul/li/div/div/div[2]/button').click()
            # sleep(1)

            # self.driver.find_element(By.XPATH, value='/html/body/div[3]/div[2]/div/div/div/div/div/div/div[3]/span[2]/div/div').click()
            # sleep(1)

            # self.driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div[2]/span/input').send_keys("oenvgw735374@hotmail.com")
            # sleep(1)
            
            # self.driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[4]/div/div/span/input').send_keys("oenvgw735374@hotmail.com")
            # sleep(1)

            # self.driver.find_element(By.XPATH, value='/html/body/div[4]/div[2]/div/div/div/div/div/div/div[3]/span[2]/div/div[2]').click()
            # sleep(10)

    def disabled(self):
        return self.is_disabled


    def otpgen(self, code):
        self.driver.execute_script("window.open('');") 
        self.driver.switch_to.window(self.driver.window_handles[1]) 
        self.driver.get("https://2fa.live/")
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID,'listToken'))).send_keys(code)
        sleep(1)
        self.driver.find_element(By.ID, 'submit').click()
        sleep(4)
        self.driver.find_element(By.ID, 'copy_btn').click()
        # print("OTP: ", )
        # sleep(1000)
        otp = pyperclip.paste().split("|")[1]
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        print("CODE GOT: ", otp)
        return otp

    def like(self, url, comment):
        self.driver.get(url)
        sleep(2)

        # # Like
        # sleep(2)
        btns = self.driver.find_elements(By.CSS_SELECTOR, 'div.x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x3nfvp2.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz')
        # sleep(5000)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x3nfvp2.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x5ve5x3'))).click()
        # # Comment
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mount_0_0_gy > div > div:nth-child(1) > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x78zum5.xdt5ytf.x1iyjqo2.x1us19tq > div > div.x9f619.x2lah0s.x1n2onr6.x78zum5.x1iyjqo2.x1t2pt76.x1lspesw > div > div > div.x78zum5.xdt5ytf.x1iyjqo2 > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div:nth-child(2) > div > div > div:nth-child(4) > div > div > div:nth-child(1) > div > div.xq8finb.x16n37ib.x1fqkajt.x1aj7aux.x1axty5n.x1uuop16 > div > div:nth-child(2)'))).click()
        # self.driver.find_element(By.XPATH, '')[1].click()
        sleep(1)
        # comment_btn
        btns[3].click()        
        sleep(2)   
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mount_0_0_AP > div > div:nth-child(1) > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x78zum5.xdt5ytf.x1iyjqo2.x1us19tq > div > div.x9f619.x2lah0s.x1n2onr6.x78zum5.x1iyjqo2.x1t2pt76.x1lspesw > div > div > div.x78zum5.xdt5ytf.x1iyjqo2 > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div:nth-child(2) > div > div > div:nth-child(4) > div > div > div.x1pi30zi.x1swvt13.x1n2onr6 > div.x1gslohp > div.x1iyjqo2 > div > div > div > div > div:nth-child(2) > div > div > div.x1r8uery.x1iyjqo2.x6ikm8r.x10wlt62.x4uap5 > form > div > div.x78zum5.x13a6bvl > div.xi81zsa.xo1l8bm.xlyipyv.xuxw1ft.x49crj4.x1ed109x.xdl72j9.x1iyjqo2.xs83m0k.x6prxxf.x6ikm8r.x10wlt62.x1y1aw1k.xn6708d.xwib8y2.x1ye3gou > div > div.xzsf02u.x1a2a7pz.x1n2onr6.x14wi4xw.notranslate'))).send_keys(comment)
        sleep(2)
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="focused-state-composer-submit"]/span/div'))).click()
        # action = ActionChains(self.driver)
        # pyautogui.write(comment)
        # action.send_keys(comment)
        # sleep(2)
        # pyautogui.press('enter')
        sleep(300)
        # sleep(1000)

        # share
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[3]/div'))).click()
            sleep(1)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]'))).click()
            sleep(10)
        except TimeoutException:
            pass

    def close(self):
        self.driver.quit()

        # try:
        #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[3]/div'))).click()
        #     sleep(1)
        #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div'))).click()
        #     sleep(1)
        # except:
        #     pass
        # close()
        
    

    def posts(self, img_path):
        # print(self.driver.find_element((By.CSS_SELECTOR, 'div.xqmpxtq.x13fuv20.x178xt8z.x78zum5.x1a02dak.x1vqgdyp.x1l1ennw.x14vqqas.x6ikm8r.x10wlt62.x1y1aw1k.xh8yej3')[1]))

        # try:
        #     WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.x6s0dn4.x78zum5.x1s65kcs.x1n2onr6'))).click
        # except:
        #     pass
        WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]'))).click()

        # sleep(1000)
        Upload = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div'))).click()
        sleep(5)

        pyautogui.write(img_path)
        pyautogui.press("enter")  
        sleep(10)

        WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div'))).click()
        
