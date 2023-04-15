def nomore(sequence):
    for i in range(len(sequence)):
        for j in sequence:
            if j <= sequence[i]:
                yield j
