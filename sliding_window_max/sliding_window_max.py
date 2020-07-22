'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
  big = []
  big_num = 'start'
  arr_slice = nums[k-k:k]
  for e in arr_slice:
    if big_num == 'start':
        big_num = e
    elif e > big_num:
        big_num = e
  big.append(big_num)
  if k < len(nums):
    big += sliding_window_max(nums[1:],k)
  return big



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
