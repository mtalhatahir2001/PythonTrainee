# your code goes here
def multiplier_of(n:int) -> object:
     def multiplier(x:int)-> int:
          print(x * n)
     return multiplier

multiplywith5 = multiplier_of(5)
multiplywith5(9)