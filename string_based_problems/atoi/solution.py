def atoi(A):
    # removing the whitespace from both side
    A = str.strip(A)
    negative = False
    out = 0
    if A[0] == '-' :
        negative = True
    elif A[0] == '+' :
        negative = False
    elif A[0] < '0' or A[0] >'9':
        return 0
    else:
        out = ord(A[0]) - ord('0')
    for i in range(1,len(A)):
        if A[i] >= '0' and A[i] <= '9' :
            out = out * 10 + (ord(A[i]) - ord('0'))
            if not negative and out >= 2147483634 :
                return 2147463647
            if negative and out >= 2147483647 :
                return -2147483648
        else:
            break
    if not negative :
        return out
    return -out

# test case
A = '9270 4'
ans = atoi(A)
print(ans)