# 0から9を格納したリストを作成して要素を2乗した値を持つリストを作成
l1 = []
for n in range(10):
    l1.append(n**2)
print(l1)

# 上記をリスト内包表記で実装
l2 = [n**2 for n in range(10)]
print(l2)
assert l1 == l2

# 上記リストから奇数のみを抽出
l3 = [n for n in l1 if n % 2 == 1]
print(l3)

# 0から9をキーに、それらを2乗した値を持つ辞書を作成
d1 = {n: n**2 for n in range(10)}
print(d1)
