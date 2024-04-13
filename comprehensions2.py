import time

started = time.time()
l = [n for n in range(100_000_000)]
finished = time.time()
elapsed = finished - started
print(f"{elapsed:.3f} seconds")
