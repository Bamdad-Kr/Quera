def comb(n, k) :
    nk = n-k
    for i in range(1, n) :
        n *= i
    for i in range(1, k) :
        k *= i
    for i in range(1, nk) :
        nk *= i
    try :
        return int(n/(k*nk))
    except ZeroDivisionError :
       return 1
    
