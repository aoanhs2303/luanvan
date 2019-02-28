def CombineAndSort(LOC1, LOC2):
    c = list(set(LOC1 + LOC2))
    return sorted(c)