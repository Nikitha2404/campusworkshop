"""Setup at app startup"""
from flask import Flask
import psycopg2
from app import routes

app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq1kfdvk4rjsv8tm70-a",
        database="todo_u8u5",
        user="nikitha",
        password="r1e5hHolqJXNxqyZWrEcSbjU13ZLgOVQ")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position

