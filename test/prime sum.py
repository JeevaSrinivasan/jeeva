def prime(num):
    primeflag=True
    for i in range(2,num):
        if num%i==0:
            primeflag=False
            print(i)
    if primeflag== True:
        return True
    else:
        return True
prime(20)