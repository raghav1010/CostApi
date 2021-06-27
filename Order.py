from collections import defaultdict

class Order:
    """
    This is a class for a prototype Order as provided by request data.

    Attributes:
        orderList (List): A list of dictionaries containing all order_items data.

        distance (int): An integer field for distance of the placed order.

        offer (dictionary): A dictionary for offer applicable on the placed order.
        
        DELIVERY_COST(dictionary): A class variable implemented using hash map functonality 
                            to store price corresponding to distance for delivery cost purpose.
    """

    DELIVERY_COST = defaultdict()
    for i in range(0,500001):
        if i<=10000:
            DELIVERY_COST[i]=50*100 
        elif i>10000 and i<=20000:
            DELIVERY_COST[i]=100*100
        elif i>20000 and i<=50000:
            DELIVERY_COST[i]=500*100 
        else:
            DELIVERY_COST[i]=1000*100


    def __init__(self,orderList=[],distance=0,offer=defaultdict()):
        """
        The constructor for the Order class.
        """
        self._orderList = orderList
        self._distance = distance
        self._offer = offer 
    

    @property 
    def orderList(self):
        """
        The getter function for returning orderList for the referred instance.
        """
        return self.__orderList
    

    @property
    def distance(self):
        """
        The getter function for returning distance for the referred instance.
        """
        return self.__distance
    

    @property
    def offer(self):
        """
        The getter function for returning offer for the referred instance.
        """
        return self.__offer
    

    @orderList.setter
    def orderList(self,x):
        """
        The setter function for setting the values of orderList for the referred instance.
        """
        self.__orderList=x 
    

    @distance.setter
    def distance(self,x):
        """
        The setter function for setting the values of distance for the referred instance.
        """
        self.__distance=x
    

    @offer.setter
    def offer(self,x):
        """
        The setter function for setting the values of offer for the referred instance.
        """
        self.__offer=x 
    

    def calculate_cost(self):
        """
        The function for computing total amount for the referred order instance.

        Returns:
            amount(Integer): Returns amount in paise for the order instance referred.
        """
        amount = Order.DELIVERY_COST[self._distance]
        for i in self._orderList:
            amount = amount + i.get('price')*i.get('quantity')
        
        if len(self._offer)==0:
            return amount 
        
        if self._offer.get('offer_type')=="FLAT":
            amount = amount - min(amount,self._offer.get('offer_val'))
        
        else:
            amount = amount - min(amount,Order.DELIVERY_COST[self._distance])
        
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

