# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "flask",
#   "requests",
#   "pandas"
# ]
# ///

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello To Script Run For UV"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)


# to run this is use cmd, virtual env nhi banata hai script ke time banta hai lekin uske uv mai rakhta hai usko yeh run karta hai
"""

- uv run --with flask second_env.py

for multiple install
- uv run --with flask --with requests --with pandas second_env.py

lekin jab more install aa jata hai tab dikkat hota hai toh usko fix karne ke liye:
uv add --script flask request or write direct
--
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "flask",
#   "requests",
#   "pandas"
# ]
# ///

"""