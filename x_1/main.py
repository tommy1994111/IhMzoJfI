from abc import ABCMeta, abstractmethod
from typing import List

class SmartPhoneStrategyAbstract(object, metaclass=ABCMeta):
    def __init__(self, price: int, camera_count: int, screen_size: int):
        self.price = price
        self.camera_count = camera_count
        self.screen_size = screen_size

    @abstractmethod
    def special_feature(self):
        '''特殊功能'''
        return NotImplemented


class GooglePhoneStrategy(SmartPhoneStrategyAbstract):
    def __init__(self):
        price = 10
        camera_count = 3
        screen_size = 5
        super().__init__(price, camera_count, screen_size)
    
    def special_feature(self, inputList: List[int]) -> List[int]:
        '''輸入一個 int list, 回傳偶數且大於 10 的元素，並由大至小進行排序
        
        例如: 輸入 [3, 43, 62, 15, 18, 22] 回傳 [62, 22, 18]
        '''
        pass

class TaiwanPhoneStrategy(SmartPhoneStrategyAbstract):
    def __init__(self):
        price = 20
        camera_count = 1
        screen_size = 3
        super().__init__(price, camera_count, screen_size)
    
    def special_feature(self, inputInt: int) -> int:
        '''輸入一個數字自動回傳 Fibonacci 斐波那契數列的運算結果

        例如: 輸入 33 回傳 3524578
        '''
        pass

class ApplePhoneStrategy(SmartPhoneStrategyAbstract):
    def __init__(self):
        price = 30
        camera_count = 2
        screen_size = 10
        super().__init__(price, camera_count, screen_size)

    def special_feature(self, x: int, y: int) -> int:
        '''輸入2個數字自動運算 p x 取 y 
        
        例如: 輸入(x=5, y=3)  回傳 60
        '''
        pass


if __name__ == "__main__":
    googlePhone = GooglePhoneStrategy()
    taiwanPhone = TaiwanPhoneStrategy()
    applePhone = ApplePhoneStrategy()