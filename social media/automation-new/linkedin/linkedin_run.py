import pandas as pd
from linkedin_bot import linkedinBot
from time import sleep
import openpyxl, re,os
import gdown
from datetime import datetime, timedelta


file_url = 'https://docs.google.com/spreadsheets/d/1Ohc7PF765iXXfhGtZDGFHqr0WQm6IQhq2l70ljEra8c/export?format=xlsx'
destination_path = 'datafile.xlsx'
gdown.download(file_url, destination_path, quiet=False)
dictionaryPath= os.getcwd()
df = pd.read_excel(dictionaryPath+"\\datafile.xlsx")

email = "ajathsolutions@gmail.com"
password = "P@ssw0rd1111"
username = "Ajathinfotech"
# email = "gofoney758@minhlun.com"
# password = "ajaj@123"
# username = "aj6025410554073"
today_date = datetime.today().date()
# print(today_date - timedelta(days=1))
varss = today_date - timedelta(days=2)

for i in range(df.shape[0]):
    try:
        if((df.iloc[i,0].date()) == varss):
            imagepath=dictionaryPath+"\\downloaded_files\\events\\"+str(df.iloc[i,4])+".jpg"
            print(imagepath)
            bot = linkedinBot(username, password,email)
            # # # bot.like("https://linkedin.com/Priscil17190586/status/1743126534129586468", reply="12345", retweet=True, save=True)
            sleep(1000)
            bot.post(caption=df.iloc[i,3], path=imagepath)
            sleep(2)
            bot.close()
    except Exception as e:
        print(e)
        pass



# for row in range(2, ws.max_row + 1):
#     try:
#         # token = df['Token'][i]
#         # full_name = df['Name Change'][i]
#         # bio = df['Bio Change'][i]
#         bot = linkedinBot(username, password)
#         # bot.update_profile(banner_path="C:\\Users\\Administrator\\Downloads\\image.jpg",dp_path="C:\\Users\\Administrator\\Downloads\\image.jpg",full_name=full_name, bio=bio)
#         # bot.like("https://linkedin.com/Priscil17190586/status/1743126534129586468", reply="12345", retweet=True, save=True)
#         bot.post(caption="Hello, I'm new here", path="imagepath")
#         # sleep(100000)
#         bot.close()
#     except Exception:
#         pass
