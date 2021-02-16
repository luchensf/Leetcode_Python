def kWeakestRows(matrix, k):
    counter = {}
    for i in range(len(matrix)):
        counter[i] = sum(matrix[i])
    s = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    print(s, s.keys()[k])
    return s.keys()[k]




kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]], 3)



