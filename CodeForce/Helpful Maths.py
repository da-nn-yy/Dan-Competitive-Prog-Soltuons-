def help(h):
  s = [h]
  hl = s[0]

  num = [int(i) for i in hl.split("+")]
  sorte = sorted(num)
  sort  = "+".join(str(i) for i in sorte)
  return sort
  
n = str(input())
print(help(n))
  