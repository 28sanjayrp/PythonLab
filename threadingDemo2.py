# creating thread importing thread class in user defined class

from threading import *


class MyThread(Thread):
    # Here "MyThread" is user defined class  and "Thread" is default class, and we are importing thread class in user
    # defined class
    def run(self):
        for j in range(5):
            print("\n this is child thread")


t = MyThread()
t.start()

for i in range(5):
    print("\n this is main thread")

#the output we get is mixup of child and parent thread print statements. every run it will generate different mixup values.
