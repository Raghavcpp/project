import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user = 'kanika'
pasw = 'Kanika@#$!001'
chrome_driver_path = "chromedriver_win64/chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"executable_path={chrome_driver_path}")

# Initialize webdriver outside the loop
browser = webdriver.Chrome(options=chrome_options)

while True:
    try:
        x = time.ctime()
        print(f"Current Time : {x}")

        # url ="https://www.ajath.com/wp-admin/"
        url ="https://www.ajath.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.ajath.com%2Fwp-admin%2F&reauth=1"
        browser.get(url)

        print(browser.title)
        wait = WebDriverWait(browser, 20)
        ok = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='jetpack-sso-wrap']/a[1]")))
        ok.click()
        time.sleep(2)  # Add a delay after page load

        # Wait for the username field to be present
        username = wait.until(EC.presence_of_element_located((By.NAME, "log")))
        username.send_keys(user)

        # Wait for the password field to be present
        password = wait.until(EC.presence_of_element_located((By.NAME, "pwd")))
        password.send_keys(pasw)

        # Wait for the login button to be clickable
        login_button = wait.until(EC.element_to_be_clickable((By.NAME, "wp-submit")))
        login_button.click()
        time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    # finally:
    #     # Close the browser to release resources
    #     browser.quit()

