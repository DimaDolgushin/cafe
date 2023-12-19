from pydantic import BaseModel


class ModifyBaseModel(BaseModel):
    id: int = 0


class Customer(ModifyBaseModel):
    fio: str
    address: str
    phone_number: str


class ChangePassword(BaseModel):
    password: str


class LoginData(BaseModel):
    login: str
    password: str


class Order(ModifyBaseModel):
    customer_id: int
    date: str
    total_cost: float


class Dish(ModifyBaseModel):
    name: str
    description: str
    price: float


class DishCategory(ModifyBaseModel):
    name: str


class OrderedDish(ModifyBaseModel):
    order_id: int
    dish_id: int
    quantity: int


class User(ModifyBaseModel):
    login: str
    position: str
    password: str
    power_level: int