def group_by(xs, key_function):
    output = {}
    for item in xs:
        if key_function(item) not in output:
            output[key_function(item)] = []
        output[key_function(item)].append(item)
    
    return output