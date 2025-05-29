pattern = int(input("Enter the size of the pattern: "))
n = 0
while n < pattern :
    for i in range(0,pattern):
        print("*", end="") 
    print()
    n += 1
    
    