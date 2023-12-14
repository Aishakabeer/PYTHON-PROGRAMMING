n=int(input("Enter the second number "))
v=97
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(v),end=" ")
    v=v+1
    print(" ")

