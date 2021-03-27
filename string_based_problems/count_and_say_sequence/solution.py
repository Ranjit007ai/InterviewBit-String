# count and say sequence look like 1, 11, 21 , 1211,...

def sequence(current):
    length = len(current)
    count = 1
    out = ''
    for i in range(len(current)) :
        if i == length - 1 :
           out += str(count) + str(current[i]) 
        elif current[i] == current[i+1]:
            count += 1
        else:
            out += str(count) + str(current[i])
            count = 1
    return out


def count_and_say_sequence(N) :
    if N == 1 :
        return '1'
    if N == 2 :
        return '11'
    prev = '11'
    for n in range(3,N+1):
        cur = sequence(prev)
        prev = cur
    return prev

# test case
N = 4
ans = count_and_say_sequence(N)
print(ans)