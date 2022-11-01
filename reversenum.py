n = int(input("enter a number"))
rn = 0
while n>0:
    c = n % 10
    rn = rn * 10 + c
    n=n//10
print(rn)