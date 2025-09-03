def mode(numbers): 
    num_map = {}
    for i in numbers: 
        if i in num_map: 
            num_map[i] += 1
        else: 
            num_map[i] = 1
    
    max_key = max(num_map, key=num_map.get)
    
    return max_key
        