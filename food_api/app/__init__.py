from flask import Flask

app = Flask(__name__)

from food_api.app import routes