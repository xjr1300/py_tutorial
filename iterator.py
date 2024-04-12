from typing import Self


# `max - 1`までの数値を順番に返すイテレーター
class NumberIterator:
    def __init__(self, max: int) -> None:
        self.max = max
        self.current = 0

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> int:
        if self.max <= self.current:
            raise StopIteration()
        returning = self.current
        self.current += 1
        return returning


iter = NumberIterator(5)
for value in iter:
    print(value)

print()

iter = NumberIterator(5)
print(iter.__next__())  # 0
print(iter.__next__())  # 1
print(iter.__next__())  # 2
print(iter.__next__())  # 3
print(iter.__next__())  # 4
print(iter.__next__())  # StopIteration例外発生
