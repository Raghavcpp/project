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
    url ="https://www.ajath.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.ajath.com%2Fwp-admin%2F&reauth=1"
    browser.get(url)
    wait = WebDriverWait(browser, 100)

    username_field = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/form/p[1]/input")))
    username_field.click()
    username_field.send_keys(username)

    password_field = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/form/div/div/input")))
    password_field.click()
    password_field.send_keys(password)

    login_button = wait.until(EC.element_to_be_clickable((By.NAME, "wp-submit")))
    login_button.click()

def create_new_page(browser, page_data):
    wait = WebDriverWait(browser, 100)
    pages = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/ul/li[3]/a/div[3]")))
    pages.click()

    new_page = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/ul/li[3]/ul/li[3]/a")))
    new_page.click()
    page_title= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[1]/div[1]/div[1]/input")))
    page_title.click()
    page_title.send_keys(page_data[0])
    sleep(1)
    print("step fill title")

    ptext= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[1]/div[5]/div/div[1]/div[2]/button[2]")))
    ptext.click()
    page_content= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[1]/div[5]/div/div[2]/textarea")))
    page_content.click()
    page_content.send_keys(page_data[1])
    sleep(2)
    print("step fill content")
    # sleep(100)
    browser.execute_script("window.scrollTo(0, 0);")

    for i in range(len(page_data[2])):
        # try:
        wait.until(EC.element_to_be_clickable((By.ID, "side-sortables"))).click()
        sleep(1)
        browser.execute_script("window.scrollTo(0,200)")
        if page_data[2][i]=="App Development":
            page_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[1]/label/input")))
            page_category.click()
        if page_data[2][i]=="Apps":
            page_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[2]/label/input")))
            page_category.click()
        if page_data[2][i]=="Asides":
            page_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[3]/label/input")))
            page_category.click()
        if page_data[2][i]=="Buying":
            page_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[4]/label/input")))
            page_category.click()
        if page_data[2][i]=="Clerkship":
            page_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[4]/ul/li[1]/label/input")))
            page_category.click()
        if page_data[2][i]=="Clothes":
            page_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[4]/ul/li[2]/label/input")))
            page_category.click()
        if page_data[2][i]=="Company History":
            page_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[5]/label/input")))
            page_category.click()
        if page_data[2][i]=="Markup":
            page_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[6]/label/input")))
            page_category.click()
        if page_data[2][i]=="Equipollent":
            page_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[6]/ul/li[1]/label/input")))
            page_category.click()
        if page_data[2][i]=="Media":
            page_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[6]/ul/li[2]/label/input")))
            page_category.click()
        if page_data[2][i]=="News":
            page_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[7]/label/input")))
            page_category.click()
        if page_data[2][i]=="One Page":
            page_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[8]/label/input")))
            page_category.click()
        if page_data[2][i]=="Responsive":
            page_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[9]/label/input")))
            page_category.click()            
        if page_data[2][i]=="Technologies and Services":
            page_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[10]/label/input")))
            page_category.click()
        if page_data[2][i]=="Uncategorized":
            page_category = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[3]/div[2]/div/div[2]/ul/li[11]/label/input")))
            page_category.click()
        sleep(1)
    print("step tick category")
    for i in range(len(page_data[3])):
        page_keyword= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[4]/div[2]/div/div/div[2]/input[1]")))
        page_keyword.click()
        page_keyword.send_keys(page_data[3][i])
        sleep(1)
        page_keyword_add= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[4]/div[2]/div/div/div[2]/input[2]")))
        page_keyword_add.click()
        sleep(1)
    print("Step keyword add")

    page_focused_keyword= wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[3]/div[1]/div[3]/div[2]/div/div[2]/div/div[4]/div/div/div[1]/div/input")))
    page_focused_keyword.click()
    page_focused_keyword.send_keys(page_data[4])
    sleep(2)
    

# def upload_image(browser, image_path):
#     sleep(5)
#     wait = WebDriverWait(browser, 100)
#     wait.until(EC.element_to_be_clickable((By.ID, "side-sortables"))).click()
#     browser.execute_script("window.scrollTo(0,700)")
#     page_image_div = browser.find_element(By.ID, 'pageimagediv')
#     if 'pagebox' in page_image_div.get_attribute('class') and 'closed' in page_image_div.get_attribute('class'):
#         page_image_div.click()
#     page_image = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[6]/div[2]/p/a")))
#     page_image.click()

#     page_upload_image_section = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-upload")))
#     page_upload_image_section.click()

#     page_upload_image = wait.until(EC.element_to_be_clickable((By.ID, "__wp-uploader-id-1")))
#     page_upload_image.click()
#     sleep(3)
#     pyautogui.write(image_path)
#     sleep(3)
#     pyautogui.press('enter')
#     sleep(10)
#     # page_image_select = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[49]/div[1]/div/div/div[3]/div[2]/div/div[3]/ul/li[1]")))
#     # page_image_select.click()
    
#     try:
#         page_set_image = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[1]/div/div/div[4]/div/div[2]/button"))).click()
#     except:
#         try:
#             page_set_image = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[49]/div[1]/div/div/div[4]/div/div[2]/button"))).click()
#         except:
#             page_set_image = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button.media-button.button-primary.button-largemedia-button-select"))).click()
#     print("step image uploaded")
#     sleep(2)

def draft_preview_publish(browser):
    sleep(3)
    browser.execute_script("window.scrollTo(0, 0);")
    sleep(1)
    wait = WebDriverWait(browser, 100)
    draft = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/input")
    draft.click()
    sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/a").click()

    # page_preview = wait.until(EC.element_to_be_clickable((By.XPATH, "preview-action")))
    # page_preview.click()
    print("preview")
    browser.switch_to.window(browser.window_handles[0])
    sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/input[2]").click()
    sleep(5)

def page_to_wordpress(username, password, page_data, image_path):
    browser = initialize_browser()
    try:
        login(browser, username, password)
        create_new_page(browser, page_data)
        # upload_image(browser, image_path)      
        draft_preview_publish(browser)
        sleep(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        browser.quit()


user = 'kanika'
pasw = 'Kanika@#$!001'
def indiaAjath(i,title,content,categories,keywords,focus):
        titled = title[i]
        list_page_Content = content[i]
        list_page_Categories = categories[i]
        list_page_Tags = keywords[i]
        focused = focus[i]
        listAjath = [titled, list_page_Content, list_page_Categories, list_page_Tags, focused]
        FIG.add_text_to_image(input_image_path="ajathINDIA.png", text_to_add=titled, output_image_path="ajathINDIAtext.png", font_names="arial.ttf", font_size=100, text_color="#71F242", boldness=3, wordwrap=32)
        dictionaryPath= os.getcwd()
        image_path = dictionaryPath+"\\output\\ajathINDIAtext.png"
        page_to_wordpress(user, pasw, listAjath, image_path)