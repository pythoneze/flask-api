from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

@app.route("/")
def home():
    return '<h1>Fask REST API App</h1>'

if __name__ == "__main__":
    app.run(debug=True)
