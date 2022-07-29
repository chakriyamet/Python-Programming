# student information      still error code
name = input("What is your name? ")
print("Hello " + name + "How can I help you? ")

print("Select an operation to show: ")
print("1. CLASS")
print("2. SCORE")
print("3. TOP RANGE")

operation = input()

if operation == "1":
    name = input("Enter your surname: ")
    text = input()
    textLen = len(text)
    sum = 0
    for i in range(textLen):
        if text[i]>='a' and text[i]<='z':
           sum = sum+1
print("\nYour Name has = " + str(sum))
    if name >= 10:
        print("You're in class A ")
    else:
        print("You're in class B ")
        
elif operation =="2":
    score = input("Enter your score: ")
    if score <= 50:
        print("You're passed ")
    else:
        print("You're failed ")
    
elif operation =="3":
    score = input("Enter your score: ")
    if score <= 100 or score >= 80:
        print("You're in the top one")
    elif score <= 80 or score >= 60:
        print("You're in the top two ")
    elif score <= 60 or score >= 50:
        print("You're in the top three ")
    elif score <= 50 or score >= 10:
        print("You're not in the top ")
    else:
        print("Enter your score again ")
    




