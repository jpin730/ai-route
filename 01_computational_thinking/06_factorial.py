def factorial(n):
    if n <= 0:
        print('Input is not an positive integer.')
        return 0
    elif n == 1:
        return 1
    return n * factorial(n - 1)


print(
    factorial(
        int(input('Input an positive integer: '))
    )
)
