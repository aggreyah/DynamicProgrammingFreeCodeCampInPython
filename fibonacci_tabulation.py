def fib(n):
    fib_list = []
    for i in range(n + 1):
        fib_list.append(0)
    fib_list[1] = 1
    for i in range(n + 1):
        fib_list[i + 1] += fib_list[i]
        try:
            fib_list[i + 2] += fib_list[i]
        except IndexError as e:
            break

    return fib_list[n]


if __name__ == "__main__":
    print(fib(6))
    print(fib(300))
