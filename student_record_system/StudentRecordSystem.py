# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 19:15:44 2024

@author: Hiba Irfan
"""

import json
import os



 

student_record = {
    "name": None,
    "rollno": 0,
    "subject": {"Maths": 0, "Science": 0, "English": 0, "Urdu":0},
    "totalmarks": 0
}


students = []

 

# json_object = json.dumps(student_record, indent=4)
 
# with open('sample.json', 'r') as openfile:
 
#     # Reading from json file
#     json_object = json.load(openfile)
 
# print(json_object)
# print(type(json_object))

# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)

class Student_record_system:
    def __init__(self,students):
     
       self.students = students
       
       
        
    def add_std(self):
        print("ADD student")
        student_record = {
            "name": None,
            "rollno": 0,
            "subject": {"Maths": 0, "Science": 0, "English": 0, "Urdu":0},
            "totalmarks": 0
        }
        student_record["name"] = input("Enter student name:: ")
        student_record["rollno"] = int(input("Enter student roll no:: "))
        for sub,marks in student_record["subject"].items():
            student_record["subject"][sub] = float(input(f"Enter {sub} number:: "))
            student_record["totalmarks"] += student_record["subject"][sub]
            
        self.students.append(student_record)
        print("Record Added successfully...\n")
        
        
        
    def view_std(self):
        print("View student")
        
        if len(self.students) == 0:
            print("no records is added")
        else:
            for i,val in enumerate(self.students, start=1):
                print(f"Student {i} :")
                print(json.dumps(val, indent=4))
        print("\n")
        
        
        
    def search_std(self):
        print("Search student")
        if len(self.students) == 0:
            print("no records is added")
        else:
            rollno = int(input("Enter roll number to find student record:: "))
            for i,val in enumerate(self.students, start=1):
                if val["rollno"] == rollno:
                    return val
            return "There is no record of it.\n"
                    
        
        
    def delete_std(self):
        print("Delete student")
        if len(self.students) == 0:
            print("no records is added")
        else:
            rollno = int(input("Enter roll number to delete student record:: "))
            for i,val in enumerate(self.students, start=1):
                if val["rollno"] == rollno:
                    self.students.remove(val)
                    print("record deleted successfully...\n.")

            
        
    def update_std(self):
         print("Update student")
         
         if len(self.students) == 0:
             print("No records added yet.\n")
             return 
         
         rollno = int(input("Enter roll number to update student record:: "))
         
         
         for i, val in enumerate(self.students):
             if val["rollno"] == rollno:
                 user = int(input("1. Update name.\n"
                                  "2. Update marks.\n"))
                 
                 if user not in range(1, 3):
                     print("\nInvalid operation. Please select a number from 1 to 2.")
                     return self.update_std()  
                 
                 if user == 1:
                     val["name"] = input("Enter new name: ")
                     print(f"Updated name for roll no {rollno}.")
 
                 elif user == 2:
                     
                     val["totalmarks"] = 0
                     for sub, marks in val["subject"].items():
                         val["subject"][sub] = float(input(f"Enter updated marks for {sub}: "))
                         val["totalmarks"] += val["subject"][sub]  
 
                     print(f"Updated marks for roll no {rollno}\n.")
                 
             
                 print(json.dumps(val, indent=4))
                 print("\n")
                 return  
         
         print("Roll number not found.\n")
         
        
    def save_std(self):
        print("Save student")
        
        if os.path.exists("Student_Records.json"):
            with open("Student_Records.json", "r") as infile:
                try:
                    existing_records = json.load(infile)
                except json.JSONDecodeError:
                   
                    existing_records = []
        else:
            existing_records = []

       
        existing_records.extend(self.students)

      
        with open("Student_Records.json", "w") as outfile:
            json.dump(existing_records, outfile, indent=4)

        print("Records saved successfully!\n")

    def load_std(self):
        print("Load student")
        

        
        if os.path.exists('Student_Records.json'):
           
            with open('Student_Records.json', 'r') as openfile:
                self.students = json.load(openfile)
        else:
            
            self.students = []
            
        print("Records loaded.....\n")
    

    def exit_program(self):
        self.save_std()
        
        
    
    
print("Welcome to Student Record Management System\n\n")
obj = Student_record_system(students)

def menu_bar():
    operations = (
       "1. Add student record\n"
             "2. View student record\n"
             "3. Search student record\n"
             "4. Delete student record\n"
             "5. Update student record\n"
             "6. Save student record\n"
             "7. Load student record\n"
             "8. Exit program\n"
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

while(True):
    user_input = menu_bar()

    if(user_input == 1):
        obj.add_std()
        
    elif(user_input == 2):
        obj.view_std()
        
    elif(user_input == 3):
       std = obj.search_std()
       print(json.dumps(std, indent=4))

    elif(user_input == 4):
        obj.delete_std()
        
    elif(user_input == 5):
        obj.update_std()
        
    elif(user_input == 6):
        obj.save_std()
        
    elif(user_input == 7):
        obj.load_std()
    elif(user_input == 8):
        ex = input("Do you want to save the record...")
        if ex == "yes":
            
            obj.exit_program()
        break
        
    else:
        print("The option you select is not in list please try different option\n")
        menu_bar()
        
        
print("LOG OUT")


