def roman_to_integer(string):
    # creating a dictionary roman:int
    romans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    length = len(string)
    sums = 0
    for i in range(length - 1, -1, -1):
        if i == length - 1:
            sums += romans[string[i]]
        elif romans[string[i]] >= romans[string[i+1]] :
            sums += romans[string[i]]
        else:
            sums -= romans[string[i]]
    return sums

# test case
string = 'IXI'
ans = roman_to_integer(string)
print(ans)