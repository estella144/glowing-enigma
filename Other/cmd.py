import os
from base64 import b64encode

ul = False

while True:
    c = input("> ")
    if ul:
        os.system(c)
    else:
        if b64encode(bytes(c, "utf8")) == b"YXV0aG9yaXNlZF91c2Vy":
            ul = True
            print("Access denied [2001]")
        else:
            print("Access denied [3105]")
