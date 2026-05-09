from flask import Blueprint, jsonify, request
from app.models import db, Question, Category

questions_bp = Blueprint('questions', __name__, url_prefix='/questions')


@questions_bp.route('/', methods=['GET'])
def get_questions():
    """Получение списка всех вопросов."""
    questions = Question.query.all()

    questions_data = []
    for q in questions:
        questions_data.append({
            "id": q.id,
            "text": q.text,
            "category": {
                "id": q.category.id,
                "name": q.category.name
            } if q.category else None
        })

    return jsonify(questions_data), 200
    return "Вопрос получен"




@questions_bp.route('/', methods=['POST'])
def create_question():
    """Создание нового вопроса."""
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    text = data.get("text")
    category_id = data.get("category_id")

    if not text:
        return jsonify({"error": "Text is required"}), 400

    if not category_id:
        return jsonify({"error": "category_id is required"}), 400

    category = Category.query.get(category_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404

    question = Question(text=text, category_id=category_id)

    db.session.add(question)
    db.session.commit()

    return jsonify({
        "id": question.id,
        "text": question.text,
        "category": {
            "id": category.id,
            "name": category.name
        }
    }), 201

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