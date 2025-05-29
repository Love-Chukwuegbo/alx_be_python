pattern = float(input("Enter the size of the pattern:"))
n = 0
while n<pattern:
    for i in range(0,int(pattern)):
        print("*", end="") 
    print()
    n+=1
    
    