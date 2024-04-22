from facebook import FacebookBot
import pandas as pd
from time import sleep

df = pd.read_excel("facebook/redlist-fb--1----Fixed-31.1.xlsx")

for i in range(df.shape[0]):
    username = str(df['Email'][i])
    password = df['Email Password'][i]
    # code = df['Token'][i]
    print("USERNAME: ", username)
    bot = FacebookBot(username, password)
    bot.like("https://www.facebook.com/groups/1276931359699730/permalink/1436053530454178/",comment="Bapak @Prabowo Subianto, semoga cita-cita mulia untuk kemajuan negeri ini dapat tercapai dengan dukungan bersama. Mari, teruslah berjuang! 🙌🌟")
    sleep(1000)
    bot.close()
    sleep(2)



