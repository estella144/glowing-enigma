nums = []
for i in range(5):
  n = int(input())
  nums.append(n)

nums.sort()
nums = [str(num) for num in nums]

for num in nums:
  print(num[1], end="")
