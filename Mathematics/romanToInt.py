
value = "MCMXCIV"



def romanToInt(s):

    mapvalue = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }
    result = 0
    prev_value = 0

    for i in s[::-1]:
        value = mapvalue[i]

        if prev_value > value:
            result = result - value
        else:
            result += value

        prev_value = value

    return result

print(romanToInt(value))

        #
        # print(mapvalue[i])
# print(1000 + 100 + 1000 + 10 + 100 + 1 + 5)

# big > small

# small < big