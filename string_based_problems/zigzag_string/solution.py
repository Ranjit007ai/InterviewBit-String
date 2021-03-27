def zigzag(A,B): # A is the string and B is the no of rows
    if B == 1 :          # if there is only one row ,then return the original string
        return A
    l = len(A)
    s = ['' for i in range(B)]
    k = 0
    for i in range(l):
        s[k] += A[i]
        if k == B - 1 :
            down = False
        elif k == 0:
            down = True
        if down :
            k += 1
        else:
            k -= 1
    ans = ''
    for i in range(0,B):
        ans += s[i]
    return ans

# test case
A = 'paypalishiring'
B = 3
ans = zigzag(A,B)
print(ans)