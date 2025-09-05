# pip install gspread pandas gspread_dataframe oauth2client
# pip install gspread oauth2client


import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Drive API ke liye scope set karo
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Credentials load karo
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Apne sheet ka naam/URL use karo
sheet = client.open("First_Python").sheet1  # ya .worksheet("Sheet1")

# Data read karo
data = sheet.get_all_records()
print(data)

# Ek specific cell padho
print(sheet.cell(2, 2).value)  # Row 2, Column 2 ka value (suresh)
