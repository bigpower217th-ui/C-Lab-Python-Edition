def calculator():
    print("--- Simple Python calculator ---")
    print("Operations: +, -, *, /")
    
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator: ")
        num2 = float(input("Enter second number: "))
        
        # Mantık hatasını çözmek için sonucu bulduğumuz an 'return' ile dışarı fırlatıyoruz
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Cannot divide by zero"
        else:
            return "Error: Invalid operator"
            
    except ValueError:
        return "Error: Please enter valid numbers"

# Fonksiyonu çağır ve dönen sonucu yazdır
print(calculator())
