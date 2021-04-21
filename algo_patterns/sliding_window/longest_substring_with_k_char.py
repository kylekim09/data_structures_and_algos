import math
def longest_substring_with_k_distinct(str, k):
  ### can i use this dictionary to keep track of all the chars?
  ### add up all the values in here? and also 
  char_dict = {}
  max_amount = 0
  sliding_window = 0

  for index in range(len(str)):
    ## keep track of how many characters
    char = str[index]

    if char not in char_dict:
      char_dict[char] = 1
    else:
      char_dict[char] += 1

    while len(char_dict.values()) > k:
      left_char = str[sliding_window] 
      ### DECREMENT first then if it is 0 then let's pop
      char_dict[left_char] -= 1
      if char_dict[left_char] == 0:
        char_dict.pop(left_char)
      sliding_window += 1
    max_amount = max(max_amount, sum(char_dict.values()))

  return max_amount
  
def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
