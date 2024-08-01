def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multipy(a,b):
    return a*b
def divide(a,b):
    if b==0:
        raise ValueError("Cannot divide by zero")
    return a/b
def modulus(a,b):
    return a%b


if __name__ =="__main__":
    operation = {
        'add':add,
        'subtract': subtract,
        'multiply': multipy,
        'divide':divide,
        'modulus':modulus  
    }
    Entry = True
    while(Entry):
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            Entry = False
        except ValueError as e:
            print(f"Error: {e}")
    
    action = input("Enter Required Mathematical Operation (add, subtract, divide, multiply, modulus): ").strip().lower()
    func = operation.get(action)
    if func:
        try:
            result = func(a,b)
            print(f"{result:.2f}")
        except ValueError as e:
            print(f"Error {e}")
    else:
        print("Unsupported Operation.")   