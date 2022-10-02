while 1:
   while 1:
       a = 1
       FizzBuzz = 0
       Buzz = 0
       Fizz = 0
       p = input("print?(answer nothing for no): ")
       n = input("input: ")
       print("-------------------------")
       pr = bool(p)
       while a <= int(n):
           if a % 5 == 0:      #this is a comment
               if a % 3 ==0:
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
           a = a + 1
       txt = "Fizz: {0} Buzz: {1} FizzBuzz: {2}"
       print(txt.format(Fizz, Buzz, FizzBuzz))
       print("-------------------------")
