# this function takes 2 arguments and return 1 if version1 > version2 ,-1 if version < version2 ,0 if version1 == version2
def compare_version(version1,version2):
    v1 = version1.split('.')
    v2 = version2.split('.')
    length_of_version1 = len(v1)
    length_of_version2 = len(v2)
    i = 0
    j = 0
    while i < length_of_version1 and j < length_of_version2 :
        if int(v1[i]) < int(v2[j]) :
            return -1
        elif int(v1[i]) > int(v2[j]) :
            return 1
        else:
            i += 1
            j += 1
    if length_of_version1 == length_of_version2 :
        return 0
    if length_of_version1 < length_of_version2 :
        if int(v2) == 0:
            return 0
        else:
            return -1
    if length_of_version1 > length_of_version2 :
        if int(v1) == 0:
            return 0
        else:
            return 1


# test case

version1 = '2.3.01'
version2 = '2.3.11'
ans = compare_version(version1,version2)
print(ans)

    