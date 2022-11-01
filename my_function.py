
# creating functions

def myfunc():
    print("this is function demo")

# calling function
myfunc()


# pssing parameters into function
def add(a, b):
    total = a + b
    print("the sum of two number is ", total)

#call function
add(34, 87)


#passing multiple values as arguments to function
def add_all(*a):
    tsum = 0

    for i in a:
        tsum = tsum + i
    print("the sum of all list elements is ",tsum)

add_all(10,76,92,39,40,54,78)


#returning values

def mul(c,d):
    product = c * d
    return product

res = mul(23,4)
print("the product of two number is ",res)