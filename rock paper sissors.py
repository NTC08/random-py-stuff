import random # my frist program :D
while 1:
   cs = 0
   ps = 0
   while ps or cs < 30:
      print("-----------------")
      p = int(input("1=rock 2=sis 3=paper input== ")) # the player input
      c = random.randint(1, 3)
      print("-----------------")
      print("player play:", p)
      print("computer play: ", c)
      print("-----------------")
      if c == p:  # make sure the the input is right
          print("tie")
      elif p >= 4:
           print("incorent input")
      elif bool(p) == False:
          print("incorent input")
      else:
           p = int(p)
           if p == 1 and c == 2: # the brain
               print("player win")
               ps = ps + 1
           elif p == 2 and c == 3:
               print("player win")
               ps = ps + 1
           elif p == 3 and c == 1:
               print("player win")
               ps = ps + 1
           else:
               print("computer win")
               cs = cs + 1
      print("-----------------")
      print("player score:" + str(ps))
      print("computer score:" + str(cs))