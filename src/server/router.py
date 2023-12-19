from src.server.database import pydantic_models, database_models
from src.server.service import RouterManager


routers = (
    RouterManager(pydantic_model=pydantic_models.Customer, database_model=database_models.Customer, prefix='/customers', tags=['Customers']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Dish, database_model=database_models.Dish, prefix='/dishes', tags=['Dishes']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.DishCategory, database_model=database_models.DishCategory, prefix='/dish_categories', tags=['DishCategories']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Order, database_model=database_models.Order, prefix='/orders', tags=['Orders']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.User, database_model=database_models.User, prefix='/users', tags=['Users']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.OrderedDish, database_model=database_models.OrderedDish, prefix='/ordered_dishes', tags=['OrderedDishes']).fastapi_router
)
