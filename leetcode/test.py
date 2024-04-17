def test(test_str: str, i: int = 1) -> str:
    if (i < 3):
        return test(test_str, i + 1)
    else:
        return "here"

print(test("hi"))
