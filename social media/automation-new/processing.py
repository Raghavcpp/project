import pandas as pd

df = pd.read_excel("fb-acc.xlsx")
new_df = pd.DataFrame()
unames = []
pwds = []
codes = []
for i in range(df.shape[0]):
    if df['is_disabled'][i] == "Not Disabled":
        unames.append(str(df['Facebook Username'][i]))
        pwds.append(df['Facebook Password'][i])
        codes.append(df['2FA Code'][i])
new_df['Facebook Username'] = unames
new_df['Facebook Password'] = pwds
new_df['2FA Code'] = codes

new_df.to_excel('working-fb.xlsx', index=False)
        