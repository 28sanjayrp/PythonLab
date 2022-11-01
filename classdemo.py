
class car:

    def getspeed(self):
        print("the speed of the car is 180 kmph")

#creating obj

Bmw = car()
Audi = car()


#call obj

car.getspeed(Bmw)
car.getspeed(Audi)


class automobile:

    def __init__(self,na,co,cr,ms):
        self.name_of_automobile = na
        self.company = co
        self.color = cr
        self.max_speed = ms

    def mydef(self):
        print("\n automobile type :", self.name_of_automobile, "\n automobile company :",self.company, "\n color :",self.color, "\n maximum speed :",self.max_speed)

#creating obj
bmw = automobile("Car","Bmw","red",180)
audi = automobile("Bike","Splender","black",90)
ferrari = automobile("car","Ferrari","silver",200)

automobile.mydef(bmw)
automobile.mydef(audi)
automobile.mydef(ferrari)