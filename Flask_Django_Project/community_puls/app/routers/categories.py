from flask import request, jsonify, Blueprint
from app.extensions import db
from app.models import  Category
from app.schemas.questions import CategoryCreate, CategoryResponse
categories_bp = Blueprint("categories", __name__, url_prefix="/categories")


# POST /categories: Создание
@categories_bp.route('/', methods=['POST'])
def create_category():
    data = request.get_json()
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
@categories_bp.route('/', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([CategoryResponse.model_validate(c).model_dump() for c in categories]), 200

# PUT /categories/{id}: Обновление
@categories_bp.route('/<int:id>', methods=['PUT'])
def update_category(id):
    cat = Category.query.get_or_404(id)
    data = request.get_json()
    cat.name = data.get('name', cat.name)
    db.session.commit()

    return jsonify(CategoryResponse.model_validate(cat).model_dump()), 200

# DELETE /categories/{id}: Удаление
@categories_bp.route('/<int:id>', methods=['DELETE'])
def delete_category(id):
    cat = Category.query.get_or_404(id)

    db.session.delete(cat)
    db.session.commit()

    return jsonify({"message": "Deleted successfully"}), 200