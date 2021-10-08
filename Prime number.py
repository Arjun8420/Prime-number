#Program to verify if a given number is prime or not

print("Program to verify if a given number is prime")
n=int(input("Enter the number = "))

flag=True

for div in range(2,n):
    if n % div == 0:
        flag = False
        break
    
print("Given number is a Prime Number" if flag == True else "Given number is Not a Prime Number")



