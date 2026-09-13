

class Migration_controller:
    async def get_quote(self, ticker: str):
        return "teste"

async def teste_function(self, ticker: str):  # adiciona o parâmetro
    return self.quote_service.get_quote(ticker)


migration_controller = Migration_controller()
