import pickle
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from time import sleep
import time
# import undetected_chromedriver as uc
import pyautogui
from selenium.webdriver.support.ui import Select
from selenium_stealth import stealth
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
from selenium.webdriver.common.keys import Keys
import json

with open('../config.json') as f:
    data = json.load(f)
    user_agent_strings = data['user_agent_strings']

class InstagramBot:
    def __init__(self, username, password,  email):
        self.username = username
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--no-sandbox')
        # self.options.add_argument('--single-process')
        # self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument("--incognito")
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # self.options.add_argument("disable-infobars")
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

        # if os.path.isfile(f"instagram/cookies/ig_{username}.pkl"):
        #     self.driver.get("https://www.instagram.com/")
        #     sleep(2)
        #     cookies = pickle.load(open(f"instagram/cookies/ig_{username}.pkl", "rb")) 
        #     for cookie in cookies:
        #         self.driver.add_cookie(cookie)
        #     self.driver.get("https://www.instagram.com/")
        #     sleep(2)
        #     # try:
        #     #     WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))).send_keys(username)
        #     #     print("NOT LOGIN: ", username)
        #     # except TimeoutException:
        #     #     pass

        # else:
        #     print("No Cookie: ", username)
        self.driver.get('https://www.instagram.com/accounts/login/')
        sleep(2)
        WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))).send_keys(username)
        email_login = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_login.send_keys(username)
        password_login = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_login.send_keys(password)
        password_login.submit()

        # try:
        #     WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[id="verificationCodeDescription"]')))
        #     if verify_code:
        #         otp = self.otpgen(verify_code)
        #     opt_fld = self.driver.find_element(By.CSS_SELECTOR, 'input[name="verificationCode"]')
        #     opt_fld.send_keys(otp)
        #     opt_fld.submit()
        #     sleep(10)

        # except TimeoutException:
        #     pass
 
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'form._aal8 > div:nth-child(2) > span > button'))).click()
            # self.driver.find_element(By.CSS_SELECTOR, 'form._aal8 > div:nth-child(2) > span > button').click()
        except TimeoutException:
            pass
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button[tabindex="0"]')))[1].click()
            sleep(2)
        except (TimeoutException, IndexError):
            pass
            
            # sleep(5)
        pickle.dump(self.driver.get_cookies(), open(f"instagram/cookies/ig_{username}.pkl", "wb"))

            #     sleep(5)

            #     try:
            #         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/div/div/div[3]/form/span/button'))).click()
            #         # self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/div/div/div[3]/form/span/button').click()
            #         sleep(2)
            #         if email.split('@')[1] == 'hotmail.com' or email.split('@')[1] == 'outlook.com':
            #             self.driver.execute_script("window.open('');") 
            #             self.driver.switch_to.window(self.driver.window_handles[1]) 
            #             self.driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=19&ct=1704704863&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fcobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26nlp%3d1%26deeplink%3dowa%252f0%252f%253fstate%253d1%26redirectTo%3daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC8%26RpsCsrfState%3dc8fb4362-e2f6-ef73-b652-f904fa47b9fc&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c")
            #             self.driver.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]').send_keys(email)
            #             sleep(2)
            #             self.driver.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div').click()
            #             sleep(2)

            #             # sleep(200)
            #             self.driver.find_element(By.ID, 'i0118').send_keys(email_pass)
            #             sleep(2)
                        
            #             self.driver.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div').click()
            #             sleep(2)
                
            # #             try:
            # #                 self.driver.execute_script("window.open('');") 
            # #                 self.driver.switch_to.window(self.driver.window_handles[2]) 
            # #                 self.driver.get("https://internxt.com/temporary-email")
            # #                 sleep(5)
                            
            # #                 temp_mail = self.driver.find_element(By.XPATH, '/html/body/div/div[3]/section[1]/div/div[2]/div[1]/div[1]/div').text
            # #                 self.driver.switch_to.window(self.driver.window_handles[1]) 

            # #                 self.driver.find_element(By.ID, 'EmailAddress').send_keys(temp_mail)
            # #                 sleep(1)
            # #                 self.driver.find_element(By.CSS_SELECTOR, '#frmAddProof > div.position-buttons > div > div').click()
            # #                 sleep(2)
            # #                 self.driver.switch_to.window(self.driver.window_handles[2])
            # #                 # sleep(200)
            # # # --------------------------------------------------
            # #                 WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/section[1]/div/div[3]/div[1]/div/div[2]/button'))).click()
            # #                 sleep(2)
            # #                 otp = self.driver.find_element(By.XPATH, '/html/body/div/div[3]/section[1]/div/div[3]/div[2]/div/div/div[3]/table/tbody/tr[4]/td/span').text
            # #                 self.driver.close()
            # #                 self.driver.switch_to.window(self.driver.window_handles[1])
            # #                 self.driver.find_element(By.ID, 'iOttText').send_keys(otp)
            # #                 sleep(1)
            # #                 self.driver.find_element(By.ID, 'iNext').click()

            # #             except NoSuchElementException:
            # #                 pass

            #             # WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input'))).click()

            #             sleep(5)
            #             try:
            #                 self.driver.find_element(By.XPATH, '/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input').click()
            #                 sleep(2)
            #                 pickle.dump(self.driver.get_cookies(), open(f"outlook/{email}.pkl"))
            #             except NoSuchElementException:
            #                 sleep(10)

            #             sleep(15)
            #             WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#MailList > div > div > div > div > div > div > div > div:nth-child(2) > div'))).click()
                        
            #             # self.driver.find_element(By.CSS_SELECTOR,'#MailList > div > div > div > div > div > div > div > div:nth-child(2) > div').click()
            #             sleep(2)
            #             otp = WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#x_email_content > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr > td > p:nth-child(4)'))).text

            #             # otp = self.driver.find_element(By.CSS_SELECTOR, '#x_email_content > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr > td > p:nth-child(4)').text
                        
            #             self.driver.close()
            #             self.driver.switch_to.window(self.driver.window_handles[0]) 

            #             otp_send = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/div/div/div[2]/form/div/input')
            #             otp_send.send_keys(otp)
            #             # otp_send.submit()
            #             sleep(1)
            #             self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/div/div/div[2]/form/span/button').click()
            #             sleep(5)
                        
                
            #     except (NoSuchElementException, TimeoutException):
            #         pass

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

    def open(self, url):
        self.driver.get(url)
        sleep(10000)
        
        

    def follow(self, url):
        self.driver.get(url)
        sleep(8)

        try:
            # Clicking on the "Following" button
            follo = self.driver.find_element(By.CSS_SELECTOR, "button._acan._acap._acas._aj1-._ap30")
            print(follo.text)
            follo.click()
            sleep(2)
        except NoSuchElementException:
            print("Already Following")

        # Clicking on the like button (Assuming this was the intended action)
        # self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div").click()
        # sleep(5)

    def update_profile(self, bio, full_name, image_path=None):
        self.driver.maximize_window()
        # WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span'))).click()
        # self.driver.find_element
        # sleep(5)
        # WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]'))).click()

        # self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]').click()
        # sleep(50)
        self.driver.get("https://www.instagram.com/accounts/edit/")
        sleep(2)
        bio_fld = self.driver.find_element(By.ID, value="pepBio")
        # bio_fld = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'pepBio')))
        bio_fld.click()
        sleep(1)
        bio_fld.clear()
        sleep(1)
        bio_fld.send_keys(bio)
        sleep(2)
        bio_fld.submit()
        
        # sleep(1000000)
        
        sleep(3)
            
        if image_path:
            # WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._ap36._a9_0'))).click()
            # self.driver.find_element(By.CSS_SELECTOR, 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._ap36._a9_0').click()
            # self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[3]/div/div/div[2]/div[1]/div[2]').click()
            # sleep(4)
            # sleep(2000)      
            pyautogui.write(image_path)
            sleep(2)
            pyautogui.press('enter')
            sleep(5)

        if full_name:
            self.driver.get("https://accountscenter.instagram.com/?entry_point=app_settings")
            self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/main/main/div[2]/div/div/div/a[1]/div[1]').click()
            # sleep(10000)
            # WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="mount_0_0_xS"]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/main/main/div[2]/div/div/div/a[1]'))).click()
            WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label="Name"]'))).click()
            # sleep(1000)
            name_fld = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="text"]')))
            # sleep(5)
            # name_fld.click()
            sleep(2)
            for _ in range(len(name_fld.get_attribute('value'))):
                name_fld.send_keys(Keys.BACK_SPACE)
            sleep(2)
            name_fld.send_keys(full_name)
            sleep(2)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[4]/div[3]/div/div/div/div/div/div/div'))).click()
            sleep(15)

    def post(self, image_path, post_text=None, screen=True, sleepval=30):
        # self.driver.get("")
        post_composition_xpath = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div'
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, post_composition_xpath))).click()
            sleep(4)
            WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/button'))).click()
            # self.driver.find_element(By.CSS_SELECTOR, 'button._acan._acap._acas._aj1-._ap30').click()
            # upload_input.send_keys(image_path)
            sleep(4)
            try:
                WebDriverWait(self.driver, 500).until(EC.presence_of_element_located((By.XPATH, '#mount_0_0_nF > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1.x1dr59a3.xixxii4.x13vifvy.xeq5yr9.x1n327nk > div > div > div > div > div.x1iyjqo2.xh8yej3 > div:nth-child(7) > div > span > div > div > div > div.x1qjc9v5.xgf5ljw.xhk9q7s.x1otrzb0.x1i1ezom.x1o6z2jb.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x2lah0s.xk390pu.x5yr21d.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x6ikm8r.x1odjw0f.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf.xh8yej3 > a:nth-child(1)'))).click()
            except TimeoutException:
                pass

            try:
                self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[1]').click()
            except NoSuchElementException:
                pass
            
            pyautogui.write(image_path)
            # self.driver.find_element(By.ID, "file-submit").click()
            sleep(2)
            pyautogui.press('enter')
            sleep(2)
            try:
                self.driver.find_element(By.CSS_SELECTOR, 'button._acan._acap._acaq._acas._acav._aj1-._ap30').click()
                
            except NoSuchElementException:
                pass

            sleep(2)
            # crop = self.driver.find_element(By.CSS_SELECTOR, 'button._acan._acao._acas._aj1-._ap30')
            # crop.click()
            # WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1f6kntn.xwhw2v2.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.x1i0vuye.xjbqb8w.xm3z3ea.x1x8b98j.x131883w.x16mih1h.x972fbf.xcfux6l.x1qhh985.xm0m39n.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1n5bzlp.x173jzuc.x1yc6y37'))).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button'))).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/div[1]'))).click()
            # sleep(2000)

            next_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div')))
            next_button.click()
            sleep(2)

            next_again = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div')))
            next_again.click()
            sleep(2)
            if post_text:

                caption_input = self.driver.find_element(By.CSS_SELECTOR, 'div[contenteditable="true"][aria-label="Write a caption..."]')
                caption_input.send_keys(post_text)

            share_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div')))
            share_button.click()
            WebDriverWait(self.driver, 1000).until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/h1/div'), "Reel shared"))
            if screen:
                    self.driver.save_screenshot(f'Screenshots/insta/{time.strftime("%Y%m%d-%H%M%S")}.png')

            print("Posted Successfully!!")
        
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
            print("Not Working: ", self.username)

    def make_comment(self, url, comment, screen=True):
        self.driver.get(url)
        sleep(2)
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.xp7jhwk'))).click()
        # self.driver.find_element(By.CSS_SELECTOR, 'span.xp7jhwk').click()
        sleep(2)
        comment_box = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Add a comment…']")))
        comment_box.click()
        sleep(1)
        # comment_box.send_keys(comment)
        pyautogui.write(comment)
        # sleep(200)
        pyautogui.press("enter")
        sleep(2)
        # Save
        try:
            save_btn = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.x11i5rnm.x1gryazu')))
            save_btn.click()
        except (NoSuchElementException, TimeoutError):
            print("Save Button Not Availabale")
        
        if screen:
            self.driver.save_screenshot(f'Screenshots/insta/{time.strftime("%Y%m%d-%H%M%S")}.png')
        
        sleep(2)

    def close(self):
        self.driver.quit()