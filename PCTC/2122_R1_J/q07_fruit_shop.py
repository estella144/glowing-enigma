a = 50
o = 50

while (a > 0) and (o > 0):
    f = input()
    n = int(input())
    if f == "APPLES":
        a -= n
    else:
        o -= n

print(max(a, o))
