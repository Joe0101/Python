class sqr:
    def __init__(self):
       self.price=5000
    def area(self,side):
        self.area=side*side
        print("Area:",self.area)
    def perimet(self,side):
      self.peri=4*side
      print("Perimit:",self.peri)
    def price(self,side):
        self.pri=side*self.price
        print(self.pri)
side=int(input())
s=sqr()
s.area(side)
s.perimet(side)
s.price(side)
