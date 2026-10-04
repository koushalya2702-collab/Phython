# #fibonacci series
# n=int(input("Enter number of terms:"))
# a=0
# b=1
# for i in range(n):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c

#check prime number
n=int(input("Enter a number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime number")
else:
    print("not prime number")