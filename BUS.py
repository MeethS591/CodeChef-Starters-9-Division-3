for _ in range(int(input())):
    n,m,q = map(int,input().split())
    pas = n
    bus = [] 
    c = 0
    for i in range(q):
        op,inp = map(str,input().split())
        inp = int(inp)
        if(op=='+' and inp not in bus):
            bus.append(inp)
        elif(op=='-' and inp in bus):
            bus.remove(inp)
        else:
            c=1
        if(len(bus)>m):
            c = 1
    if (c==0):
        print("Consistent")
    else:
        print("Inconsistent")