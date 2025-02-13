
from com.count.exchage_service import ExchangeService
from com.count.exchange_model import ExchangeModel


class ExchangeController:
    def __init__(self, **kwargs):
        self.amount = int(kwargs.get("amount"))
        self.currency = kwargs.get("currency")

    def get_result(self) -> ExchangeModel:
        exchange = ExchangeModel()
        exchange.amount=self.amount
        exchange.currency=self.currency
        service = ExchangeService()
        return service.execute(exchange)

        
        

