def int_to_roman(A):
    number = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    sign = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    res = ''
    i = 0
    while A :
        div = A // number[i]
        A = A % number[i]
        while div :
            res += sign[i]
            div -= 1
        i += 1
    return res

# test case
A = 12
ans = int_to_roman(A)
print(ans)