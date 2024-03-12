n = int(input())
hi = []
sum_x =sum_y= sum_z = 0
for i in range(n):
  x,y,z = map(int,input().split())
  hi.append((x,y,z))
sum_x,sum_z,sum_y = 0,0,0
for j in hi:
  x,y,z = j
  sum_x += x
  sum_y += y
  sum_z += z
if sum_x == 0 and sum_z == 0 and sum_y == 0:
  print("YES")
else:
  print("NO")
  