def pair(lst,t):
    import itertools
    for i in itertools.combinations(lst,2):
            if sum(i)==t:
                lst.pop()
    return lst
            
