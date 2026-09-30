def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b


def main():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = add(num1, num2)
        if result.is_integer():
            print(f"The sum of {num1} and {num2} is: {int(result)}")
        else:
            print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Error: Invalid input. Please enter valid numerical values.")


if __name__ == "__main__":
    main()
