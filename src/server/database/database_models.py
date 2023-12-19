from peewee import Model, CharField, IntegerField, FloatField, ForeignKeyField
import peewee   
import settings


db = peewee.SqliteDatabase(database=f'{settings.DATABASE_PATH}/{settings.DATABASE_NAME}')


class BaseModel(Model):
    class Meta:
        database = db

class Customer(BaseModel):
    fio = CharField(default='')
    address = CharField(default='')
    phone_number = CharField(default='')

class Order(BaseModel):
    customer_id = ForeignKeyField(model=Customer, related_name='fk1', default=0)
    date = CharField(default='')
    total_cost = FloatField(default=0)

class DishCategory(BaseModel):
    name = CharField(default='') 

class Dish(BaseModel):
    category_id = ForeignKeyField(model=DishCategory, related_name='fk2', default=0)
    name = CharField(default='')
    description = CharField(default='')
    price = FloatField(default=0)

class OrderedDish(BaseModel):
    order_id = ForeignKeyField(model=Order, related_name='fk2', default=0)
    dish_id = ForeignKeyField(model=Customer, related_name='fk3', default=0)
    quantity = IntegerField(default=0)

class User(BaseModel):
    position = CharField(default='')
    login = CharField(default='')
    password = CharField(default='')
    power_level = IntegerField(default=0)



db.create_tables(
    [
        Customer,
        Order,
        DishCategory,
        Dish,
        OrderedDish,
        User
    ]
)