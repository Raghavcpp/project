import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
import Featured_Image_Generation as FIG
import pyautogui

def initialize_browser():
    chrome_driver_path = "chromedriver_win32/chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"executable_path={chrome_driver_path}")
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=chrome_options)
    
    return browser

def login(browser, username, password):
    url = "https://www.ajath.ae/wp-login.php?redirect_to=https%3A%2F%2Fwww.ajath.ae%2Fwp-admin%2F&reauth=1"
    browser.get(url)
    wait = WebDriverWait(browser, 100)
    
    username_field = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/form/p[1]/input")))
    username_field.click()
    username_field.send_keys(username)

    pas= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/form/div/div/input")))
    pas.click()
    pas.send_keys(password)

    login_button = wait.until(EC.element_to_be_clickable((By.NAME, "wp-submit")))
    login_button.click()

def create_new_page(browser, page_data):
    wait = WebDriverWait(browser, 100)
    pages = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/ul/li[5]/a/div[3]")))
    pages.click()

    new_page = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/a")))
    new_page.click()
    page_title= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[1]/div[1]/div[1]/input")))
    page_title.click()
    page_title.send_keys(page_data[0])
    sleep(1)
    print("step fill title")

    ptext= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[1]/div[3]/div/div[1]/div[2]/button[2]")))
    ptext.click()
    page_content= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[1]/div[3]/div/div[2]/textarea")))
    page_content.click()
    page_content.send_keys(page_data[1])
    print("step fill content")
    sleep(2)

    page_focused_keyword= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[3]/div[1]/div[3]/div[2]/div/div[2]/div/div[4]/div/div/div[1]/div/input")))
    page_focused_keyword.click()
    page_focused_keyword.send_keys(page_data[4])
    sleep(2)
    print("step focus")

    page_SEO = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[3]/div[1]/div[3]/div[2]/div/div[2]/div/div[5]/div/div/section/div/section[2]/div[1]/div[3]/div[1]/div/div/div")))
    page_SEO.click()
    
    page_SEO.send_keys(Keys.CONTROL,"a",Keys.DELETE)
    sleep(1)
    page_SEO.send_keys(page_data[2])
    sleep(1)
    print("step SEO")
    
    page_slug = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[3]/div[1]/div[3]/div[2]/div/div[2]/div/div[5]/div/div/section/div/section[2]/div[3]/input")))
    page_slug.click()
    page_slug.send_keys(page_data[5])
    sleep(1)
    print("step slug")

    again = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[3]/div[1]/div[3]/div[2]/div/div[2]/div/div[5]/div/div/section/div/section[2]/div[4]/div[3]/div[1]/div/div/div/div/div")))
    again.click()
    again.send_keys(page_data[3])
    sleep(1)
    print("Step meta add")

def draft_preview_publish(browser):
    sleep(3)
    browser.execute_script("window.scrollTo(0, 0);")
    sleep(1)
    wait = WebDriverWait(browser, 100)
    page_save_draft = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/input")))
    page_save_draft.click()
    print("draft")

    sleep(5)
    page_preview = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/a")))
    page_preview.click()
    print("preview")
    browser.switch_to.window(browser.window_handles[0])
    sleep(1)

    # page_publish = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/input[2]")))
    # page_publish.click()
    sleep(5)

def page_to_wordpress(username, password, page_data):
    browser = initialize_browser()
    try:
        login(browser, username, password)
        create_new_page(browser, page_data)
        draft_preview_publish(browser)
        sleep(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        browser.quit()

user = 'kanika'
pasw = 'Kanika@#$!001'
def arabAjath(i,title,content,SEO,META,focus,slag):
        titled = title[i]
        list_page_Content = content[i]
        list_page_SEO = SEO[i]
        list_page_Metas = META[i]
        focused = focus[i]
        slaged = slag[i]
        listAjath = [titled, list_page_Content, list_page_SEO, list_page_Metas, focused, slaged]

        # FIG.add_text_to_image(input_image_path="ajathARAB.png", text_to_add=titled, output_image_path="ajathARABtext.png", font_names="arial.ttf", font_size=100, text_color="#71F242", boldness=3, wordwrap=32)
        # dictionaryPath= os.getcwd()
        # image_path = dictionaryPath+"\\output\\ajathARABtext.png"
        # page_to_wordpress(user, pasw, listAjath, image_path)
        page_to_wordpress(user, pasw, listAjath)
