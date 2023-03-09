#Following is the exercise, function provided:
from functools import partial
def func(u: int, v: int , w: int, x: int) -> int:
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function
partial_function = partial(func, 3, 4, 6)
print(partial_function(24))
