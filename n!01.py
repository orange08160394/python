def nH_(a):
    sum1=1
    for i in range(1,a+1):
        sum1*=i
    return sum1
a=input("enter range")
print("ans=",nH_(int(a)))