nums = []
valid = 0

for i in range(12):
    x = int(input())
    nums.append(x)

for n in nums:
    n = str(n)
    f = int(n[0])
    l = int(n[-1])
    if f-l in (1, -1):
        valid += 1

print(valid)
