# your code goes here
from typing import Callable

def multiplier_of(n:int) -> Callable:
     def multiplier(x:int)-> int:
          print(x * n)
     return multiplier

multiplywith5 = multiplier_of(5)
multiplywith5(9)
