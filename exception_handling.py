import sys

print("例外処理開始")
try:
    f = open("non-existent-file.txt")
except FileNotFoundError as e:
    print(f"no such a file: {e}", file=sys.stderr)
except Exception as e:
    print(f"unexpected exception raised: {e}", file=sys.stderr)

print("例外処理終了\n")

# 例外処理なし
f = open("non-existent-file.txt")
