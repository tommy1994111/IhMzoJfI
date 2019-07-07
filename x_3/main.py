import os
from typing import List

FOLDER_PATH = os.path.join('.', 'ilovecoffee')
CSV_PATH = os.path.join(FOLDER_PATH, 'customers.csv')

class CustomerGenerator(object):
    '''客戶資料產生器
    
    結構如下:
    ```
    customer_id,customer_name, customer_mobile, frequency
    "y88xTa", "tom.y88xTa","+886938766119", "4"
    "uYt49x", "peter.uYt49x","+886938922440", "6"
    "p9g5As", "hank.p9g5As","+886918300227", "1"
    .....
    ```
    '''
    
    CUSTOMER_NAME_PREFIX = ['tom', 'peter', 'hank', 'jim', 'taylor', 'abe', 'steph',
        'chi', 'chino', 'hiromi']
    CUSTOMER_MOBILE_PREFIX = "+8869"
    
    def generateIds(self, amount: int) -> List[str]:
        '''產生 customer_id
        
        長度8, 由數字[0-9], 大寫[A-Z]，小寫[a-z]隨機組成，但開頭不可為數字
        '''
        pass

    def generateNames(self, id_list: List[str]) -> List[str]:
        '''產生 customer_name

        隨意用10個英文名字建立一組list: 如 ['tom','peter','hank'....]
        將customer_id與隨機從 name list 中取出的一個元素進行合併，例如產出"tom.y88xTa"
        '''
        pass

    def generateMobiles(self, amount: int) -> List[str]:
        '''產生 customer_mobile
        
        隨機產生一個+886開頭的台灣電話號碼，若新產出的電話號碼有重複，則需要重新產生
        '''
        pass

    def generateFrequencies(self, amount: int) -> List[int]:
        '''產生 frequency
        
        從 [0-20] 中隨機進行選擇
        '''
        pass

    def generateCustomers(self, amount):
        '''產生客戶資料'''
        pass

class CsvHanlder(object):
    def __init__(self):
        self.detect_folder()

    def detect_folder(self):
        '''偵測相同目錄下是否存在一個 ilovecoffee 資料夾，若無則建立，有則略過'''
        os.makedirs(FOLDER_PATH, exist_ok=True)
    
    def create_csv(self):
        '''隨機寫入 500 筆客戶資料至 /ilovecoffee/customers.csv'''
        pass

    def calculate_csv(self):
        '''讀取 /ilovecoffee/customers.csv，並列印出frequency 的中數、眾數及平均數 (取至小數點後 5 位)'''
        pass

if __name__ == "__main__":
    handler = CsvHanlder()
    handler.create_csv()
    handler.calculate_csv()