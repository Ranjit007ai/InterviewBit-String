def power_of_2(A):
    if int(A) <= 0:
        return False
    while int(A) != 2 :
        if int(A) % 2 != 0 :
            return False
        A = int(A) // 2
    return True

# test case
number = '8'
ans = power_of_2(number)
print(ans)