from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)
api = Api(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"

user_arg = reqparse.RequestParser()
user_arg.add_argument('name', type=str, required=True, help="Name cannot be blank")
user_arg.add_argument('email', type=str, required=True, help="Email cannot be blank")

class Users(Resource):
    def get(self):
        users = UserModel.query.all()
        return users

api.add_resource(Users, '/api/users/')

@app.route("/")
def home():
    return '<h1>Fask REST API App</h1>'

if __name__ == "__main__":
    app.run(debug=True)
