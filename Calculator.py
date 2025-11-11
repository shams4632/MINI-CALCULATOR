
   # Mini Calculaltor Project 

while True:


    num1 = float(input("Enter the 1st Number: "))
    Operator = input("Choose what you want: --> (+,-,*,/) -->: ")
    num2 = float(input("Enter the 2nd Number: "))



    if Operator== "+":
        add = num1+num2
        print(add) 
    elif Operator== "-":
        Subtract = num1-num2
        print(Subtract)   
    elif Operator== "*":
        Multiply = num1*num2
        print(Multiply)  
    elif Operator== "/":
        if num2==0:
            print("Your Number is Invalid")
        else:
            Divide = num1/num2
            print(Divide) 

    elif Operator == "^":     # Power
        print("Result =", num1 ** num2)

    elif Operator == "%":
        print("Result =", (num1 * num2) / 100)


    elif Operator == "%%":     # Modulus
        if num2 == 0:
            print("Error: Cannot perform modulus with zero!")
        else:
            print("Result =", num1 % num2)
    else:
        print("Invalid Choice")

    another = input("Do you want more calculation ? (Y/N)")  

    if another.lower() != "y":
        print("Calculator Closed")  
        break
        
   
  











