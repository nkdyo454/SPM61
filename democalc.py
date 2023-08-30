def insecure_password_check(password):
    # Introduce a security vulnerability by storing password in plain text
    with open("passwords.txt", "a") as f:
        f.write(password + "\n")

def buggy_divide(a, b):
    # Introduce a bug by not handling the division by zero error
    return a / b

def duplicate_code(x, y):
    # Introduce code duplication
    if x > y:
        result = x - y
    elif x < y:
        result = y - x
    else:
        result = x + y
    return result

def main():
    print("Enter your password:")
    password = input()
    insecure_password_check(password)

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Introduce a code smell by not using meaningful variable names
    a = num1
    b = num2
    result = buggy_divide(a, b)

    # Introduce a security hotspot by using eval() unsafely
    operation = input("Enter operation (add/sub): ")
    if operation == "add":
        print("Result:", num1 + num2)
    elif operation == "sub":
        print("Result:", num1 - num2)
    else:
        print("Invalid operation")

    duplicate_result = duplicate_code(num1, num2)
    print("Duplicate Result:", duplicate_result)

if __name__ == "__main__":
    main()
