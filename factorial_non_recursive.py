def factorial(n: int) -> int:
    result = 1
    for m in range(2, n + 1):
        result *= m
    return result


if __name__ == "__main__":
    print(factorial(10))
