from flask import Flask
from app.config import DevelopmentConfig
from app.routers.questions import questions_bp
from app import create_app

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(questions_bp, url_prefix='/questions')

app = create_app()
if __name__ == '__main__':
 app.run(debug=True)