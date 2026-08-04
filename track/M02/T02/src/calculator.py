def calculator(n1, n2, opeartor):
    if operator == "+":
        return n1 + n2
    elif operator == "-":
        return n1 - n2
    elif operator == "*":
        return n1 * n2
    elif operator == "/":
        return n1 / n2
    else:
        return "Invalid Input"

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
operator = input("Enter the operator: ")
result = calculator(n1, n2, operator)
print(f"The result of {n1} {operator} {n2} is : {result}")