n = int(input())
bit = 0
for i in range(n):
  x=input()
  if (x == '++X') or (x == 'X++'):
    bit += 1
  elif (x == '--X') or  (x == 'X--'):
    bit -= 1

print(bit)

