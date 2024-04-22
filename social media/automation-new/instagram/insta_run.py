import pandas as pd
import os
import gdown
from datetime import datetime, timedelta
from create_post import InstagramBot
import pandas as pd
from time import sleep

file_url = 'https://docs.google.com/spreadsheets/d/1Ohc7PF765iXXfhGtZDGFHqr0WQm6IQhq2l70ljEra8c/export?format=xlsx'
destination_path = 'datafile.xlsx'
gdown.download(file_url, destination_path, quiet=False)
dictionaryPath= os.getcwd()
df = pd.read_excel(dictionaryPath+"\\datafile.xlsx")
# print(4,df.columns)

# email = "ajathsolutions@gmail.com"
# password = "P@ssw0rd1111"
# username = "ajathinfotech"
email = "jagik41466@gexige.com"
password = "ajaj@123"
username = "jagik41466"
today_date = datetime.today().date()

for i in range(df.shape[0]):
    try:
        if((df.iloc[i,0].date()) == today_date):
            imagepath=dictionaryPath+"\\downloaded_files\\events\\"+str(df.iloc[i,4])+".jpg"
            instagram_bot = InstagramBot(username, password, email)
            # sleep(100)
            # instagram_bot.update_profile(bio=bio, full_name=name)
            # instagram_bot.open("https://www.instagram.com/topvoice/")
            ## Like, Comment & Save ##
            # for url in urls:
            #     instagram_bot.make_comment(url=url, comment=random.choice(comments), screen=True)
            
            instagram_bot.post(image_path=imagepath,post_text=df.iloc[i,3], sleepval=50)
            sleep(2)
            # instagram_bot.follow("https://www.instagram.com/beyonce/")

            ## Follow ##
            # for acc in follow_df['Link']:
            #     try:
            #         instagram_bot.follow(acc)
            #         sleep(30)
            #     except Exception:
            #         continue
            instagram_bot.close()

    except Exception as e:
        print("ERROR: ",e)
        print("NOT WORKING: ")
        continue