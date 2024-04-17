cw = ""
s = []
while cw != "stop":
  cw = input()
  s.append(cw)
del s[-1]
lw = s[-1]
del s[-1]
for i in s:
  print(i, end=" ")
print(lw)
