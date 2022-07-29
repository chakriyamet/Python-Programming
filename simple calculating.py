#Build a simple calculator
print("Select an operation to perform: ")
print("1. ADD")
print("2. SUBSTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
    #for add
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The sum is" + str(int(num1) + int(num2)) )
elif operation =="2":
    #for substract
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The sum is" + str(int(num1) - int(num2)) )
elif operation =="3":
    #for multiply
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The sum is" + str(int(num1) * int(num2)) )
elif operation =="4":
    #for devide
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The sum is" + str(int(num1) / int(num2)) )
else:
    print("Invailed entry! ")
    



    
    