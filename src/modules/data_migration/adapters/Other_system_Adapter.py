# src/modules/data_migration/adapters/Other_system_Adapter.py
class OtherSystemAdapter:
    def __init__(self):
        self.base_url = "https://other-system.com/api"

    async def send_products(self, products: list) -> dict:
        # async with httpx.AsyncClient() as client:
        #     response = await client.post(
        #         f"{self.base_url}/products",
        #         json=[product.model_dump(mode="json") for product in products],
        #     )
        #     response.raise_for_status()
        #     return response.json()

        return {
            "status": "success",
            "message": "products received successfully",
            "total": len(products),
        }


other_system_adapter = OtherSystemAdapter()