k,n,w=map(int,input().split())
t= ((k + k*w)*w // 2)
if t<=n:
  print(0)
else:
  kk = t - n
  print(kk)