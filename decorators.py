from typing import Callable


# デコレーター
def print_deco(func) -> Callable[[int, int], int]:
    # print_deco関数が返す関数
    def wrapper(n: int, m: int) -> int:
        # 追加の前処理
        print("--- start ---")

        result = func(n, m)

        # 追加の後処理
        print("--- end ---")
        return result

    # 関数を返す
    return wrapper


# デコレーターで修飾
@print_deco
def foo(n: int, m: int) -> int:
    value = n + m
    print(f"foo will return {value}")
    return value


# 単純な`foo`関数の呼び出しが、デコレーターにより加工された関数呼び出しになっている
value = foo(10, 12)
assert value == 22
