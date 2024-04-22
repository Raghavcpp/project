import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.keys import Keys
import pyautogui
import contentPage
import urllib.request

def initialize_browser():
    chrome_driver_path = "chromedriver_win32/chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"executable_path={chrome_driver_path}")
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=chrome_options)
    
    return browser

def login(browser, username, password):
    # url ="https://www.usa.ajath.com/wp-admin/"
    url ="https://www.ajath.us/wp-admin/post-new.php?post_type=stm_services"
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
    post_title= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[1]/div[1]/div[1]/input")))
    post_title.click()
    post_title.send_keys(post_data[0])
    sleep(1)
    print("step fill title")

    element = browser.find_element(By.CLASS_NAME, 'wpb_switch-to-composer')
    if element.text.strip() == "Classic Mode":
        element.click()
    elif element.text.strip() == "Backend Editor":
        pass

    ptext= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[1]/div[6]/div/div[1]/div[2]/button[2]")))

    ptext.click()
    post_content= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[1]/div[6]/div/div[2]/textarea")))
    post_content.click()
    post_content.send_keys(post_data[1])
    sleep(10)
    print("step fill content")

    for i in range(len(post_data[2])):
        # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[5]/form/div[2]/div/div[2]/div"))).click()
        # sleep(1)
        # browser.execute_script("window.scrollTo(0,500)")
        if post_data[2][i]=="Application services":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[1]/label/input")))
            post_category.click()
        if post_data[2][i]=="Artificial intelligence":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[2]/label/input")))
            post_category.click()
        if post_data[2][i]=="Automation":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[3]/label/input")))
            post_category.click()
        if post_data[2][i]=="Business":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[4]/label/input")))
            post_category.click()
        if post_data[2][i]=="Business strategy":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[5]/label/input")))
            post_category.click()
        if post_data[2][i]=="Cloud":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[6]/label/input")))
            post_category.click()
        if post_data[2][i]=="Investment":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[7]/label/input")))
            post_category.click()
        if post_data[2][i]=="Researches":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[8]/label/input")))
            post_category.click()
        if post_data[2][i]=="Science":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[9]/label/input")))
            post_category.click()
        if post_data[2][i]=="Solutions":
            post_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[10]/label/input")))
            post_category.click()
        sleep(1)
    print("step tick category")

    # browser.execute_script("window.scrollTo(0,500)")
    # for i in range(len(post_data[3])):
    #     post_keyword= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[5]/form/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input[1]")))
    #     post_keyword.click()
    #     post_keyword.send_keys(post_data[3][i])
    #     sleep(1)
    #     post_keyword_add= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[5]/form/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input[2]")))
    #     post_keyword_add.click()
    #     sleep(1)
    # print("Step keyword add")

    # post_focused_keyword= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[5]/form/div[2]/div/div[3]/div[1]/div[3]/div[2]/div/div[2]/div/div[4]/div/div/div[1]/div/input")))
    # post_focused_keyword.click()
    # post_focused_keyword.send_keys(post_data[4])
    # sleep(2)

def upload_image(browser, image_path):
    wait = WebDriverWait(browser, 100)
    # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    post_image= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[4]/div[2]/p/a")))
    post_image.click()

    post_upload_image_section = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[1]/div/div/div[3]/div[1]/div/button[1]")))
    post_upload_image_section.click()

    post_upload_image =wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[1]/div/div/div[3]/div[2]/div/div/div[1]/button")))
    post_upload_image.click()
    sleep(3)
    pyautogui.write(image_path)
    sleep(3)
    pyautogui.press('enter')
    sleep(10)
    # post_image_select = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[16]/div[1]/div/div/div[3]/div[2]/div/div[3]/ul/li[1]")))
    # post_image_select.click()
    post_set_image = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[1]/div/div/div[4]/div/div[2]/button")))
    post_set_image.click()
    print("step image uploaded")
    sleep(2)
    
def draft_preview_publish(browser):
    wait = WebDriverWait(browser, 100)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/ul/li[3]/a"))).click()
    select_element = wait.until(EC.element_to_be_clickable((By.NAME,"butterbean_stm_default_fields_setting_header_transparent")))
    select = Select(select_element)
    select.select_by_value("true")
    sleep(3)
    browser.execute_script("window.scrollTo(0, 0);")
    sleep(1)
    post_save_draft = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div[2]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/input")))
    post_save_draft.click()
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
def usaAjath(i,title,titleSummary,heading,heading_summary,SubHeading,SubHeading_summary,categories,graphData,graphLine,link):
        titled = title[i]
        list_Post_Content = contentPage.content(titleSummary[i],heading[i],heading_summary[i],SubHeading[i],SubHeading_summary[i],graphData[i],graphLine[i])
        list_Post_Categories = categories[i]
        listAjath = [titled, list_Post_Content, list_Post_Categories]
        url = link[i]
        # print(url)
        filename = "output\\image"
        file_extension = url.split('.')[-1]
        filename_with_extension = filename + '.' + file_extension
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        with open(filename_with_extension, 'wb') as f:
            f.write(response.read())
        dictionaryPath = os.getcwd()
        image_path = os.path.join(dictionaryPath, filename_with_extension)
        post_to_wordpress(user, pasw, listAjath, image_path)