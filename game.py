import random
gess = 0
num = 0
tr = 0
print("between")
try:
    min = int(input("min: "))
    max = int(input("max: "))
    num = random.randint(min, max) # min and max for random number generator
except:
    print("bad input plz try again")
    print("------------------------------------------")
while num != gess:
    try:
        gess = int(input("input: "))
        if num == gess:
            print("YOU WON!!!! and took {0} attempts".format(tr)) # logic for the "game"
        elif num > gess:
            print("the number in higher than your guess")
        else:
            print("the number in lower than your guess")
        print("------------------------------------------")
        tr = tr + 1
    except:
        print("bad input plz try again")


