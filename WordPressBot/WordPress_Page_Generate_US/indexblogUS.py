import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
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
    # url ="https://www.usa.ajath.com/wp-admin/"
    url ="https://www.ajath.us/wp-admin/post-new.php"
    browser.get(url)
    wait = WebDriverWait(browser, 100)
    
    print("step browser open")
    sleep(1)

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
    # posts = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/ul/li[4]/a/div[3]")))
    # posts.click()

    # new_post = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[5]/a")))
    # new_post.click()
    sleep(3)
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/a"))).click()
    except:
        pass
    sleep(1)
    post_title= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[1]/div[1]/div[1]/input")))
    post_title.click()
    post_title.send_keys(post_data[0])
    sleep(1)
    print("step fill title")

    sleep(1)
    try:
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/a"))).click()
    except:
        pass
    sleep(1)
    element = browser.find_element(By.CLASS_NAME, 'wpb_switch-to-composer')
    if element.text.strip() == "Classic Mode":
        element.click()

    sleep(1)
    ptext= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[1]/div[6]/div/div[1]/div[2]/button[2]")))
    ptext.click()
    sleep(1)
    post_content= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[1]/div[6]/div/div[2]/textarea")))
    post_content.click()
    post_content.send_keys(post_data[1])
    sleep(10)
    print("step fill content")

    for i in range(len(post_data[2])):
        # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[5]/form/div[2]/div/div[2]/div"))).click()
        sleep(1)
        browser.execute_script("window.scrollTo(0,0)")
        if post_data[2][i]=="Awards":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[1]/label/input")))
            post_category.click()
        if post_data[2][i]=="Business":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[2]/label/input")))
            post_category.click()
        if post_data[2][i]=="Deadline":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[3]/label/input")))
            post_category.click()
        if post_data[2][i]=="History":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[4]/label/input")))
            post_category.click()
        if post_data[2][i]=="Non classifié(e)":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[5]/label/input")))
            post_category.click()
        if post_data[2][i]=="Plans":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[6]/label/input")))
            post_category.click()
        if post_data[2][i]=="Success":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[7]/label/input")))
            post_category.click()
        if post_data[2][i]=="Uncategorized":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[8]/label/input")))
            post_category.click()
        sleep(1)
    print("step tick category")

    # browser.execute_script("window.scrollTo(0,500)")
    for i in range(len(post_data[3])):
        post_keyword= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[4]/div[2]/div/div/div[2]/input[1]")))
        post_keyword.click()
        post_keyword.send_keys(post_data[3][i])
        sleep(1)
        post_keyword_add= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[4]/div[2]/div/div/div[2]/input[2]")))
        post_keyword_add.click()
        sleep(1)
    print("Step keyword add")

    # post_focused_keyword= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[5]/form/div[2]/div/div[3]/div[1]/div[3]/div[2]/div/div[2]/div/div[4]/div/div/div[1]/div/input")))
    # post_focused_keyword.click()
    # post_focused_keyword.send_keys(post_data[4])
    # sleep(2)

def upload_image(browser, image_path):
    wait = WebDriverWait(browser, 100)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    post_image= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[8]/div[2]/p/a")))
    post_image.click()

    post_upload_image_section = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/div/div/div[3]/div[1]/div/button[1]")))
    post_upload_image_section.click()

    post_upload_image =wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/div/div/div[3]/div[2]/div/div/div[1]/button")))
    post_upload_image.click()
    sleep(3)
    pyautogui.write(image_path)
    sleep(3)
    pyautogui.press('enter')
    sleep(10)
    # post_image_select = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[16]/div[1]/div/div/div[3]/div[2]/div/div[3]/ul/li[1]")))
    # post_image_select.click()
    post_set_image = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/div/div/div[4]/div/div[2]/button")))
    post_set_image.click()
    print("step image uploaded")
    sleep(2)
    
def draft_preview_publish(browser):
    wait = WebDriverWait(browser, 100)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/ul/li[2]/a"))).click()
    select_element = wait.until(EC.element_to_be_clickable((By.NAME,"butterbean_stm_default_fields_setting_header_transparent")))
    select = Select(select_element)
    select.select_by_value("true")
    sleep(3)
    browser.execute_script("window.scrollTo(0, 0);")
    sleep(1)
    wait = WebDriverWait(browser, 100)
    post_save_draft = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/input")))
    post_save_draft.click()
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/a"))).click()
    except:
        pass
    
    sleep(1)
    post_preview = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/a")))
    post_preview.click()
    print("preview")
    browser.switch_to.window(browser.window_handles[0])
    sleep(1)
    post_publish = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/input[2]")))
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

user = 'ajath'
pasw = 'Ajath@#007!$&'
def usaAjath(i,title,content,categories,keywords,focus):
        titled = title[i]
        list_Post_Content = content[i]
        list_Post_Categories = categories[i]
        list_Post_Tags = keywords[i]
        focused = focus[i]
        listAjath = [titled, list_Post_Content, list_Post_Categories, list_Post_Tags, focused]
        FIG.add_text_to_image(input_image_path="ajathUSA.png", text_to_add=titled, output_image_path="ajathUSAtext.png", font_names="arial.ttf", font_size=100, text_color="#71F242", boldness=3, wordwrap=32)
        dictionaryPath= os.getcwd()
        image_path = dictionaryPath+"\\output\\ajathUSAtext.png"
        post_to_wordpress(user, pasw, listAjath, image_path)