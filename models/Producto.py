class Producto:
    
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        
    def check_stock(self, neccesity):
        if self.stock < neccesity:
            return f"There is not enough stock. Stock = {self.stock}. Solicited {neccesity}."
        else:
            return f"There is enough stock. Stock = {self.stock}. Solicited {neccesity}."
        
    def update_stock(self, new_stock):
        self.stock = new_stock
    
    def __str__(self):
        return f"My id is {self.id}, my name is {self.name}, my price is {self.price} and my stock is {self.stock}"
    
class ProductoElectronico (Producto):
    def __init__(self, id, name, price, stock, garanty):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.garanty = garanty

    def __str__(self):
        return f"My id is {self.id}, my name is {self.name}, my price is {self.price}, my stock is {self.stock} and my garanty is {self.garanty}"
    
class ProductoRopa (Producto):
    def __init__(self, id, name, price, stock, size, color):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.size = size
        self.color = color

    def __str__(self):
        return f"My id is {self.id}, my name is {self.name}, my price is {self.price}, stock is {self.stock}, my size is {self.size} and my color is {self.color}"