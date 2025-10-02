#Implement the function that meets the specifications below:
def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assumes tA and tB are the same length.
    Returns a tuple where the:
    * first element is the length of one of the tuples
    * second element is the sum of the pairwise products of tA and tB
    """
    # Your code here
    length = len(tA)
    pairwise_sum = sum(a * b for a, b in zip(tA, tB))
    return (length, pairwise_sum)

response = dot_product((1, 2, 3), (4, 5, 6))
print(response) # Should print (3, 32)