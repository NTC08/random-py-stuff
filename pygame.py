from cmath import sin
import random
import math
yes = 0
no = 0
numinput = ""

while 1 == 1:
    a = random.randint(1, 21)
    b = random.randint(1, 21)
    ran = random.randint(1, 4)

    if ran == 1:
        print(str(a) + " + " + str(b))
        numinput = int(input("input number: "))
        print("------------------")
        if int(numinput) == a + b:
            print("YES!!")
            yes = yes + 1
        else:
            print("no ans = " + str(a + b))
            no = no + 1
        print("right: " + str(yes))
        print("wrong: " + str(no))
    elif ran == 2:
        print(str(a) + " - " + str(b))
        numinput = int(input("input number: "))
        print("------------------")
        if int(numinput) == a - b:
            print("YES!!")
            yes = yes + 1
        else:
            print("no ans = " + str(a - b))
            no = no + 1
        print("right: " + str(yes))
        print("wrong: " + str(no))
    elif ran == 3:
        print(str(a) + " * " + str(b))
        numinput = int(input("input number: "))
        print("------------------")
        if int(numinput) == a * b:
            print("YES!!")
            yes = yes + 1
        else:
            print("no ans = " + str(a * b))
            no = no + 1
        print("right: " + str(yes))
        print("wrong: " + str(no))
    elif ran == 4:
        while a % b != 0:
           a = random.randint(1, 40)
           b = random.randint(1, 40)
        print(str(a) + " / " + str(b))
        numinput = int(input("input number: "))
        print("------------------")
        if int(numinput) == a / b:
            print("YES!!")
            yes = yes + 1
        else:
            print("no ans = " + str(a / b))
            no = no + 1
        print("right: " + str(yes))
        print("wrong: " + str(no))
    print("------------------")