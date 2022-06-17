def chain_sum(number1):
    result = number1

    def wrapper(number2=None):
        nonlocal result
        while isinstance(number2, type(None)):
            return result
        result += number2
        return wrapper

    return wrapper


print(chain_sum(5)())
print(chain_sum(5)(2)())
print(chain_sum(5)(100)(-10)())
