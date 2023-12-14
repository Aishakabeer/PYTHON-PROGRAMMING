class car():
    def __init__(self, c,p,km):
       self.color = c
       self.price = p
       self.kilometer=km
    def car_price(self):
        return self.price
    def car_color(self):
        return self.color
    def car_kilometer(self):
        return self.kilometer
car1=car("red",23400,8000)
car2=car("white",75400,1500)
print("Color of 1 st car is ",car1.car_color()," and color of 2 nd car is ",car2.car_color())
if(car1.car_price()>car2.car_price()):
    pp=car1.car_price()-car2.car_price()
    print("Price of car 1 is more than car 2 -",pp)
else:
    pp=car2.car_price()-car1.car_price()
    print("Price of car 2 is more than car 1 -",pp)
total=car1.car_kilometer()+car2.car_kilometer()
print("Total kilometer of 2 cars is ",total)
