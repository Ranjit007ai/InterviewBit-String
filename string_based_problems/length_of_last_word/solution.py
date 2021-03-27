# this function takes the string as the parameter and return the length of the last word in the string
# if there is no space i.e only single word then return 0  ,else return the count of char in last word.
def length_of_last_word(string): 
    string = str.strip(string) # we are triming i.e removing all the whitespace from both the end of the string
    length = len(string)
    count_of_char = 0
    count_of_space = 0
    for i in range(length - 1, -1 , -1) : # traversing the string in the reverse order
        if string[i] != ' ' : #if the current element of the string is not space 
            count_of_char += 1
        else:
            count_of_space += 1
            break
    if count_of_space == 0:
        return 0
    else:
        return count_of_char

# test case
input_string = 'hello world'
ans = length_of_last_word(input_string)
print(ans)