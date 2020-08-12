import math
'''
Input: a List of integers as well as an integer `k` representing the size of
the sliding window
Returns: a List of integers
'''


# Is this not O(n) time? O(k*(n-k))
# Took 80 seconds to run the large test file. So...no
#  def sliding_window_max(nums, k):
#      maxes = []
#      for i in range(len(nums)-k+1):
#          maxes.append(max(nums[i:i+k]))
#      return maxes

# So this one took 3.6 seconds. So big improvement, but still not there...
# This has to be O(n). Hard to tell though, maybe depends on distribution
# of values and how many rescans have to happen? Worst case it's just the
# previous algorithm
def sliding_window_max(nums, k):
    maxes = []
    current_max = {
        'index': -1,
        'value': None
    }

    for i in range(len(nums)-k+1):
        right_index = i+k-1

        # The max has just fallen out
        if current_max['index'] < i:
            # rescan the whole window
            current_max['value'] = -math.inf
            for j, num in enumerate(nums[i:i+k]):
                if num > current_max['value']:
                    current_max['index'] = i+j
                    current_max['value'] = num
                else:
                    pass
        # new value > current max
        elif nums[right_index] > current_max['value']:
            current_max['index'] = right_index
            current_max['value'] = nums[right_index]
        else:
            pass
        maxes.append(current_max['value'])

    return maxes


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
