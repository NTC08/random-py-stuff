# odd=3x+1
# even=/2
input = input("input: ")
pr = False
bruh = 1  # number
hsteps = 0  # highest steps
FizzBuzz = 0
Buzz = 0
Fizz = 0
numberh = 0  # track for hightest number
hnumber = 0  # hightest number
stepnumber = 0  # track for hightest steps
while bruh <= int(input):
    number = 0
    steps = 0
    number = bruh
    while number != 1:  # the3x+1part
        if number % 2 == 0:
            number = number / 2
            steps = steps + 1
            if pr == True:
                print(number)
        else:
            number = (number * 3) + 1
            steps = steps + 1
            if pr == True:
                print(number)

        if number > hnumber:  # hightest numbers tracker
            hnumber = number
            numberh = bruh

        if steps > hsteps:  # hightest steps tracker
            hsteps = steps
            stepnumber = bruh
        else:
            pass
        if number % 5 == 0:  # the fizzbuzz part
            if number % 3 == 0:
                if pr == True:
                    print("FizzBuzz")
                FizzBuzz = FizzBuzz + 1
            else:
                if pr == True:
                    print("Buzz")
                Buzz = Buzz + 1
        elif number % 3 == 0:
            if pr == True:
                print("Fizz")
            Fizz = Fizz + 1
        else:
            if pr == True:
                print(number)
            pass
    #print("-------------------")
    #print("number: " + str(bruh))
    #print("steps: " + str(steps))
    #print("-------------------")
    bruh = bruh + 1

print("-------------------")
print("input: " + str(input))
print("highest steps: " + str(hsteps))  # print info
print("from number: " + str(stepnumber))
print("highest number: " + str(hnumber))
print("number from: " + str(numberh))
txt = "Fizz: {0} Buzz: {1} FizzBuzz: {2}"
print(txt.format(Fizz, Buzz, FizzBuzz))
print("-------------------")
