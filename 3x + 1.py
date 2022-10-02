#odd=3x+1
#even=/2
while 1:
    number = 0
    steps = 0
    hnumber = 0
    a = 0
    FizzBuzz = 0
    Buzz = 0
    Fizz = 0
    number = int(input("number: "))
    p = input("print?(answer nothing for no): ")
    pr = bool(p)
    bruh = number
    while number != 1:
        a = number
        if number > hnumber:
           hnumber = number
        else:
           pass
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
        if a % 5 == 0:  # this is a comment
            if a % 3 == 0:
              if pr == True:
                 print("FizzBuzz")
              FizzBuzz = FizzBuzz + 1
            else:
              if pr == True:
                 print("Buzz")
              Buzz = Buzz + 1
        elif a % 3 == 0:
          if pr == True:
             print("Fizz")
          Fizz = Fizz + 1
        else:
           if pr == True:
              print(a)
           pass
    print("-------------------")
    print("input: " + str(bruh))
    print("steps: " + str(steps))
    print("highest number: " + str(hnumber))
    txt = "Fizz: {0} Buzz: {1} FizzBuzz: {2}"
    print(txt.format(Fizz, Buzz, FizzBuzz))
    print("-------------------")

