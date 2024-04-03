n,h = map(int,input().split())
person = list(map(int,input().split()))
count = 0
for i in range(n):
  if person[i] > h:
    count = count + 2
  else:
    conut = count + 1
   
print(count)