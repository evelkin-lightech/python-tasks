# Since Python v3, all classes are explicitly
# and implicitly inherited from the base class object

class Series:
    """custom class for test"""
    KEY = 1492

    @classmethod
    def __check_value(cls, value):
        return type(value) in (int, float) and 0 <= value != cls.KEY

    def __new__(cls, *args, **kwargs):
        """before init class"""
        return super().__new__(cls)

    def __init__(self, *args):
        """init class"""
        self.args = [*args]

    def __del__(self):
        """finalize class"""
        pass

    def __repr__(self):
        """Class"""
        return str(self.args)

    def __str__(self):
        """Values"""
        return str(self.args)

    def __iter__(self):
        return self

    def length(self):
        """
        Count items in the series
        """
        count = 0
        for i in self.args:
            count += i
        return count

    def add(self, value=None):
        """
        Append new item in end of the series
        """
        if self.__check_value(value):
            self.args = self.args + [value]
        return self.args

    def update(self, *args):
        """
        Append a few item in end of the series
        """
        self.args = self.args + [*args]
        return self.args

    def remove(self, value):
        """
        Find and remove item in the series
        """
        new_series = []
        for i in self.args:
            if i != value:
                new_series = new_series + [i]
        if new_series == self.args:
            return f'{value} - not found into this series'
        else:
            return new_series

    def sum(self):
        """
        Counts the sum of the sequence
        """
        print(self.summa(self.args))

    def avg(self):
        """
        Counts the average value of the sequence
        """
        print(self.average(self.args))

    @staticmethod
    def summa(args):
        s = 0
        for i in args:
            s += i
        return s

    @staticmethod
    def average(args):
        s = 0
        for i in args:
            s += i
        return s / len(args)
