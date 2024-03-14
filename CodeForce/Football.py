def foot(f):
  count = 1
  for i in range(1,len(f)):
    if f[i] == f[i-1]:
      count += 1
      if count == 7:
        return "YES"
    else:
      count = 1
  return "NO"
  
n  = (input())
print (foot(n))