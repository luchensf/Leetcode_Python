def kWeakestRows(matrix, k):
    counter = {}
    for i in range(len(mat)):
        counter[i] = sum(mat[i])
    s = sorted(counter, key=counter.get)[:k]
    return s




kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]], 3)



