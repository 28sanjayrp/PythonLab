#Inheritance

#class1
class class1:

    def __init__(self,n,c,s):
        self.name = n
        self.color = c
        self.speed = s

    def mydef(self):
        print("\n Car name :", self.name, "\n Car color :",self.color, "\n speed of car :",self.speed)

#creating obj
bmw = class1("Bmw","red",180)
audi = class1("Audi","black",190)
ferrari =class1("Ferrari","silver",200)

#obj calling
bmw.mydef()
audi.mydef()
ferrari.mydef()


#class2

class class2(class1):
    def getspeed(self):
        print("\n corrent speed :",self.speed)

obj1 = class2("ford","red",120)

obj1.getspeed()                                #o/p : corrent speed : 120




#class3
class class3(class1):
    def getcarnames(self):
        print("\n car name : ", self.name)

obj2 = class3("cord","blue",140)

obj2.getcarnames()                                      #o/p :  car name :  cord

#mix
print("\n Inherating outputs as below")
obj1.mydef()             #obj1 is child object and mydef is parent class's function.
obj1.getspeed()

obj2.mydef()             #obj2 is another child object and mydef is parent class's function.
obj2.getcarnames()

