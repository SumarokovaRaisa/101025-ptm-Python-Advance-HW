from flask import request, jsonify, Flask
from app.models import db, Category, Question
from app.schemas.questions import CategoryCreate, CategoryResponse, QuestionResponse


app = Flask(__name__)
# POST /categories: Создание
@app.route('/categories', methods=['POST'])
def create_category():
    data = request.json
    try:
        # Валидация через Pydantic
        cat_data = CategoryCreate(**data)
        new_cat = Category(name=cat_data.name)
        db.session.add(new_cat)
        db.session.commit()
        return jsonify(CategoryResponse.model_validate(new_cat).model_dump()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# GET /categories: Список всех
@app.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([CategoryResponse.model_validate(c).model_dump() for c in categories])

# PUT /categories/{id}: Обновление
@app.route('/categories/<int:id>', methods=['PUT'])
def update_category(id):
    cat = Category.query.get_or_404(id)
    data = request.json
    cat.name = data.get('name', cat.name)
    db.session.commit()
    return jsonify(CategoryResponse.model_validate(cat).model_dump())

# DELETE /categories/{id}: Удаление
@app.route('/categories/<int:id>', methods=['DELETE'])
def delete_category(id):
    cat = Category.query.get_or_404(id)
    db.session.delete(cat)
    db.session.commit()
    return jsonify({"message": "Deleted successfully"}), 200