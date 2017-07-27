for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                for e in range(0,10):
                    if 4*(10000*a+1000*b+100*c+10*d+e)==(10000*e+1000*d+100*c+10*b+a):
                        print(a,b,c,d,e)