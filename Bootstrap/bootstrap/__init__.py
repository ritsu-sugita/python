from flask import Flask

app = Flask(__name__)
import bootstrap.main

from bootstrap import db

db.create_books_table()
