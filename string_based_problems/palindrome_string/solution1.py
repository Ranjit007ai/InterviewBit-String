# In this problem we are given a sentence , and we have to tell if it is palindrome string or not .
# Palindrome string are those string ,which is same on even after reversing the string.

# *** we have to only consider the alphanumeric character and ignoring cases.

# This solution takes O(n) Time complexity and O(n) space complexity.

# function plaindrome return True if the string is palindrome else return False if not palindrome.

def palindrome(input_string):

    alphanumeric_string = '' # B will be the new string ,which will contain only the alphanumeric character from the input_string.

    # Traversing the input_string
    for i in input_string :
        cur_ele = str.upper(i) # converting the current element to its upperform .
        x = ord(cur_ele) # x stores the ASCII value of the current element .
        if x >= 65 and x <= 90 or x>= 49 and x <= 57 : # ASCII value of uppercase alphabet is b/w 65 to 90 and for number is b/w 49 to 57 
            alphanumeric_string += cur_ele
    
    reversed_string = alphanumeric_string[::-1]
    
    if alphanumeric_string == reversed_string :
        return True
    else:
        return False

# test case
input_string = 'A man , a plan , a canal : panama'
ispalindrome = palindrome(input_string)
print(ispalindrome)