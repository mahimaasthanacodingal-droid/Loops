# Reverse a number 

num = int(input("Enter a number: "))

# N is the variable for the digit counter

n = 0

# Loop to check the positive numbers by dividing by 10

if num >= 0:  
    while num >= 1:
        num = num/10
        print (num)
        n = n + 1

# Loop to check the negative numbers by multiplying num * -1

else:
    num = num * -1
    while num >= 1:
        num = num/10
        n = n + 1


print(f"The number of digits in the number is {n} ")
    