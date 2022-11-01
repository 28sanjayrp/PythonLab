#try and except

x = [1,2,3,"simplilearn"]
length = 0
i = 0

try:
    while x[i]:
        length +=1
        i+=1
except IndexError:
    print(length)