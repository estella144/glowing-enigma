m = int(input())
for i in range(1_000):
  if (i+1)**3 > m:
    break
  print((i+1)**3)
