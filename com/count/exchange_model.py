from dataclasses import dataclass

@dataclass
class ExchangeModel :
    amount:int
    currency:str
    result:str
    page:str

    @property
    def amount(self) -> int:
        return self._amount
    
    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def currency(self) -> str:
        return self._currency
    
    @currency.setter
    def currency(self, currency):
        self._currency = currency

    @property
    def result(self) -> str:
        return self._result
    
    @result.setter
    def result(self, result):
        self._result = result

    @property
    def page(self) -> str:
        return self._page
    
    @page.setter
    def page(self, page):
        self._page = page