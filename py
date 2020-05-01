#Royal Orchid is a florist. They want to be alerted when stock of a flower goes below a particular level. 
#The flowers are identified using name, price per kg and stock available (in kgs).
#Write a Python program to implement the above requirement.

#lex_auth_012727119215337472135
#Start writing your code here
class Flower:
    def __init__(self, lower_name, price_per_kg, stock_available):
        self.__flower_name=None
        self.__price_per_kg=None
        self.__stock_available=None
        
    def set_flower_name(self,flower_name):

        self.__flower_name=flower_name

    def get_flower_name(self):

        return self.__flower_name
        
    def set_price_per_kg(self,price_per_kg):

        self.__price_per_kg=price_per_kg

    def get_price_per_kg(self):

        return self.__price_per_kg
        
    def set_stock_available(self,stock_available):

        self.__stock_available=stock_available

    def get_stock_available(self):

        return self.__stock_available
        
    
    def validate_flower_name(self):

        if self.__flower_name==Orchid or self.__flower_name==Rose or self.__flower_name==Jasmine:

            return True

        else:

            return False
   
    
