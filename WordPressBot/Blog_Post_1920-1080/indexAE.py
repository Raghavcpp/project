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
    # sleep(1000)
    # print(browser.title)
    wait = WebDriverWait(browser, 100)
    
    username_field = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/form/p[1]/input")))
    username_field.click()
    username_field.send_keys(username)

    pas= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/form/div/div/input")))
    pas.click()
    pas.send_keys(password)

    login_button = wait.until(EC.element_to_be_clickable((By.NAME, "wp-submit")))
    login_button.click()

def create_new_post(browser, post_data):
    wait = WebDriverWait(browser, 100)
    posts = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/ul/li[3]/a/div[3]")))
    posts.click()

    new_post = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/ul/li[3]/ul/li[3]/a")))
    new_post.click()
    post_title= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[1]/div[1]/div[1]/input")))
    post_title.click()
    post_title.send_keys(post_data[0])
    sleep(1)
    print("step fill title")

    ptext= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[1]/div[3]/div/div[1]/div[2]/button[2]")))
    ptext.click()
    post_content= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[1]/div[3]/div/div[2]/textarea")))
    post_content.click()
    post_content.send_keys(post_data[1])
    sleep(10)
    print("step fill content")

    for i in range(len(post_data[2])):
        if post_data[2][i]=="Blogging":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[1]/label/input")))
            post_category.click()
        if post_data[2][i]=="Online Marketing":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[2]/label/input")))
            post_category.click()
        if post_data[2][i]=="Ratings":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[3]/label/input")))
            post_category.click()
        if post_data[2][i]=="Remarketing":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[4]/label/input")))
            post_category.click()
        if post_data[2][i]=="SEO":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[5]/label/input")))
            post_category.click()
        if post_data[2][i]=="SEO Testing":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[6]/label/input")))
            post_category.click()
        if post_data[2][i]=="Social Media Marketing":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[7]/label/input")))
            post_category.click()
        if post_data[2][i]=="Uncategorized":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[8]/label/input")))
            post_category.click()
        sleep(1)
    print("step tick category")
    for i in range(len(post_data[3])):
        post_keyword= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input[1]")))
        post_keyword.click()
        post_keyword.send_keys(post_data[3][i])
        sleep(1)
        post_keyword_add= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input[2]")))
        post_keyword_add.click()
        sleep(1)
    print("Step keyword add")

    post_focused_keyword= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[3]/div[1]/div[6]/div[2]/div/div[2]/div/div[4]/div/div/div[1]/div/input")))
    post_focused_keyword.click()
    post_focused_keyword.send_keys(post_data[4])
    sleep(2)

def upload_image(browser, image_path):
    wait = WebDriverWait(browser, 100)
    post_image= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[3]/div[2]/div[1]/div[2]/p/a")))
    post_image.click()

    post_upload_image_section = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[1]/div/div/div[3]/div[1]/div/button[1]")))
    post_upload_image_section.click()

    post_upload_image =wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[1]/div/div/div[3]/div[2]/div/div/div[1]/button")))
    post_upload_image.click()
    sleep(3)
    pyautogui.write(image_path)
    sleep(3)
    pyautogui.press('enter')
    # sleep(100)
    sleep(10)

    # post_image_select = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[1]/div/div/div[3]/div[2]/div/div[3]/ul/li[1]")))
    # post_image_select.click()

    post_set_image = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[1]/div/div/div[4]/div/div[2]/button")))    
    post_set_image.click()
    print("step image uploaded")
    sleep(2)
    
def draft_preview_publish(browser):
    sleep(3)
    browser.execute_script("window.scrollTo(0, 0);")
    sleep(1)
    wait = WebDriverWait(browser, 100)
    post_save_draft = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/input")))
    post_save_draft.click()
    print("draft")

    sleep(5)
    post_preview = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/a")))
    post_preview.click()
    print("preview")
    browser.switch_to.window(browser.window_handles[0])
    sleep(1)

    post_publish = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/input[2]")))
    post_publish.click()
    sleep(5)

def post_to_wordpress(username, password, post_data, image_path):
    browser = initialize_browser()
    try:
        login(browser, username, password)
        create_new_post(browser, post_data)
        upload_image(browser, image_path)      
        draft_preview_publish(browser)
        sleep(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        browser.quit()

user = 'kanika'
pasw = 'Kanika@#$!001'
def arabAjath(i,title,content,categories,keywords,focus):
        titled = title[i]
        list_Post_Content = content[i]
        list_Post_Categories = categories[i]
        list_Post_Tags = keywords[i]
        focused = focus[i]
        listAjath = [titled, list_Post_Content, list_Post_Categories, list_Post_Tags, focused]

        FIG.add_text_to_image(input_image_path="ajathARAB.png", text_to_add=titled, output_image_path="ajathARABtext.png", font_names="arial.ttf", font_size=100, text_color="#71F242", boldness=3, wordwrap=32)
        dictionaryPath= os.getcwd()
        image_path = dictionaryPath+"\\output\\ajathARABtext.png"
        post_to_wordpress(user, pasw, listAjath, image_path)