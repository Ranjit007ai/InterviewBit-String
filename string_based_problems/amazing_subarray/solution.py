def amazing_subarray(Arr):
    l = len(Arr)
    vowel = ['A','E','I','O','U','a','e','i','o','u']
    count = 0
    for i in range(0,l):
        if Arr[i] in vowel :
            count += (l - i)
    return count % 10003

# testcase 
arr = 'ABEC'
ans = amazing_subarray(arr)
print(ans)