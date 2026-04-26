from flask import Blueprint, jsonify, request
from app.models import db, Question

questions_bp = Blueprint('questions', __name__, url_prefix='/questions')


@questions_bp.route('/', methods=['GET'])
def get_questions():
    """Получение списка всех вопросов."""

    # questions = Question.query.all()

    # questions = db.session.query(Question).all()


    # questions_data = [{"id": q.id, "text": q.text} for q in questions]
    # return jsonify(questions_data)
    return "Вопрос получен"




@questions_bp.route('/', methods=['POST'])
def create_question():
    """Создание нового вопроса."""
    data = request.get_json()

    if not data or not data.get("text"):
        return  jsonify({"message": "Вопрос создан", })

    return "Вопрос создан"


@questions_bp.route('/<int:id>', methods=['GET'])
def get_question(id):
    """Получение деталей конкретного вопроса по его ID."""
    return f"Детали вопроса {id}"


@questions_bp.route('/<int:id>', methods=['PUT'])
def update_question(id):
    """Обновление конкретного вопроса по его ID."""
    return f"Вопрос {id} обновлен"


@questions_bp.route('/<int:id>', methods=['DELETE'])
def delete_question(id):
    """Удаление конкретного вопроса по его ID."""
    return f"Вопрос {id} удален"