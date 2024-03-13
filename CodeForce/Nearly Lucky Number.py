def lucky(l):
  num  = str(l)
  count = 0

  for i in num:
    if i == '4' or  i == '7':
      count += 1
  if count == 4 or count == 7:
    return "YES"
  else:
    return "NO"
  
n = int(input())
print(lucky(n))