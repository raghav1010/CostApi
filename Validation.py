
class Validation:

    def validate_Name(self,x):
        if len(x)<4 or len(x)>20:
            return False
        elif x.isalpha()==False:
            return False
        return True

    def validate_Price(self,x):
        if type(x)!=int:
            return False 
        if x<0 or x>10000:
            return False
        return True 


    def validate_Quantity(self,x):
        if type(x)!=int:
            return False 
        if x<0 or x>20:
            return False
        return True 

    def validate_Item(self,item):
        item_name = item.get('name',"-1")
        item_price = item.get('price',-1)
        item_quantity = item.get('quantity',-1)

        if self.validate_Name(item_name) and self.validate_Quantity(item_quantity) and self.validate_Price(item_price):
            return True 
        else:
            return False

    def validate_OrderList(self,orders):
        
        for item in orders:
            if self.validate_Item(item)==False:
                return False
        return True

    def validate_Distance(self,x):
        if type(x)!=int:
            return False 
        if x<0 or x>500000:
            return False
        return True 
    
    def validate_OfferType(self,x):

        if x=="FLAT" or x=="DELIVERY":
            return True 
        else:
            return False
        

    def validate_OfferValue(self,x):
        
        if type(x)!=int:
            return False 
        if x<0 :
            return False
        return True 

    def validate_Offer(self,offer):
        
        offer_type = offer.get('offer_type','-1')
        offer_val = offer.get('offer_val',None)

        if self.validate_OfferType(offer_type) and self.validate_OfferValue(offer_val):
            return True
        else:
            return False
