from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mpd_control.sqlite'
db = SQLAlchemy(app)

class Address(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user = db.Column(db.String(120))
  address = db.Column(db.String(512))

  def __init__(self, user, address):
    self.user = user
    self.address = address


@app.route("/users", methods=["GET"])
def get_users():
  all_users = Address.query.all()
  return all_users

# Hello World example
#@app.route("/")
#def hello():
#    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)

