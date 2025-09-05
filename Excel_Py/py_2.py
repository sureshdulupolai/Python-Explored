import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

sheet = client.open("First_Python").sheet1

# 1) Naya row add karna
sheet.append_row([3, "rahul", "rahul@gmail.com"])

# 2) Specific cell update karna (row=2, col=3 -> email change)
sheet.update_cell(2, 3, "suresh_new@gmail.com")

# 3) Pura row update karna
sheet.update("A4:C4", [[4, "neha", "neha@gmail.com"]])

# 4) Cell ka value read karna
print("Cell (2,3):", sheet.cell(2, 3).value)
