import pandas as pd
import os

df = pd.read_excel("facebook/redlist-fb--1----Fixed-31.1.xlsx")

for i in range(df.shape[0]):
    username = str(df['Email'][i]).split('.')[0]
    if os.path.exists(f'facebook/fb_cookies/fb_{username}.pkl'):
        pass
    else:
        print(username)