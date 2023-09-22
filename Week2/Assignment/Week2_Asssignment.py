print("1. Basic")
print("2. BMI")
calculatorChoice = input("which calculator would you like to use? (type the number)")


while True:
  if calculatorChoice == "1":
    print("Which operation would you like to use?")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    def add(x, y):
      return x + y

    def subtract(x, y):
      return x - y

    def multiply(x, y):
      return x * y

    def divide(x, y):
      return x / y

    choice = input("Enter choice(1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print(add(num1, num2))
        break
    elif choice == "2":
        print(subtract(num1, num2))
        break
    elif choice == "3":
        print(multiply(num1, num2))
        break
    elif choice == "4":
        print(divide(num1, num2))
        break
  elif calculatorChoice == "2":
    weight = float(input("Please input your weight. (in kg)"))
    height = float(input("Please input your height. (in m)"))

    print(weight / (height**2.0))
    break
  else:
    print("please choose a number 1 or 2")
    break
