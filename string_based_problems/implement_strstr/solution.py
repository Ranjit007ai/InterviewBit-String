def strstr(A,B):
    m = len(A) # bigger string length
    n = len(B) # smaller string length
    if m == 0 or n == 0:
        return -1
    if m < n :
        return -1
    for i in range(0,m-n+1) :
        count = 0 
        for j in range(0,n) :
            if A[i+j] != B[j]:
                break
            else:
                count += 1
        if count == n :
            return i
    return -1


