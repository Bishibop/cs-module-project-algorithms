'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    existence_hash = {}
    for n in arr:
        if n in existence_hash:
            existence_hash.pop(n)
        else:
            existence_hash[n] = 1
    return list(existence_hash.keys())[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")


# Doing this in O(1)?
# Use the array object as the memo?
# Delete elements from the array as I put them into the dictionary?
