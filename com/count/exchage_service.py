
from com.count.exchange_model import ExchangeModel

class ExchangeService :
    def __init__(self):
        pass

    def execute(self, exchange:ExchangeModel) -> ExchangeModel:
        currency_list = []
        currency_unit = ''

        if exchange.currency =='USD':
            currency_list = self.get_dollar_list()
            currency_unit = '달러'
            exchange.page = "exchange_dollar.html"
        elif exchange.currency == 'WON':
            currency_list = self.get_won_list()
            currency_unit = '원'
            exchange.page = "exchange_won.html"
        elif exchange.currency == "JPY":
            currency_list = self.get_yen_list()
            currency_unit = "엔"
            exchange.page = "exchange_yen.html"
        elif exchange.currency == "CNY":
            currency_list = self.get_yuan_list()
            currency_unit = "위안"
            exchange.page = "exchange_yuan.html"
        else:
            raise ValueError("잘못된 화폐 단위입니다.")

        currency_dict = self.get_currency_dict(exchange.amount, currency_list)
        self.print_currency_dict(currency_dict)
        exchange.result = self.format_currency_count(currency_dict, currency_unit)
        return exchange
    
    def get_currency_dict(self, amount, currency_list)->dict:
        money = amount
        currency_dict = {}
        for currency in currency_list:
            currency_dict[currency] = money // currency
            money %= currency
        return currency_dict
    
    def get_won_list(self):
        WON_50000 = 50000
        WON_10000 = 10000
        WON_5000 = 5000
        WON_1000 = 1000
        WON_500 = 500
        WON_100 = 100
        WON_50 = 50
        WON_10 = 10
        won_list = [WON_50000, WON_10000, WON_5000,
                        WON_1000, WON_500, WON_100, WON_50, WON_10]
        return won_list
    
    def get_dollar_list(self):
        DOLLAR_100 = 100
        DOLLAR_50 = 50
        DOLLAR_20 = 20
        DOLLAR_10 = 10
        DOLLAR_5 = 5
        DOLLAR_2 = 2
        DOLLAR_1 = 1

        dollar_list = [DOLLAR_100, DOLLAR_50, DOLLAR_20, 
                       DOLLAR_10, DOLLAR_5, DOLLAR_2, DOLLAR_1] 
        return dollar_list  
    
    def get_yen_list(self):
        yen_10000 = 10000
        yen_5000 = 5000
        yen_2000 = 2000
        yen_1000 = 1000
        yen_500 = 500
        yen_100 = 100
        yen_50 = 50
        yen_10 = 10
        yen_5 = 5
        yen_1 = 1

        yen_list = [yen_10000, yen_5000, yen_2000, yen_1000,
                       yen_500, yen_100, yen_50, yen_10, yen_5,yen_1 ] 
        return yen_list  
    
    def get_yuan_list(self):
        yuan_100 = 100
        yuan_50 = 50
        yuan_20 = 20
        yuan_10 = 10
        yuan_5 = 5
        yuan_1 = 1

        yuan_list = [yuan_100, yuan_50, yuan_20, 
                       yuan_10, yuan_5, yuan_1] 
        return yuan_list  
    
    def format_currency_count(self, currency_dict, currency_unit):
        temp = ''
        for currency ,count in currency_dict.items():
            temp += f"{currency}{currency_unit}: {count}개<br/>"
        return temp
   
    def print_currency_dict(self, currency_dict):
        print("-------💰거스름돈💰-------")
        for won, count in currency_dict.items():
            print(f"{won}원: {count}개")
        print("-------끝-------")


    