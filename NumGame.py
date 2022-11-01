import random

rnum = random.randint(1000, 9999)  # rnum-> random number bwn 11-99.

print(rnum)

# user need to guess the number with position

unum = int(input("User input number"))  # unum-> stores the user input number

while unum != 10:  # if unum is 10 then game should quit.
    num = rnum  # random number(rnum) is assigned to num(new var)
    count_corr_pos = 0  # corr_por -> stores the count of number user entered correct position as same as rnum

    while num > 0:
        rem_of_num = num % 10
        rem_of_unum = unum % 10
        num = num // 10
        unum = unum // 10

        if rem_of_num == rem_of_unum:
            count_corr_pos = count_corr_pos + 1

    if count_corr_pos == 4:
        print("oh! Great finally you Guessed exact same number")
        break
    else:
        print("you entered only %d number exact same with respect to their position." % count_corr_pos)
        unum = int(input("User input number"))
else:
    print("you exit from the game")
