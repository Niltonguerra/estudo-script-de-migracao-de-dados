# modules/data_migration/repositories/Migration_repository.py
from src.modules.data_migration.schema.product_schema import Product
from src.modules.data_migration.schema.user_schema import User


class MigrationRepository:
    async def create(self, name: str, price: float, description: str) -> Product:
        return await Product(name=name, price=price, description=description).insert()

    # async def find_by_ticker(self, ticker: str) -> Product | None:
    #     return await Product.find_one(Product.ticker == ticker)

    async def find_by_name(self, name: str) -> Product | None:
        return await Product.find_one(Product.name == name)

    # async def update_price(self, product: Product, price: float) -> Product:
    #     return await product.set({Product.price: price})

    async def delete(self, product: Product) -> None:
        await product.delete()
        
    async def create_product(self, name: str, price: float, description: str) -> Product:
        return await Product(name=name, price=price, description=description).insert()

    async def create_user(self, name: str, email: str) -> User:
        return await User(name=name, email=email).insert()

    async def get_all_products(self) -> list[Product]:
        return await Product.find_all().to_list()

    async def get_all_users(self) -> list[User]:
        return await User.find_all().to_list()


migration_repository = MigrationRepository()