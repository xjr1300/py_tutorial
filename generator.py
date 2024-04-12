from typing import Generator


# `max - 1`までの値を順に返すジェネレーター関数
def number_generator(max: int) -> Generator[int, None, None]:
    for i in range(max):
        yield i


for value in number_generator(5):
    print(value)

print()

iter = number_generator(5)
print(iter.__next__())  # 0
print(iter.__next__())  # 1
print(iter.__next__())  # 2
print(iter.__next__())  # 3
print(iter.__next__())  # 4
print(iter.__next__())  # StopIteration例外発生
