### This is a great way of calculating and dynamically adding/removing things from a source of data

### good for things that are in one particular order and you need to gather the calculation in a specific window

### array of elements and we want to find the computation of a sub array

### k is the length of the array. 
def find_averages_of_subarrays(K, arr):
  results = []
  left_window = 0
  array_sum = 0.0

  for window_end in range (len(arr)):
    array_sum += arr[window_end]

    if window_end >= K - 1:
      results.append(array_sum / K)
      array_sum -= arr[left_window]
      left_window += 1

  return results


def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()