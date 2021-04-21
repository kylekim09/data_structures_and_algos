###given an array of positive numbers find the max sum of any contigious sub array of size K
import math
def max_sub_array_of_size_k(k, arr):
  sum_iterator = 0
  max_sum = 0
  window_start = 0

  for index, number in enumerate(arr):
    sum_iterator += number
    
    if index >= k-1:
      max_sum = max(max_sum, sum_iterator)
      sum_iterator -= arr[window_start]
      window_start += 1
    
  
  return max_sum

def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()