from flask import Flask
from flask_restful import Api
from custom_resource import OrderValue
app = Flask(__name__)

api = Api(app)

api.add_resource(OrderValue, '/api/v1.0/OrderValue')

if __name__ == '__main__':
  
    app.run(debug = True)
