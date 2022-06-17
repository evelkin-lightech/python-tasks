class ChainSum(int):
    def __call__(self, addition=0):
        return ChainSum(self + addition)


print(1 + ChainSum(5))
print(1 + ChainSum(5)(2))
print(1 + ChainSum(5)(100)(-10))
