def FileWiki(fl,url):
    chr1=""
    chr2=""
    c_fl=0
    pl_chr1=0
    pl_chr2=0
    for i in fl:
        t=fl.count(i):
            if t>c_fl:
                chr1=i
                c_fl=fl.count(i)
            else:
                chr2=i
                c_fl=fl.count(i)
    for x in url:
        if chr1==url:
            pl_chr1=pl_chr1+1
        if chr2==url:
            pl_chr2=pl_chr2+1
    return pl_chr1,pl_chr2
        
