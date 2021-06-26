from flask.wrappers import Response
from flask_restful import Resource
from flask import jsonify,request
import Validation as V

import Order as O
import json

class OrderValue(Resource):

    def post(self):
          
        data = request.get_json()
        if data ==None:
            return {'message':'No data provided'},422
        order_list = data.get('order_items',None)
        distance = data.get('distance',-1)
        offer = data.get('offer',None)
        custom_validation = V.Validation()
        if order_list and distance!=-1 and offer :
            if custom_validation.validate_OrderList(order_list)==False or custom_validation.validate_Distance(distance)==False or custom_validation.validate_Offer(offer)==False:
                return {'message':'Invalid order values'},422
            else:
                obj = O.Order()
                obj._orderList = order_list
                obj._distance = distance
                obj._offer = offer 
                
                return {'total_cost':obj.calculate_cost()},200
                
        elif order_list and distance!=-1 and offer==None:
            if custom_validation.validate_OrderList(order_list)==False or custom_validation.validate_Distance(distance)==False:
                return {'message':'Invalid order values'},422
                # return Response({'message': 'Invalid order_item values'}, status=401, mimetype='application/json')
            else:
                obj = O.Order()
                obj._orderList = order_list
                obj._distance = distance
                return {'total_cost':obj.calculate_cost()},200
                # return Response({'total_cost':obj.calculate_cost()}, status=200, mimetype='application/json')
                
        else:
            return {'message':'Insufficient data'},422
            # return Response({'message': 'Insufficient data'}, status=401, mimetype='application/json')
            
            