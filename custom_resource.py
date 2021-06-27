#flask,flask_restful imports
from flask import jsonify,request,abort
from flask.wrappers import Response
from flask_restful import Resource
import json

#custom packages imports
import validation as V
import order as O


class OrderValue(Resource):
    """
    This is a resource class for handling http requests (POST,GET,PUT,etc)
    """
    def post(self):
        """
        This is function to handle the post request,
        validate the incoming data,
        create objects for the order data,

        Return : (json_data,http_code)
            returns data in json format with valid http_codes
        """

        try:
            data = request.get_json()
        except:
            return {'message':'Missing data'},400
    
        if data == None:
            return {'message':'No data provided'},422
        order_list = data.get('order_items',None)
        distance = data.get('distance',None)
        offer = data.get('offer',None)
        custom_validation = V.Validation()
        
        if order_list and distance!=-1 and offer :
            vo = custom_validation.validate_OrderList(order_list)
            vd = custom_validation.validate_Distance(distance)
            vof = custom_validation.validate_Offer(offer)
            if not vo or not vd or not vof:
                mes={}
                if not vo:
                    mes['message 1']='Invalid order_list values'
                if not vd:
                    mes['message 2']='Invalid distance'
                if not vof:
                    mes['message 3']='Invalid offer'
                return mes,422
            else:
                obj = O.Order()
                obj._orderList = order_list
                obj._distance = distance
                obj._offer = offer 
                
                return {'total_cost':obj.calculate_cost()},200
                
        elif order_list and distance!=-1 and offer==None:
            vo = custom_validation.validate_OrderList(order_list)
            vd = custom_validation.validate_Distance(distance)
            if not vo or not vd :
                mes={}
                if not vo:
                    mes['message 1']='Invalid order_list values'
                if not vd:
                    mes['message 2']='Invalid distance'
                return mes,422
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
            
            