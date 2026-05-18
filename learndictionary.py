#list

fruits_names= ['Apple', 'Orange', 'Grapes', 'Mango', 'Litchi'],
people_names = ['Londeka', 'Jane', 'Joshua', 'Jessica', 'Luke'],
prices = [2, 4, 6, 8, 10],
quantity = [10, 30, 40, 50, 90]

data = {
   "fruits_names": ['Apple', 'Orange', 'Grapes', 'Mango', 'Litchi'],
   "people_names": ['Londeka', 'Jane', 'Joshua', 'Jessica', 'Luke'],
   "prices": [2, 4, 6, 8, 10],
   "quantity": [10, 30, 40, 50, 90]
}


#dictionary
person_dict = {
    "name" : "Londeka",
    "age" : 30,
    "address" : "45 Joseph Nduli street"
    
}

print(f"Person Dictionary: {person_dict}")

#adding item in the dictionary
person_dict["gender"] = "Female" 

#updating name
person_dict["name"] = "Zintle"

print(f"Person Dictionary: {person_dict}")

#delete a key-value pair from the dictionary
del person_dict["address"]

#accessing values from the dictionary
print(f"Personal Information Dictionary: {person_dict}")


print("###################################################################")
print("###################################################################")
print("###################################################################")
print("###################################################################")
print("###################################################################")
print("###################################################################")

#creating a new dictionary

gijima_students = [{"name": "Ndumiso Ngcobo",
                   "Age": 22,
                   "course": "Artificial Intelligence",
                   "duration": "7 months",
                   },
                   
                   {"name" : "Londeka Nduli",
                    "Age" : "23",
                    "course" : "Artificial Intelligence",
                    "duration" : "7 months",
                       
                   },
                   {"name" : "Megan-lee Williamson",
                    "Age" : "23",
                    "course" : "Data Science",
                    "duration" : "7 months",
                       
                   },
                   {"name" : "Bekezela Msweli",
                    "Age" : "31",
                    "course" : "Artificial Inteligence",
                    "duration" : "7 months",
                   },
                   {"name" : "Dembe Nemathithi",
                    "Age" : "26",
                    "course" : "Data Science",
                    "duration" : "7 months",
                       
                   },
                    {"name" : "Mjabulelwa Kumalo",
                    "Age" : "24",
                    "course" : "Data Science",
                    "duration" : "7 months",
                   },
                    
                    {"name" : "Gudani Lukhwareni",
                    "Age" : "23",
                    "course" : "Artificial Inteligence",
                    "duration" : "7 months",
                   },
                    
                     {"name" : "Kilibane Yanelisa",
                    "Age" : "30",
                    "course" : "Data Science",
                    "duration" : "7 months",
                     }
                    
                ]

# display one students
print(f"Gijima Students: {gijima_students[3]}")

print("Print using For Loop: ")


try:
    
    # display all students
    for student in gijima_students:
        if student['name'] is not "Ndumiso Ngcobo":
         print(f"{student}")
    print("###########################################################")
    
    for i in range(len(gijima_students)):
        print(gijima_students[i])
        
    print("###########################################################")
    print("######################## While Loop ###########################")
    
    # while lopp:
    x = 0
    
    while x < len(gijima_students):
        
        if gijima_students[x]['name'] == "Megan-lee Williamson":
            pass
        else:
             print(gijima_students[x])
        x = x+1
            
        
        
        
        
    print("###########################################################")
    
         
except Exception as ex:
    print(f"Error: {ex}")
    
