#Take input of number of rows
n=int(input("enter the number of rows: "))

for i in range(1, n + 1):
        print(" " * (n - i), end="")  # Add leading spaces for alignment
        for j in range(1, i + 1):  # Print numbers
            print(j, end=" ")
        print()  # Move to the next line