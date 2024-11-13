def main():
    try:
        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    except ValueError:
        print("Invalid input")


if __name__ == "__main__":
    main()
