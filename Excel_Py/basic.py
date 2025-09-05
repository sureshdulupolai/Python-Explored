"""
https://console.cloud.google.com/iam-admin/serviceaccounts/details/117303554918089492434;edit=true/keys?project=fiery-celerity-460505-k8

### 🔹 Next Steps (Screen par jo aap dekh rahe ho uske hisaab se)

1. **API Enable karna**

   * Left side ya Quick Access me **APIs and services** pe click karo.
   * Fir **+ ENABLE APIS AND SERVICES** pe click karo.
   * Search box me **Google Sheets API** likho → enable karo.
   * Wahi step repeat karke **Google Drive API** bhi enable karo.

---

2. **Service Account banani hai**

   * Wapas **APIs and services → Credentials** pe jao.
   * Upar **+ CREATE CREDENTIALS** button pe click karo.
   * “**Service account**” select karo.
   * Naam daalo (example: `sheets-service`).
   * Continue karo (roles optional hai, skip kar sakte ho).
   * Service account create ho jaayegi.

---

3. **JSON Key generate karni hai**

   * Jo service account banayi hai uspe click karo.
   * **Keys → Add Key → Create new key** pe jao.
   * JSON select karo → ek `.json` file download hogi.
   * Us file ko rename karke `credentials.json` rakho.
   * Usko apne Python script ke folder me rakho.

---

4. **Google Sheet share karo**

   * Apni Sheet (“First\_Python”) open karo.
   * **Share** button dabao.
   * JSON file ke andar `client_email` hota hai (kuch aisa: `xxxx@xxxx.iam.gserviceaccount.com`).
   * Us email ko sheet pe **Editor access** do.

---

5. **Python code run karo**
   Ab aapka code sahi chalega aur aap sheet ke data ko read kar paoge ✅


"""