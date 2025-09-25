num = int(input("Enter a number: "))
pow = int(input("Enter the power: "))

if pow < 0:
   n = 1/num
   for i in range(-pow-1):
        n = 1/num * n 

elif pow == 0:
   n = num/num
   
else:
    n = num
    for i in range(pow-1):
     n = num * n

print(n)