import random
import math
import uuid

while True:
    u = uuid.uuid4()
    uf = f"{hex(u.time_low)}-{hex(u.time_mid)}-{hex(u.time_hi_version)}-{hex(u.clock_seq_hi_variant)}-{hex(u.clock_seq_low)}-{hex(u.node)}"
    print(uf)

