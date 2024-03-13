def lucky(l):
  num = str(l)
  count = 0

  for i in num:
    if i == 4 or i == 7:
      count =+ 1
  return count
  

n = int(input())
print(lucky(n))
