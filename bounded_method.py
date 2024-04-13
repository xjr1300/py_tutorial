import time
from typing import List

started = time.time()
l: List[int] = []
m = l.append
for n in range(100_000_000):
    m(n)
finished = time.time()
elapsed = finished - started
print(f"{elapsed:.3f} seconds")
