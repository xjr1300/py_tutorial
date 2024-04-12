def call_by_int_value(n: int):
    n += 10


def call_by_float_value(f: float):
    f += 10


def call_by_str_value(s: str):
    s = s + "asdf"


if __name__ == "__main__":
    n = 1
    call_by_int_value(1)
    print(f"n = {n}")

    f = 3.14
    call_by_float_value(f)
    print(f"f = {f}")

    s = "1234"
    call_by_str_value(s)
    print(f"s = '{s}'")
