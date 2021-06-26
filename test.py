
import Validation as V

import Order as O


class OrderValue:

    def solve(self,d):
          
        data = d
        order_list = data.get('order_items',None)
        distance = data.get('distance',-1)
        offer = data.get('offer',None)
        custom_validation = V.Validation()
        if order_list and distance!=-1 and offer :
            if custom_validation.validate_OrderList(order_list)==False or custom_validation.validate_Distance(distance)==False or custom_validation.validate_Offer(offer)==False:
                return ({'message': 'Invalid order_items values'})
            else:
                obj = O.Order()
                obj._orderList = order_list
                obj._distance = distance
                obj._offer = offer 
                return ({'total_cost':obj.calculate_cost()})
        elif order_list and distance!=-1 and offer==None:
            if custom_validation.validate_OrderList(order_list)==False or custom_validation.validate_Distance(distance)==False:
                return ({'message': 'Invalid order_items values'})
            else:
                obj = O.Order()
                obj._orderList = order_list
                obj._distance = distance
                obj._offer = {}
                return ({'total_cost':obj.calculate_cost()})
        else:
            return ({'message': 'Insufficient data'})
            

o1 = OrderValue()
print(o1.solve({
  "order_items": [
    # {
    #   "name": "bread",
    #   "quantity": 2,
    #   "price": 2200
    # },
    # {
    #   "name": "butter",
    #   "quantity": 1,
    #   "price": 5900
    # }
  ],
  "distance": 1200,
  "offer": {
    "offer_type": "DELIVERY",
    "offer_val": 1000
  }
}))