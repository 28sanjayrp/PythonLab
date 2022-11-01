var = int(input("Enter the number which is multiple 7"))

while var % 7 != 0:
    var = int(input("Enter the number which is multiple 7"))
else:
    print("%d finally you entered multiple 7" % var)
