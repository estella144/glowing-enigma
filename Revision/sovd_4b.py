print("4b - Calculating SA and area of a cuboid")
s1 = int(input("Side 1 length: "))
s2 = int(input("Side 2 length: "))
s3 = int(input("Side 3 length: "))

f1 = s1 * s2
f2 = s1 * s3
f3 = s2 * s3

sa = 2 * (f1 + f2 + f3)
vol = s1 * s2 * s3

print(f"Surface area: {sa}")
print(f"Volume      : {vol}")
