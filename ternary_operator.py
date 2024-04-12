import random

n = random.randint(1, 100)

# 通常の`if`文で分岐して適切な値を得る
if n % 2 == 0:
    s = "even"
else:
    s = "odd"
print(s)

# 上記`if`文の処理と同じ結果を三項演算子を使用して簡潔に得る
s = "even" if n % 2 == 0 else "odd"
print(s)
