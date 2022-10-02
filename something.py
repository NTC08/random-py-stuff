num = int(input("num: "))
print("###########")
if num > 0:
    print("- positive")
elif num < 0:
    print("- negative")
else:
    print(num)
if num % 2 == 0:
    print("- even")
else:
    print("- odd")
if num % 5 == 0:
    if num % 3 == 0:
        print("- fizzbuzz")
    else:
        print("- buzz")
elif num % 3 == 0:
    print("- fizz")
else:
    print("-",num)
print("###########")