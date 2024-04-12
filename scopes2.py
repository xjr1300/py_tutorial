import sys

x = 100


def foo():
    # 関数内でグローバル変数の参照を試行
    # しかし、変数がローカルスコープで束縛されていない（宣言されていない）ことを
    # 示す`UnboundLocalError`例外が発生するため、例外処理してプログラムが
    # クラッシュすることを避ける
    try:
        print("x in foo func:", x)
    except UnboundLocalError as e:
        print(f"UnboundLocalError: {e}", file=sys.stderr)

    # 関数内でグローバル変数と同じ名前の変数を宣言
    # この変数`x`は`foo`関数のローカル変数であり、`foo`関数の終了とともに破棄
    # される。
    # また、グローバル変数`x`は、見えなくなる
    x = 300
    print("x is a local variable in foo func:", x)


def bar():
    # `x`はグローバル変数であることを宣言
    global x

    # 関数内でグローバル変数`x`を参照
    print("x in bar func:", x)

    # 関数内でグローバル変数`x`の値を変更
    x = 400
    print("x was changed in bar func:", x)


if __name__ == "__main__":
    # 関数の外でグローバル変数`x`を参照
    print("x:", x)

    # 関数の外でグローバル変数`x`の値を変更
    x = 200
    print("x after changing:", x)

    print("\n--- go to foo func ---")
    foo()
    print("--- return from foo func ---\n")

    print("x:", x)

    print("\n--- go to bar func ---")
    bar()
    print("--- return from bar func ---\n")

    print("x:", x)

    # グローバル変数`x`が400出ない場合、プログラムがクラッシュ
    assert x == 400
