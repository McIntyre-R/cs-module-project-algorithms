'''
Input: an integer
Returns: an integer
'''
def permutation(arr): 
    if len(arr) == 0: 
        return [] 
    elif len(arr) == 1: 
        return [arr] 
    permutations = [] 
    for i in range(len(arr)): 
       cur = arr[i] 
       remaining = arr[:i] + arr[i+1:] 
       for j in permutation(remaining): 
           permutations.append([cur] + j) 
    return permutations 

def combos(nums, target, partial=[], par=0):
  if par == target:
    yield partial
  elif par > target:
    return
  for i in range(len(nums)):
    n = nums[i]
    remaining = nums[i+1:]
    yield from combos(remaining, target, partial + [n], par + n)

def eating_cookies(n):
  if n == 0:
    return 1
  num1 = [1]*n
  num2 = [2]*(n//2)
  num3 = [3]*(n//3)
  a = list(combos(num1+num2+num3, n))
  b_set = set(map(tuple,a))  
  b = list(map(list,b_set))
  perm = []
  for e in range(0,len(b)):
    perm += permutation(b[e])
  perm_set = set(map(tuple,perm))  
  perm_b = list(map(list,perm_set))
  return len(perm_b)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
