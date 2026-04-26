from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import DevelopmentConfig

from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

db = SQLAlchemy()
migrate = Migrate()