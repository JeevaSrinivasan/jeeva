num=int(input())
for n in range(1,num):
    if (num%2!=0):
        if (num%1==0 and num%n==0):
            print("Nth prime number is",n)