from com.knapsack.knapsack_model import KnapsackModel

class KnapsackService :
    def __init__(self):
        pass

    def execute(self, knapsack:KnapsackModel) -> KnapsackModel:
        
        capacity = knapsack.capacity
        profits = [knapsack.profit1, knapsack.profit2, knapsack.profit3, knapsack.profit4]
        weights = [knapsack.weight1, knapsack.weight2, knapsack.weight3, knapsack.weight4]
        
        profit_per_weight = [profits[i]/weights[i] for i in range(4)]

        items = [ {"name": f"item{i+1}", "profit": profits[i], "weight": weights[i], 
                   "profit_per_weight": profit_per_weight[i]}
            for i in range(4)]

        for i in range(4):
           for j in range(i+1, 4):
            if items[i]["profit_per_weight"] < items[j]["profit_per_weight"]: 
                items[i], items[j] = items[j], items[i]
        
        for i in items:
           print("😎💲", i["name"])
        
        remaining_capacity = capacity 
        total_profit = 0
        selected_items = []

        for item in items:
            if item["weight"] <= remaining_capacity:
                remaining_capacity -= item["weight"]
                total_profit += item["profit"]
                selected_items.append(item["name"])
            else:
               fraction = remaining_capacity / item["weight"]
               total_profit += item["profit"]*fraction
               selected_items.append(f"{item['name']} ({fraction * 100:.1f}%)")
               remaining_capacity
               break
    
        knapsack.result = f"총 이익: {total_profit}, 선택된 아이템: {selected_items}"
        return knapsack
