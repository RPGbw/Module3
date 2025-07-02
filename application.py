from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    booktitle = db.Column(db.String(80), unique=True, nullable=False)
    publisher = db.Column(db.String(40))
    author = db.Column(db.String(40))

    def __repr__(self):
        return f"{self.booktitle} - {self.author}"

@app.route('/')
def index():
    return 'hello'
