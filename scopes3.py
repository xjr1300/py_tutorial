import sys


def print_exception(e: Exception) -> None:
    print(f"{e.__class__.__name__}: {e}", file=sys.stderr)


# `if`文
if True:
    a = 1
try:
    print(a)
except UnboundLocalError as e:
    print_exception(e)

# `for`文
for _ in range(5):
    b = 2
try:
    print(b)
except Exception as e:
    print_exception(e)

# `while`文
i = 0
while i < 3:
    c = 3
    i += 1
try:
    print(c)
except Exception as e:
    print_exception(e)

# 例外処理(tryブロック)
try:
    f = 4
except:
    pass
try:
    print(f)
except Exception as e:
    print_exception(e)

# 例外処理(exceptブロック)
try:
    raise Exception
except:
    g = 5
try:
    print(g)
except Exception as e:
    print_exception(e)


# コンテキストマネージャ
with open("scopes3.py", "rt") as f:
    j = 6
try:
    print(j)
except Exception as e:
    print_exception(e)


# 関数
def func() -> None:
    h = 7


try:
    print(h)
except Exception as e:
    print_exception(e)
