def isnumber(A): # A is the string
    A = A.strip()
    length = len(A)
    if length == 0: # if the string is empty
        return 0
    # if there is only one character and character is not mumber then return 0
    if length == 1 and not(A[0] >= '0' and A[0] <= '9'):
        return 0
    # if the first char is not +,- or digit
    if A[0] != '+' and A[0] != '-' and A[0] != '.' and not (A[0] >= '0' and A[0] <= '9'):
        return 0
    # to check if '.' or 'e' is found is given string, we use this flag to make sure that either of them appear only once.
    flag_dot_or_e = False
    for i in range(0,length):
        # if any of char does not belong to {digit,+,-}
        if A[i] != 'e' and A[i] != '.' and A[i] != '+' and A[i] != '-' and not (A[i] >= '0' and A[i] <= '9'):
            return 0
        
        if A[i] == '.':
            # check if char e has already occured before '.' . If yes ,return 0
            if flag_dot_or_e :
                return 0
            if i+1 >= length:
                return 0
            if not (A[i+1] >= '0' and A[i+1] <= 9) :
                return 0
        elif A[i] == 'e' :
            flag_dot_or_e = True
            # if there is not digit before the e
            if not(A[i-1] >= '0' and A[i-1] <= '9'):
                return 0
            # if e is last char
            if (i + 1 ) >= length :
                return 0
            # if not followed by +,-,or digit
            if A[i+1] != '+' and A[i+1] !='-' and (A[i+1] >= '0' and A[i+1] <= '9'):
                return 0
    return 1


# test case
string = '2e+3'
ans = isnumber(string) 
print(ans)

