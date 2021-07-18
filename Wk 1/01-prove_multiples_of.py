def multiples_of(number,length):   
    """

    This function will produce a list of size 'length' starting

    with 'number' followed by multiples of 'number'.  For

    example, multiples_of(7, 5) will result in:

    [7, 14, 21, 28, 35].  Assume that length is a positive

    integer greater than 0.  The implementation must be

    done using a list comprehension.

    """
    mul_list=[number*i for i in range(1,length+1)]
    #we multiply the given number with numbers ranging from 1 to given length
    return mul_list

print(multiples_of(7, 5))    # [7, 14, 21, 28, 35]
print(multiples_of(1.5, 10)) # [1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0, 13.5, 15.0]
print(multiples_of(-2, 10))  # [-2, -4, -6, -8, -10, -12, -14, -16, -18, -20]

