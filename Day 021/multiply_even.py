def multiply_even_numbers(lst):
    """
    multiply_even_numbers([2,3,4,5,6]) # 48"""
    total = 1
    for val in lst:
        if val % 2 == 0:
            total = total * val
    return total


print(multiply_even_numbers([2, 3, 4, 5, 6]))
