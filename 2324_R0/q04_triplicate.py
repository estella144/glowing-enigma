e1 = input()
e2 = input()
e3 = input()
if (e1 != e2) and (e1 != e3):
  print("BOTH MISMATCH")
elif e1 != e2:
  print("ENTRY 2 MISMATCH")
elif e1 != e3:
  print("ENTRY 3 MISMATCH")
else:
  print("OK")
