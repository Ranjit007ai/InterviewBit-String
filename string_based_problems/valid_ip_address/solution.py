def isvalid(ip): 
    # splitting the ip by '.'
    ip = ip.split('.')
    # check corner cases
    for i in ip :
        if len(i) > 3 and int(i) < 0 and int(i) > 255 :
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if len(i) > 1 and int(i) != 0 and i[0] == '0':
            return False
    return True
def convert(A): # A is the string
    s2 = len(A)
    if s2 > 12 :
        return []
    snew = A
    l = []
    # generating different combinations
    for i in range(0,s2 - 2):
        for j in range(i + 1,s2-1) :
            for k in range(j + 1,s2) :
                
                snew = snew[:k] + '.' + snew[k:]
                snew = snew[:j] + '.' + snew[j:]
                snew = snew[:i] + '.' + snew[i:]

                if isvalid(snew):
                    l.append(snew)
                snew = A
    return l 

# test case
input_string = '25525511135'
ans = convert(input_string)
print(ans)