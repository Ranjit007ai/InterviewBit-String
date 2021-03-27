# if there is only one word or last line than left justification else center justification
# here iam using ',' in place of ' ' .
def left_justify(i,j,max_width,cur_length,words):
    # variable definition
    diff = max_width - cur_length
    res = ''
    if j - i == 1 :     # only one word
        res += words[i] + ','*diff
    else: # more than one word and on last line
        for k in range(i,j-1):
            # incase of last word
            res += words[k] + ','
            diff -= 1
        res += words[j-1] + ','*diff
    return res

def center_justify(i,j,max_width,cur_length,words):
    # variable definition
    diff = max_width - cur_length
    space_place = j - i - 1
    space_required = diff // space_place
    extra_space = diff % space_place
    res = ''
    for k in range(i,j-1):
        if extra_space != 0 :
            res += words[k] + ','*space_required + ','
            extra_space -= 1
        else:
            res += words[k]  + ','*space_required
    res += words[j-1]
    return res
 


def justify_string(words,max_width): # words is an list of words and ,max_width is the max len of line should have
    n = len(words)
    i = 0
    find_output = []

    while i < n :
        j = i + 1
        cur_length = len(words[i])
        print(cur_length)
        while j < n and (cur_length + len(words[j]) + ( j - i ) <= max_width ) :
            cur_length += len(words[j])
            j += 1
        # check if it is lef justify or center justify
        no_of_word = j - i 
        if (no_of_word) == 1 or j >= n : # left_justify
            ans = left_justify(i,j,max_width,cur_length,words)
            find_output.append(ans)
        else:        # center justification
            ans = center_justify(i,j,max_width,cur_length,words)
            find_output.append(ans)
        i += 1
    return find_output

# test case
words = ['This','is','an','example','of','text','justification']
l = 16
ans = justify_string(words,l)
print(ans)