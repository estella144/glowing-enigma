wl = int(input())
wd = 0
wi = 0

while wl > 5:
  wi += wd + 5
  wl -= 5
  wd += 5
wi += (wd + wl)
print(wi)
