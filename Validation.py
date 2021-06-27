
class Validation:
    """
    This is a class for custom validations on all request data.
    """

    def validate_Name(self,x):
        """
        The function to validate order_item Name.

        Parameters:
            x(Name): The Name of the order_item.
        
        Returns:
            Boolean value: true or false is returned depending on the validation.
        """

        if x==None:
            return False
        if len(x)<4 or len(x)>20:
            return False
        if x.isalpha()==False:
            return False
        return True


    def validate_Price(self,x):
        """
        The function to validate order_item Price.

        Parameters:
            x(Price): The price of the order_item.
        
        Returns:
            Boolean value: true or false is returned depending on the validation.
        """

        if x==None:
            return False
        if type(x)!=int:
            return False 
        if x<0 or x>10000:
            return False
        return True 


    def validate_Quantity(self,x):
        """
        The function to validate order_item Quantity.

        Parameters:
            x(Quantity): The Quantity of the order_item.
        
        Returns:
            Boolean value: true or false is returned depending on the validation.
        """

        if x==None:
            return False
        if type(x)!=int:
            return False 
        if x<0 or x>20:
            return False
        return True 


    def validate_Item(self,item):
        """
        The function to validate a given order_item.

        Parameters:
            item(dictionary): The order_item comprising of 
                { 
                    name:"",
                    price:,
                    quantity:
                } 
                as key:value pairs.

        Returns:
            Boolean value: true or false is returned depending on the validation.
        """

        if item==None:
            return False
        item_name = item.get('name',None)
        item_price = item.get('price',None)
        item_quantity = item.get('quantity',None)

        if self.validate_Name(item_name) and self.validate_Quantity(item_quantity) and self.validate_Price(item_price):
            return True 
        else:
            return False

    def validate_OrderList(self,orders):
        """
        The function to validate each order_item from orders.

        Parameters:
            orders(list of dictionaries): List comprising of each order_item as dictionary values
                [
                    { 
                        name:"",
                        price:,
                        quantity:
                    } ,

                    { 
                        name:"",
                        price:,
                        quantity:
                    }
                
                ]

        Returns:
            Boolean value: true or false is returned depending on the validation.
        """
        if orders==None:
            return False
        for item in orders:
            if self.validate_Item(item)==False:
                return False
        return True


    def validate_Distance(self,x):
        """
        The function to validate distance for an order.

        Parameters:
            x(Distance): The Distance(Integer value) corresponding to the order.
        
        Returns:
            Boolean value: true or false is returned depending on the validation.
        """

        if x==None:
            return False
        if type(x)!=int:
            return False 
        if x<0 or x>500000:
            return False
        return True 
    

    def validate_OfferType(self,x):
        """
        The function to validate offer_type for applicable offer for an order.

        Parameters:
            x(Offer_Type): The offer_type(String value) for applicable offer for an order.
        
        Returns:
            Boolean value: true or false is returned depending on the validation.
        """

        if x==None:
            return False
        if x=="FLAT" or x=="DELIVERY":
            return True 
        else:
            return False
        

    def validate_OfferValue(self,x):
        """
        The function to validate offer_type for applicable offer for an order.

        Parameters:
            x(Offer_Value): The offer_value(Integer value) for applicable offer for an order.
        
        Returns:
            Boolean value: true or false is returned depending on the validation.
        """

        if x==None:
            return False
        if type(x)!=int:
            return False 
        if x<0 :
            return False
        return True 

    def validate_Offer(self,offer):
        """
        The function to validate offer applicable for an order.

        Parameters:
            offer(dictionary): The offer comprising of 
                { 
                    offer_type:"",
                    offer_value:
                } 
                as key:value pairs..
        
        Returns:
            Boolean value: true or false is returned depending on the validation.
        """

        if offer==None:
            return False
        offer_type = offer.get('offer_type','-1')
        offer_val = offer.get('offer_val',0)

        if self.validate_OfferType(offer_type) and self.validate_OfferValue(offer_val):
            return True
        else:
            return False
