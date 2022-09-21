def tril(lst):
    miden=0
    ena=0
    for i in range(len(lst)):
        if lst[i]==0:
           miden=miden+1
        elif lst[i]==1:
           ena=ena+1
    return miden,ena
