from threading import *

class Demo:
    def show(self):
        for j in range(5):
            print("\n",j+1,". this is child thread")
obj = Demo()
t = Thread(target=obj.show())
t.start()

#this is parent thraed
for i in range(5):
    print("\n",i+1, ". this is parent thread")