def knn_distance(a, q, k):
    d = [(abs(x - q), x) for x in a]

    def partition(l, r, p):
        pivot = d[p][0]
        d[p], d[r] = d[r], d[p]
        s = l
        for i in range(l, r):
            if d[i][0] < pivot:
                d[s], d[i] = d[i], d[s]
                s += 1
        d[r], d[s] = d[s], d[r]
        return s

    def quickselect(l, r, target):
        if l >= r:
            return
        p = partition(l, r, (l + r) // 2)
        if target < p:
            quickselect(l, p - 1, target)
        elif target > p:
            quickselect(p + 1, r, target)

    quickselect(0, len(d) - 1, k - 1)
    farthest_pair = d[0]
    for pair in d[:k]:
        if pair[0] > farthest_pair[0]:
            farthest_pair = pair
            
    distance, point = farthest_pair
    
    return distance, point
