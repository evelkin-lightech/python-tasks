# Create a class using type(class_name, parent_class, attr_dict)

def series_init(self, *args):
    self.args = self.__clear_extra_values([*args])


def series_str(self):
    return str(self.args)


def series_check_value(cls, value):
    return type(value) in (int, float) and 0 <= value != cls.KEY


def series_clear_extra_values(cls, values):
    new_values = []
    for i in values:
        if cls.__check_value(i):
            new_values = new_values + [i]
    return new_values


Series = type('Series', (object,),
              {
                  'KEY': 1492,
                  '__check_value': staticmethod(series_check_value),
                  '__clear_extra_values': staticmethod(series_clear_extra_values),
                  '__init__': series_init,
                  '__str__': series_str,
              })
