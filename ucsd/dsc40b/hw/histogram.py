def histogram(points, bins):
    output = []
    bin_index = 0
    bin_count = 0 
    i = 0
    total_len = len(points)
        
    while i < total_len: 
        low, high = bins[bin_index]
        point = points[i]
        if low <= point < high:
            bin_count += 1
            i += 1 
        else: 
            bin_width = high - low
            a = bin_count / (total_len * bin_width)
            output.append(a)
            
            bin_count = 0
            bin_index += 1
            
    while bin_index < len(bins):
        low, high = bins[bin_index]
        bin_width = high - low
        a = bin_count / (total_len * bin_width)
        output.append(a)
        bin_count = 0
        bin_index += 1

    return output  