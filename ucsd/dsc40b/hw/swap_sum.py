def swap_sum(A, B):
    sum_a = sum(A)
    sum_b = sum(B)
    diff = (sum_b - sum_a- 10) / 2
    
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        current = B[j] - A[i]
        if current == diff:
            return (i, j)
        elif current > diff:
            i += 1
        else:
            j += 1
    
    return None