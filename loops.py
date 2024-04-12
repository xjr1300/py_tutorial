import time

# for文
print("--- for statements ---")
# 指定した回数だけ繰り返し
for i in range(5):
    print(i)
print()
time.sleep(3)

# リストの要素を順に処理
for i in [1, 2, 3, 4, 5]:
    print(i)
print()
time.sleep(3)

# 文字列を1文字ずつ順に処理
for c in "hello":
    print(c)
print()
time.sleep(3)

# 辞書に格納されたキーと値のペアを処理（順番は保証されない）
for key, value in {"a": 1, "b": 2, "c": 3}.items():
    print(key, value)
print()
time.sleep(3)

# while文
print("--- while statements ---")
i = 0
while i < 5:
    print(i)
    i += 1
print()
time.sleep(3)

# 無限ループ
while True:
    print("infinite loop")
    time.sleep(1)
print()
time.sleep(3)
