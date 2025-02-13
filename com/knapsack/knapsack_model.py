from dataclasses import dataclass

@dataclass
class KnapsackModel :
    capacity : int
    profit1 : int
    profit2 : int
    profit3 : int
    profit4 : int
    weight1 : int
    weight2 : int
    weight3 : int
    weight4 : int
    result : str =""

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def profit1(self) -> int:
        return self._profit1

    @profit1.setter
    def profit1(self, profit1):
        self._profit1 = profit1

    @property
    def profit2(self) -> int:
        return self._profit2

    @profit2.setter
    def profit2(self, profit2):
        self._profit2 = profit2

    @property
    def profit3(self) -> int:
        return self._profit3

    @profit3.setter
    def profit3(self, profit3):
        self._profit3 = profit3

    @property
    def profit4(self) -> int:
        return self._profit4

    @profit4.setter
    def profit4(self, profit4):
        self._profit4 = profit4

    @property
    def weight1(self) -> int:
        return self._weight1

    @weight1.setter
    def weight1(self, weight1):
        self._weight1 = weight1

    @property
    def weight2(self) -> int:
        return self._weight2

    @weight2.setter
    def weight2(self, weight2):
        self._weight2 = weight2

    @property
    def weight3(self) -> int:
        return self._weight3

    @weight3.setter
    def weight3(self, weight3):
        self._weight3 = weight3

    @property
    def weight4(self) -> int:
        return self._weight4

    @weight4.setter
    def weight4(self, weight4):
        self._weight4 = weight4

    @property
    def result(self) -> str:
        return self._result

    @result.setter
    def result(self, result):
        self._result = result