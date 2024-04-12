import sys
import time

# 項とフィボナッチ数を格納する辞書
d: dict[int, int] = {}


def fibonacci(n):
    # dict型はミュータブルであるため、global宣言は不要
    # 辞書に項が格納されていれば、その値を返す
    if n in d:
        return d[n]

    if n == 0:
        return 0
    elif n == 1:
        return 1
    value = fibonacci(n - 2) + fibonacci(n - 1)
    d[n] = value
    return value


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("expected one argument", file=sys.stderr)
        sys.exit(1)
    try:
        n = int(args[1])
    except ValueError:
        print("expected an integer number", file=sys.stderr)
        sys.exit(1)

    # フィボナッチ数を求める
    started = time.time()
    value = fibonacci(n)
    finished = time.time()
    elapsed = finished - started
    print(f"fibonacci value: {value} ({elapsed:.2f} seconds)")
