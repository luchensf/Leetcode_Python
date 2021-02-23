def brokenCalc(X, Y):
    res = 0
    while X < Y:
        if Y % 2 == 1:
            Y += 1
            res += 1
        Y = Y / 2
        res += 1
    if Y < X:
        res += (X - Y)
    return int(res)


brokenCalc(1024, 1)



