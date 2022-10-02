import random
def mystuff(*k):
    print("1 input was", len(k), "long")
    for x in k:
        print(x)

good = {
      "kkkd": "lllll",
      "bruhhhh": "deez nuts"
}

def mythings(**p):
    print("2 input was", p["bruh"])

def randnum(min, max):
    x = random.randint(min, max)
    return(x)

print(randnum(1, 10000))

class bruh:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    x = 0

p1 = bruh("deez", "nuts")
p2 = bruh("deez2", "nuts2")
print(good["bruhhhh"])
if good["bruhhhh"] == "deez nuts":
    print("test complet")
else:
    print("bruh wtf")
good["deez"] = "HAHA"
print(good.keys())
p = good["deez"]
print(p)
