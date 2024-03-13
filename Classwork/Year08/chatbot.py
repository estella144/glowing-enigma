from base64 import b64encode as e
from base64 import b64decode as d

c1 = b'dG9jcA=='

c = input("What do you like? ").lower()
cb = bytes(c, "utf-8")

if cb == d(c1):
    print("u still think thats the hardest one?")
elif c == "rice":
    print("yum")
else:
    print(f"I like {c} too")
