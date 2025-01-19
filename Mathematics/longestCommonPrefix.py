array_word = ["aa","ab"]



def longestCommonPrefix(strs):
    def checkExist(index, charters):
        find = False
        for i in strs:
            if i[index] == charters:
                find = True
            else:
                find = False
                return find

        return find

    result = ''
    temp = ''

    small_word = min(strs, key=len)

    for index,charter in enumerate(small_word):
        temp = charter
        if checkExist(index,temp):
            result += temp
        else:
            return result

    return result







print(longestCommonPrefix(array_word))

