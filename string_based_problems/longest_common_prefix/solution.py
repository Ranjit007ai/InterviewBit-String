# Given a array of strings ,we need to find the longest common prefix in them.

# this function  take the input array as a parameter and return the longest common prefix . 
def longest_common_prefix(input_array):
    min_length = 999999999999999 # min_length to store the length of the string with minimum size among all other strings
    min_index = -1  # min_index to store the index of the minimum length string
    n = len(input_array) # n store the length of the input array
    prefix = '' 
    # traversing  the input_array 
    for i in range(0,n):
        
        length = len(input_array[i]) # length store the length the ith string in the array
        
        if length < min_length :
            min_length = length
            min_index = i 
        
        min_word = input_array[min_index] # min_word is the string with minimum length

        for i in range(0,min_length): # traversing  the min_word
            cur_alphabet = min_word[i]
            count = 0
            for j in range(0,n): # traversing the array
                if input_array[j][i] == cur_alphabet : 
                    count += 1
                else:
                    break
            if count == n :
                prefix += cur_alphabet
            else:
                break
        return prefix

# test case
input_array = ['abcdef','abcdf']
answer = longest_common_prefix(input_array)
print(answer)

        