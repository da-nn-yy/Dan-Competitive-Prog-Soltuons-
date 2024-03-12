n = int(input())
w = []

for i in range(n):
  w.append(input())
for j in w:
  if len(j) > 10:
    print(j[0] + str(len(j)-2) + j[-1])
  else:
    print(j)


