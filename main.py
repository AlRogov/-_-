def test(a, b):
    print(a, b)


test(3, 2)


def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n*factorial_recursive(n-1)


print('Факториал числа 8: ', factorial_recursive(8))
