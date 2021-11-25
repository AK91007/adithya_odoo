r=4 #Variable for rows
k=4 #Variable for spaces
#Loop for printing the pattern
for i in range(0,r):
    for j in range (0,k):
        print(end=" ")
    k-=1
    for j in range(0,i+1):
        print("* ",end="")
    print("")