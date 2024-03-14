def wrong(w,k):
  for i in range(k):
    num  = [str(j) for j in str(w)]
    if num[-1] == '0':
      w = w//10
    elif num[-1] != '0':
      w = w-1
  return w

n,k = map(int,input().split())
print(wrong(n,k))

