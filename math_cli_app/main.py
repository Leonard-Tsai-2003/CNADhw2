from addition import add_numbers
from factorial import calculate_factorial
from odd_even import check_odd_even

def main():
    while True:
        print("\nMath Operations CLI")
        print("1. Addition")
        print("2. Factorial")
        print("3. Odd/Even Check")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = add_numbers(a, b)
                print(f"The sum is: {result}")
            except ValueError:
                print("Please enter valid numbers")
                
        elif choice == "2":
            try:
                n = int(input("Enter a non-negative integer: "))
                result = calculate_factorial(n)
                print(f"The factorial of {n} is: {result}")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == "3":
            try:
                n = int(input("Enter an integer: "))
                result = check_odd_even(n)
                print(f"The number {n} is {result}")
            except ValueError:
                print("Please enter a valid integer")
                
        elif choice == "4":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 