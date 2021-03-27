def multiply(A,B):
    l1 = len(A)
    l2 = len(B)
    
    # creating a res of size ( l1 + l2 )
    res = [0] * ( l1 + l2 )
    
    # converting to int list
    A = list(map(int,A))
    B = list(map(int,B))

    # reverse list
    A.reverse()
    B.reverse()

    for j in range(0,l2):
        for i in range(0,l1):
            res[ i + j ] = res[ i + j ] + ( A[i] * B[j] )
            res[ i + j + 1 ] = res[ i + j + 1 ]  + ( res[ i + j ] // 10 )
            res[ i + j ] = res[ i + j ] % 10
    
    # for elemenating all leading zeros 
    i = len(res) - 1
    while res[i] == 0 and i > 0:
        i -= 1
    return ''.join(map(str,res[:i+1][::-1]))

# test case
A = '15'
B = '2'
ans = multiply(A,B)
print(ans)