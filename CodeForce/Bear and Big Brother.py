a,b = map(int, input().split())
c = 1
while a<=b:
  a *= 3
  b *= 2
  if a <= b:
    c += 1
  else:
    break
print (c)

