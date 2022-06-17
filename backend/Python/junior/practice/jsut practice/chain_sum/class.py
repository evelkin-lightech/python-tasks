class ChainSum:
    def __init__(self, number):
        self._number = number

    def __call__(self, value=0):
        return ChainSum(self._number + value)

    def __str__(self):
        return str(self._number)


print(ChainSum(5))
print(ChainSum(5)(2))
print(ChainSum(5)(100)(-10))
