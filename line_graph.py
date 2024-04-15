# ビルトインされていないパッケージを利用するためにはインポートする必要があります。
#
# `numpy`パッケージを`np`としてインポート
import numpy as np

# `matplotlib`パッケージから`pyplot`モジュールを`plt`としてインポート
import matplotlib.pyplot as plt

# 乱数の生成を固定するシードを設定
np.random.seed(0)

# 0から19までの整数を生成
x = [i for i in range(20)]
# 0から100までの整数を20個生成
y = [np.random.randint(0, 100) for _ in range(20)]

# 描画エリアを作成
_, ax = plt.subplots()
# 折れ線グラフを描画
ax.plot(x, y)

# 折れ線グラフを表示
plt.show()
