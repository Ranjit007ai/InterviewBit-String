# # In this problem we are given a sentence , and we have to tell if it is palindrome string or not .
# Palindrome string are those string ,which is same on even after reversing the string.

# *** we have to only consider the alphanumeric character and ignoring cases.

# We are going to use the Two pointer concept to solve this problem.

# function plaindrome return True if the string is palindrome else return False if not palindrome.
def palindrome(input_string):
    lower = 0               # lower pointer points to first index of the string
    higher = len(input_string) - 1 # higher pointer points to the last index of the string
    while lower < higher :
        # converting the current element of the string to upper case
        upper_case_of_lower_element = str.upper(input_string[lower])
        upper_case_of_higher_element = str.upper(input_string[higher])
        
        # finding the ascii value of both  the lower element and higher element

        ascii_value_of_lower_element = ord(upper_case_of_lower_element)
        ascii_value_of_higher_element = ord(upper_case_of_higher_element)

        if ascii_value_of_lower_element >= 65 and ascii_value_of_lower_element <= 90 or ascii_value_of_lower_element >=49 and ascii_value_of_lower_element <= 57 :
            if ascii_value_of_higher_element >= 65 and ascii_value_of_higher_element <= 90 or ascii_value_of_higher_element >=49 and ascii_value_of_higher_element <= 57 :
                if upper_case_of_lower_element == upper_case_of_higher_element :
                    lower += 1
                    higher -= 1
                else:
                    return False
            else:
                higher -= 1
        else:
            lower += 1
    return True


# test case
input_string = 'A man , a plan , a canal : panama'
ispalindrome = palindrome(input_string)
print(ispalindrome)




