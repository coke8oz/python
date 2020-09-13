def compute(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "invalid operator"


num1 = ""
while num1 != "x":
    num1 = input("Enter a number: ")
    if num1 != "x":
        operator = input("Enter operator: ")
        num2 = float(input("Enter a number: "))
        print(compute(float(num1), num2, operator))
