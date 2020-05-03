from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config
from model import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
#db = SQLAlchemy(app)
migrate = Migrate(app, db)

from views import *

if __name__ == '__main__':
    app.run()