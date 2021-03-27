def reverse_string(string):
    words  = string.split()
    reverse = []
    for word in words :
        reverse.insert(0,word)
    
    return ' '.join(reverse)

# test case
input_string  = 'hello world'
ans = reverse_string(input_string)
print(ans)