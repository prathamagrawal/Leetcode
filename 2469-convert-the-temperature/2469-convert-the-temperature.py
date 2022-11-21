class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return list([celsius+273.15,(celsius*1.80)+32])