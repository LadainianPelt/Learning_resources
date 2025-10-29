#Implement the function that meets the specifications below.
def recur_power(base, exp):
 """
 base: int or float.
 exp: int >= 0
 Returns base to the power of exp using recursion.
    Hint: Base case is when exp = 0. Otherwise, in the recursive
 case you return base * base^(exp-1).
 """
 # Your code here
 def recur_power(base, exp):
    if exp <=0:
        return 1
    return base * recur_power(base, exp - 1)