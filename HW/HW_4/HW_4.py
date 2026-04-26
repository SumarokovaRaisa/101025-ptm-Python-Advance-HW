from sqlalchemy import (create_engine,
                        Column, Integer,
                        String, Boolean,
                        Numeric, ForeignKey,
                        func)
from sqlalchemy.orm import sessionmaker, declarative_base, relationship


engine = create_engine("sqlite:///:memory:", echo=True)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))

    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Numeric(10,2), nullable=False)
    in_stock = Column(Boolean, default=True)

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")


Base.metadata.create_all(engine)


"""Задача 1: Наполнение данными
Добавьте в базу данных следующие категории и продукты
Добавление категорий: Добавьте в таблицу categories следующие категории:
Название: "Электроника", Описание: "Гаджеты и устройства."
Название: "Книги", Описание: "Печатные книги и электронные книги."
Название: "Одежда", Описание: "Одежда для мужчин и женщин."""""

categories = [
    Category(name="Электроника", description="Гаджеты и устройства."),
    Category(name="Книги", description="Печатные книги и электронные книги."),
    Category(name="Одежда", description="Одежда для мужчин и женщин.")
    ]

session.add_all(categories)
session.commit()

"""Добавление продуктов: Добавьте в таблицу products следующие продукты, убедившись, 
что каждый продукт связан с соответствующей категорией:
Название: "Смартфон", Цена: 299.99, Наличие на складе: True, Категория: Электроника
Название: "Ноутбук", Цена: 499.99, Наличие на складе: True, Категория: Электроника
Название: "Научно-фантастический роман", Цена: 15.99, Наличие на складе: True, 
Категория: Книги
Название: "Джинсы", Цена: 40.50, Наличие на складе: True, Категория: Одежда
Название: "Футболка", Цена: 20.00, Наличие на складе: True, Категория: Одежда"""

products = [
    Product(name="Смартфон", price= 299.99, in_stock=True, category_id=1),
    Product(name="Ноутбук", price= 499.99, in_stock=True, category_id=1),
    Product(name="Научно-фантастический роман", price= 15.99, in_stock=True, category_id=2),
    Product(name="Джинсы", price= 40.50, in_stock=True, category_id=3),
    Product(name="Футболка", price= 20.00, in_stock=True, category_id=3),
]
session.add_all(products)
session.commit()


"""Задача 2: Чтение данных
Извлеките все записи из таблицы categories. Для каждой категории извлеките и 
выведите все связанные с ней продукты, включая их названия и цены."""

categories = session.query(Category).all()
for category in categories:
    print(category.name, category.description)
    if category.products:
        for product in category.products:
            print(product.name, product.price)


"""Задача 3: Обновление данных
Найдите в таблице products первый продукт с названием "Смартфон". Замените цену
 этого продукта на 349.99."""

product = session.query(Product).filter(Product.name == "Смартфон").first()

if product:
    product.price = 349.99
    session.commit()


"""Задача 4: Агрегация и группировка
Используя агрегирующие функции и группировку, подсчитайте общее количество 
продуктов в каждой категории."""

result = (
    session.query(Category.name, func.count(Product.id))
    .join(Product)
    .group_by(Category.id)
    .all()
)
for category_name, product_count in result:
    print(category_name, "- ", product_count)


"""Задача 5: Группировка с фильтрацией
Отфильтруйте и выведите только те категории, в которых более одного продукта."""

result_1 = (
    session.query(Category.name, func.count(Product.id))
    .join(Product)
    .group_by(Category.id)
    .having(func.count(Product.id) > 1)
    .all()
)
for category_name, product_count in result_1:
    print(category_name, " - ", product_count)