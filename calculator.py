

def calculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return " error : modulus by zero"
        return num1%num2
    else:
        return "no any operation is selected"
    

def main():
    while True:
        num1=float(input("enter num1:"))
        num2=float(input("enter num2:"))
        operation=input("enter an operation(add, subtract, multiply, divide):")
        result=calculator(num1, num2, operation)
        print("Result:", result)
        
        
if __name__ == "__main__":
    main()