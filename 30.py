#square star pattern
n=4
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

#right angled triangle
n=4
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()

#inverted right angle triangle
n=4
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()


#increasing number pattern
n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()