def calc(a: list) -> tuple:
    x=max(a)
    s=0
    n=0
    for i in a:
        s=s+i
        n=n+1
    y=s/n
    a=sorted(a)
    if len(a)%2==0:
        m=(a[(n//2)-1]+a[(n//2)])/2
    else:
        m=a[((n+1)//2)-1]
    T=(y,m,x)
    return T
