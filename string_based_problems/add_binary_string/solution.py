def binarysum(A,B):
    max_len = max(len(A),len(B))
    # Zfill function add zeros at beginning of string,until it reaches specified length.
    # if the value of length specified is less than the length of string ,no filling is done.
    
    A = A.zfill(max_len)
    B = B.zfill(max_len)
    carry = 0
    res = ''
    for i in range(max_len-1,-1,-1):
        sums = int(A[i]) + int(B[i]) + carry
        carry = sums // 2
        res += str(sums % 2)
    if carry == '1':
        res += '1'
    res = res[::-1] # reversing
    return res

# testcase
A = '11'
B = '111'
ans = binarysum(A,B)
print(ans)