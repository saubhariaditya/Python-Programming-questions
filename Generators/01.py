def jay():
    print('hai')
    yield 1
    print('hello')
    yield 2
    print('bye')
    yield 3
print(list(jay()))


def jay():
    print('hai')
    return 1
    print('hello')
    return 2
    print('bye')
    return 3
print(jay())
