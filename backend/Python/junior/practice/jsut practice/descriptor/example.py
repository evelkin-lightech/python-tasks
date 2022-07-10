class TestDescriptor:
    # начиная с python 3.6+ появился метод __set_name__
    # def __init__(self, name):
    #     self.__name = name

    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value


class TestClass:
    test_value = TestDescriptor()

    def __init__(self, x=0):
        self.test_value = x


if __name__ == '__main__':
    tc = TestClass(10)
    print(tc)
    print(tc.test_value)
    print(TestClass().test_value)
