def rotate_list_right(data,amount):
    """

    Rotate the 'data' to the right by the

    'amount'.   For example, if the data is

    [1, 2, 3, 4, 5, 6, 7, 8, 9] and an amount

    is 5 then the list returned should be

    [5, 6, 7, 8, 9, 1, 2, 3, 4].  The value

    of amount will be in the range of 1 and

    len(data).

    """
    #using negative indexing we can easily divide the two portions of the data
    #that is left half and right half and combine them seperately
    return data[-amount:]+data[:-amount]
    #the statement below also works which is based on the constant length rearrangement
    #we use modulus here so as to keep the length of the list constant

d=[1,2,3,4,5,6,7,8,9]
print(rotate_list_right(d,1))
print(rotate_list_right(d,5))
print(rotate_list_right(d,9))