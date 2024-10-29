# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:24:08 2024

@author: Hiba
"""
def Addition(num_1,num_2):
    add = num_1 + num_2
    return add

def Subtraction(num_1,num_2):
    sub = num_1 - num_2
    return sub

def Multiplication(num_1,num_2):
    mul = num_1 * num_2
    return mul

def Division(num_1,num_2):
    if num_2 == 0:
        return "Error! Division by zero."
    return num_1 / num_2

def Exponent(num_1,num_2):
    exp = num_1**num_2
    return exp

def SquareRoot(num_1):
    root = num_1**0.5
    return root

def Cube(num_1):
    cube = num_1**3
    return cube
def Square(num_1):
    square = num_1**2
    return square



def menu_bar():
    operations = (
       "1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n"
       "5. Exponent\n6. Square Root\n7. Cube\n8. Square\n"
   )
    print(operations)
    try:
        selected_operation = int(input("Select which operation you want to perform: "))
        if selected_operation not in range(1, 9):
            print("\nInvalid operation. Please select a number from 1 to 8.")
            return menu_bar()
        return selected_operation
    except ValueError:
        print("Invalid input. Please enter a number.")
        return menu_bar()

def print_result(result):
    if isinstance(result, str):  
        print(result)
    else:
        formatted_value = round(result, 2)
        if formatted_value.is_integer():
            print(int(formatted_value))
        else:
            print(formatted_value)

    
welcome_message = "Hello, Welcome to Hiba calculator."
print(welcome_message)

while True:
    selected_operation = menu_bar()
    try:
        if selected_operation in [6, 7, 8]:
            num_1 = float(input("Input number: "))
        else:
            num_1 = float(input("Input First number: "))
            num_2 = float(input("Input Second number: "))
        valid_input = True 
    except ValueError:
        print("\nInvalid input! Please enter a valid numeric value.")
        valid_input = False 
        
    if valid_input:
        if selected_operation == 1:
            
            print(f"{num_1} + {num_2} = ",end=' ')
            result = Addition(num_1,num_2)
            print_result(result)
            
            
        elif selected_operation == 2:
            print(f"{num_1} - {num_2} = ",end=' ')
            
            result = Subtraction(num_1,num_2)
            print_result(result)
            
        elif selected_operation == 3:
            print(f"{num_1} * {num_2} = ",end=' ')
            
            result = Multiplication(num_1,num_2)
            print_result(result)
            
        elif selected_operation == 4:
            print(f"{num_1} / {num_2} = ",end=' ')
            
            result = Division(num_1,num_2)
            print_result(result)
        elif selected_operation == 5:
            print(f"{num_1} exponent {num_2} = ",end=' ')
            
            result = Exponent(num_1,num_2)
            print_result(result)
        elif selected_operation == 6:
            print(f"Sqaure Root of {num_1} = ",end=' ')
             
            result = SquareRoot(num_1)
            print_result(result)
        elif selected_operation == 7:
            print(f"Cube of {num_1} = ",end=' ')
             
            result = Cube(num_1)
            print_result(result)
        elif selected_operation == 8:
            print(f"Sqaure of {num_1}= ",end=' ')
            result = Square(num_1)
            print_result(result)
        else:
            print("The option you select is not in the list please try again...")
    else:
        print("Try again...\n")
        
    
      
    
    exit_operation = input("Type 'yes' if you want to continue, or anything else to exit: ").lower()
    if exit_operation == 'yes':
        continue
    else:
        break

print("Thank You for using Hiba's Calculator")
