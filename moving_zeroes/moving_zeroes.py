from collections import deque
'''
Input: a List of integers
Returns: a List of integers
'''


#  def moving_zeroes(arr):
#      # I used a Deque here because you need to swap the 0s in order.
#      # There might be more zeros than numbers and then you might
#      # have a "leftover" zero that hasn't been swapped to the end.
#      # If you do this with a List, then you need to do an O(n) insertion
#      # or deletion into or from the beginning of the list.
#      zero_indices = deque()
#
#      for i, n in enumerate(arr):
#          if n == 0:
#              # Save the index
#              zero_indices.append(i)
#          elif zero_indices:
#              # Swap with the first 0
#              zero_index = zero_indices.popleft()
#              arr[zero_index] = arr[i]
#              arr[i] = 0
#              zero_indices.append(i)
#          else:
#              # No previous 0s, so do nothing
#              pass
#
#      return arr


# Single-pass, O(1) space solution
def moving_zeroes(arr):

    frontier_index = 1

    for i, n in enumerate(arr):
        if n == 0:
            while frontier_index < len(arr):
                if arr[frontier_index] == 0:
                    frontier_index += 1
                else:
                    arr[i] = arr[frontier_index]
                    arr[frontier_index] = 0
                    break
        else:
            frontier_index += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
