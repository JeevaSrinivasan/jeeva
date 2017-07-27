def prime(num):
    primeflag=True
    for i in range(2,num):
        if num%i==0:
            primeflag=False
    if primeflag == True:
        return True
    else:
        return False
for index in range(2, int(input())):
    print(index," = ",prime(index))
