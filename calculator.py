def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
choice = int(input("choose an opertaion 1, 2, 3, 4 :\n"))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if choice == 1:
    print(a, "+", b, "=",add(a, b))
elif choice == 2:
    print(a, "-", b, "=",subtract(a, b))
elif choice == 3:
    print(a, "*", b, "=",multiply(a, b))
elif choice == 4:
    print(a, "/", b, "=",divide(a, b))
else:
    print("Invalid input")
