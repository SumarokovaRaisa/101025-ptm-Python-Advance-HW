from flask_sqlalchemy import SQLAlchemy # new
from flask_migrate import Migrate # new

db = SQLAlchemy() # new

from app.models.responses import *
from app.models.questions import *