n = int(input())
ps=0 
for i in range(n):
  p,v,t=map(int, list(input().split()))
  if p+v+t >= 2:
    ps += 1
print(ps)
    
  