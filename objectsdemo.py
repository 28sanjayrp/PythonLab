
#simple object demo

class Person:

    def __init__(self):
        self.name = "sam"
        self.age = 23
        self.gender = "male"

    def talk(self):
        print("Hi I'm ",self.name)

    def vote(self):
        print("I'm",self.age," and I have voting power")

#creating objects

obj = Person()

#calling methods using object.
Person.talk(obj)



#multiple objects
#creating class for object
class Employee():

    def __init__(self,n,a,g):   #constructor
        self.name = n
        self.age = a
        self.gender = g

     #creating functions
    def talk(self):
        print("Hi my name is ",self.name)

    def vote(self):
        if self.age < 18 :
            print("I'm not eligible to vote because I'm ",self.age,"year old")
        else:
            print("I'm eligible to vote because I'm ",self.age,"year old")


#creating objects
obj1 = Employee("sanjay",24,"male")

obj2 = Employee("sara",17,"female")

#calling methods using object
Employee.talk(obj1)
Employee.vote(obj1)


Employee.talk(obj2)
Employee.vote(obj2)
Person.vote(obj)