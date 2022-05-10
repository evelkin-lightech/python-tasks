# def func(a, x=[]):
#     x.append(a)
#     print(x, id(x))
#
#
# y = [1, 2, 3]
# print(y, id(y))
#
# func(4)
# func(3)
# func(5, y)

def func(a, x=None):
    if x is None:
        x = []
    x.append(a)
    print(x, id(x))


y = [1, 2, 3]
print(y, id(y))

func(4)
func(3)
func(5, y)
