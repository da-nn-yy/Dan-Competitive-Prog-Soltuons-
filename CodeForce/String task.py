inp = input().lower()

vowel = ["A", "E", "I", "O", "U","Y","a", "e", "i", "o", "u","y"]
r = ""
for char in inp:
  if char not in vowel:
    r += "." + char
    
print (r)