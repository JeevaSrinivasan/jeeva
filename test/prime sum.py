def prime(num):
    primeflag = True
    for i in range(2, num):
        if num % i == 0:
            primeflag = False
    if primeflag == True:
        return True
    else:
        return False


ans = 2
no_of_iterations = int(input())
for index in range(3, no_of_iterations):
    if prime(index):
        ans = ans + index
        if ans <= no_of_iterations and prime(ans):
         print(ans)
