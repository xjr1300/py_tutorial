def call_by_reference(l: list):
    l.append("added")


if __name__ == "__main__":
    l = ["foo", "bar", "baz"]
    call_by_reference(l)
    print(l)
