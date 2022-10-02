#starting a coffe shop
#robot barista
def mystuff(mylist):
    a = 0
    while a < len(mylist):
        print(mylist[a])
        a = a + 1
while 1:
    menu = ["coffe", "black coffe", "latai", "cupcake"]
    print("welcom to coffe shop!!!!!!!!!!!")
    name = str(input("what is your name \n"))
    if name == "bob":
        print("go away")
        exit()
    else:
        print("welcome " + name + " to my shop")
    print("this is our menu")
    mystuff(menu)
    order = input("what do you want, " + name + "\n")
    number = input("how many " + order + " do you want?\n")
    price = 8
    added = int(number) * int(price)
    print("that will be " + str(added) + " USD")
