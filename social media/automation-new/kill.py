import subprocess
# os.system("taskkill /f /im geckodriver.exe /T")
# os.system("taskkill /f /im chromedriver.exe /T")
subprocess.run(["taskkill", "/F", "/IM", "chrome.exe"], check=True)