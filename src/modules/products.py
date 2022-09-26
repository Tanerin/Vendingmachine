class Product:
    def __init__(self, name, price, quantity):
        self.NameOfProduct = name
        self.PriceOfProduct = price
        self.QuantityOfProduct = quantity
    
    def setPrice(self, newprice):
        self.PriceOfProduct = newprice
    
    def getPrice(self):
        price = self.PriceOfProduct
        return price 
    
    def setQuantity(self, newquantity):
        self.QuantityOfProduct = newquantity
    
    def getQuantity(self):
        quantity = self.QuantityOfProduct
        return quantity