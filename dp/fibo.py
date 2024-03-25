def fibo(n: int) -> int:
    if (n <= 2):
        result = 1
    else:
        result = fibo(n - 1) + fibo(n - 2)
    return result

if __name__ == "__main__":
    print(fibo(7))
    print(fibo(50))

