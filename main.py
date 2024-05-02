def test(*param, **parampampam):
    print(param, parampampam)


test('Пицца',Пепперони=750, Мясная=800)


def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n*factorial_recursive(n-1)


print('Факториал числа 8: ', factorial_recursive(8))
