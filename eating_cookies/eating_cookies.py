'''
Input: an integer
Returns: an integer
'''


#  Why do the original tests for this function pass in a list as a second argument???
#  def eating_cookies(n):
#      if n == 0:
#          return 1
#      elif n == 1:
#          return 1
#      elif n == 2:
#          return 2
#      elif n == 3:
#          return 4
#      else:
#          return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


memo = {
    0: 1,
    1: 1,
    2: 2,
    3: 4
}


def eating_cookies(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
        return memo[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
