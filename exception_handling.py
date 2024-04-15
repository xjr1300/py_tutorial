import sys

path = "non-existent-file.txt"
print("例外処理開始")
try:
    f = open(path, "rt")
except FileNotFoundError as e:
    print(f"no such a file: {e}", file=sys.stderr)
except Exception as e:
    print(f"unexpected exception raised: {e}", file=sys.stderr)
print("例外処理終了\n")

# 例外処理なし
f = open(path, "rt")
