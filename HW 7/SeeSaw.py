def seesaw(sequence):
    odd = []
    even = []
    for i in sequence:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    count = min(len(even), len(odd))
    i = 0
    while i < count:
        yield even[i]
        yield odd[i]
        i += 1
    if i >= len(even):
        j = i
        while j < len(odd):
            yield odd[j]
            j += 1
    else:
        j = i
        while j < len(even):
            yield even[j]
            j += 1
            
