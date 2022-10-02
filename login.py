

mynames = [1, 2, 3, 4, 5]
print(type(mynames))

def mystuff(x):
    a = 0
    while a < len(x):
        print(x[a])
        a = a + 1
        
mystuff(mynames)