# interpreter.py

def main():
    # Prompt the user for an arithmetic expression
    expression = input("Expression: ").strip()

    try:
        # Split the input into parts
        x_str, operator, z_str = expression.split()

        # Convert x and z to integers
        x = int(x_str)
        z = int(z_str)

        # Perform the appropriate operation
        if operator == '+':
            result = x + z
        elif operator == '-':
            result = x - z
        elif operator == '*':
            result = x * z
        elif operator == '/':
            result = x / z
        else:
            raise ValueError("Unknown operator")

        # Output the result formatted to one decimal place
        print(f"{result:.1f}")
    
    except ValueError:
        print("Invalid input. Please enter a valid arithmetic expression in the format 'x y z'.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Ensure the main function runs if the script is executed
if __name__ == "__main__":
    main()
