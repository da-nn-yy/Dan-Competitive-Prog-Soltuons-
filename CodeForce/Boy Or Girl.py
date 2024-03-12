borg = input().lower()
bg= []
for char in borg:
     if char not in bg:
            bg.append(char)
if (len(bg)%2) == 0:
      print("CHAT WITH HER!")
else:
      print("IGNORE HIM!")
    

