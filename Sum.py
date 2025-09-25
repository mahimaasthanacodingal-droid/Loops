# Range upto which you want sum (Sum of natural numbers)
num =int(input("Enter, how many number sum's you want: "))

sum = 0 #Avoid garbage value

for i in range (1, num+1):
    sum = sum+i
    print("\n", sum)
