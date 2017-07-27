"""
Take student marks of three subjects and print the grade by
percentage.
If percentage is < 40 then fail,
less than 50 then D grade,
less than 60 then C grade,
less than 70 B grade,
less than 80, A grade,
less than 90, A+ grade,
greater than 90, A++ grade

"""
eng=float(input())
mat=float(input())
phy=float(input())
mar=(eng/100)*100
mar1=(mat/100)*100
mar2=(phy/100)*100
average=(mar+mar1+mar2)/3
print(average)
if average<40:
    print("Fail")
elif average<50:
    print("D grade")
elif average<60:
    print("C grade")
elif average<70:
    print("B grade")
elif average<80:
    print("A grade")
else:
    print("A+ grade")