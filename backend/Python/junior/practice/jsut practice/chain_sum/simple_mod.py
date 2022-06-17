def chain_sum(number1):
    def wrapper(number2=None):
        if number2 is None:
            return wrapper.result
        wrapper.result += number2
        return wrapper

    wrapper.result = number1
    return wrapper


print(chain_sum(5)())
print(chain_sum(5)(2)())
print(chain_sum(5)(100)(-10)())
