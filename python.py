import random
number = random.randint(1, 100)

def makenumber(a, b):
    c = random.randint(a, b)
    return c
    
print(makenumber(1, 20000))