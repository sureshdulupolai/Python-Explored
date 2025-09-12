"""

my_flask_app/
│── app/
│   ├── __init__.py       # App factory, Flask config
│   ├── routes.py         # Routes / Views
│   ├── models.py         # Database models (SQLAlchemy, etc.)
│   ├── forms.py          # Forms (WTForms)
│   ├── static/           # CSS, JS, Images
│   └── templates/        # HTML Templates
│
│── venv/                 # Virtual Environment (optional, ignore in git)
│── requirements.txt      # Dependencies
│── config.py             # Configurations (Dev/Prod/Testing)
│── run.py                # Entry point to start the app


Example run.py
from app import app

if __name__ == "__main__":
    app.run(debug=True)

    
Example app/init.py
from flask import Flask

app = Flask(__name__)

from app import routes


Example app/routes.py
from app import app
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")

"""