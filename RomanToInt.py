def romanToInt(s):
    m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev, num = 0, 0
    for i in s[::-1]:
        if m[i] >= prev:
            num += m[i]
        else:
            num -= m[i]
        prev = m[i]
    return num


romanToInt('LVIII')


