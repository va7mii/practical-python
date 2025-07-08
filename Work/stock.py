from typedproperty import typedproperty, String, Integer, Float
class Stock:
    # _shares is the real box, shares is a disguise
    #__slots__= ('name','_shares','price')
    
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    
    
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares # actually calls the shares.setter behind the scenes
        self.price = price
    
    def __repr__(self):
        return f'Stock(\'{self.name}\', {self.shares}, {self.price})'
    
    @property
    def cost(self):
        return self.shares * self.price # calls the getter function secretely

    def sell(self, shares):
        self.shares -= shares
    

    
    