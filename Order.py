from collections import namedtuple
from collections import defaultdict


class Order:

    delivery_cost = defaultdict()
    for i in range(0,500001):
        if i<=10000:
            delivery_cost[i]=50*100 
        elif i>10000 and i<=20000:
            delivery_cost[i]=100*100
        elif i>20000 and i<=50000:
            delivery_cost[i]=500*100 
        else:
            delivery_cost[i]=1000*100

    def __init__(self,orderList=[],distance=0,offer=defaultdict()):
        self._orderList = orderList
        self._distance = distance
        self._offer = offer 
    
    @property 
    def orderList(self):
        return self.__orderList
    
    @property
    def distance(self):
        return self.__distance
    
    @property
    def offer(self):
        return self.__offer
    
    @orderList.setter
    def orderList(self,x):
        self.__orderList=x 
    
    @distance.setter
    def distance(self,x):
        self.__distance=x
    
    @offer.setter
    def offer(self,x):
        self.__offer=x 
    
    def calculate_cost(self):

        amount = Order.delivery_cost[self._distance]
        for i in self._orderList:
            amount = amount + i.get('price')*i.get('quantity')
        
        if len(self._offer)==0:
            return amount 
        
        if self._offer.get('offer_type')=="FLAT":
            amount = amount - min(amount,self._offer.get('offer_val'))
        
        else:
            amount = amount - min(amount,Order.delivery_cost[self._distance])
        
        return amount
    

# obj = Order()
# obj._orderList = [
#     {
#       "name": "bread",
#       "quantity": 2,
#       "price": 2200
#     },
#     {
#       "name": "butter",
#       "quantity": 1,
#       "price": 5900
#     }
#   ]

# obj._distance = 1200
# obj._offer = {
 
#   }
# print(obj.calculate_cost())

