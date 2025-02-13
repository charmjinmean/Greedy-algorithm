from com.knapsack.knapsack_model import KnapsackModel
from com.knapsack.knapsack_service import KnapsackService


class KnapsackController:
    def __init__(self, **kwargs):
        self.capacity = int(kwargs.get("capacity"))
        self.profits = [int(kwargs.get(f"profit{i}", 0)) for i in range(1, 5)]
        self.weights = [int(kwargs.get(f"weight{i}", 0)) for i in range(1, 5)]

    def get_result(self) -> KnapsackModel:
        knapsack = KnapsackModel(capacity=self.capacity,
            profit1=self.profits[0], profit2=self.profits[1], profit3=self.profits[2], 
            profit4=self.profits[3],weight1=self.weights[0], weight2=self.weights[1], 
            weight3=self.weights[2], weight4=self.weights[3])
        service = KnapsackService()
        return service.execute(knapsack)
    

        
        