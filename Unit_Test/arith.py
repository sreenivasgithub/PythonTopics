
def addition(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    return 'please enter integers'
    #raise TypeError


def division(a, b):
    if (isinstance(a, str) or isinstance(b, str)):
        return 'error'
    elif b != 0:
        return a / b
    else:
        return 'ZeroDivisionError'
