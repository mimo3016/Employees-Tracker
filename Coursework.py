#Greeting to welcome the user
print("Hello and welcome to Mohamed Coursework project..Est 2023..")

#Asking the user to insert the number of the company's employees
employees_number = int(input("Enter the number of the employees: "))

#While loop to make sure that the user insert an appropriate number 
while employees_number <= 0:
    print("This can not be a number of employees!")
    employees_number = int(input("Enter the number of the employees: "))
    
    

#Lists to store the details of the employees that will be given by the user
employees_name = []
employees_id = []
employees_prop_sold = []
employees_comission = []

#Variables that will be used for future calculation
comission = 1
total_commission = 0
number_prop_sold = 0


#For loop to ask the user every employee details depending on the number of employees
for i in range(1, employees_number+1):
    #Asking the user about the employee name
    name = input("Enter the  employee name: ")
    #Adding the employee name to the list that contains every employee name
    employees_name.append(name)
    
    #Asking the user about the employee ID
    id = int(input("Enter ID number: "))
    #Adding the employee ID to the list that contains every employee ID
    employees_id.append(id)
    
    #Asking the user about the employee number of properties that he sold
    prop_sold = int(input("Enter number of properties sold: "))
    #Adding the employee ID to the list that contains every employee number of properties sold
    employees_prop_sold.append(prop_sold)

    
    #If condition to do calculations of commissions
    if prop_sold > 0 :
        #calculate each employee commission
        comission = prop_sold * 500
        #Adding each employee commission to the list that contains every employee commissions
        employees_comission.append(comission)
        #Calculating the total commission that the company will pay by adding each employee commission that the user insert every time
        total_commission += comission
        #Calculating the total number of properties sold by the company by adding each employee number of properties sold that the user insert every time
        number_prop_sold += prop_sold
        

     
#Function to sort the employees depending on the number of properties that they sold using bubble sort    
def sort(employees_prop_sold, employees_name, employees_id):
    # Bubble sort implementation
    for o in range(len(employees_prop_sold) - 1):
        for j in range(len(employees_prop_sold) - o - 1):
            # Swap if the current element is smaller than the next one (descending order)
            if employees_prop_sold[j] < employees_prop_sold[j + 1]:
                # Swap properties sold
                employees_prop_sold[j], employees_prop_sold[j + 1] = employees_prop_sold[j + 1], employees_prop_sold[j]
                # Swap corresponding names
                employees_name[j], employees_name[j + 1] = employees_name[j + 1], employees_name[j]
                # Swap corresponding IDs
                employees_id[j], employees_id[j + 1] = employees_id[j + 1], employees_id[j]

# Example usage
sort(employees_prop_sold, employees_name, employees_id)
#The list that contains number of properties sold is in a descending order which means that the first name in the names list is the employee that sold the most properties
best_employee = employees_name[0]


#Calculating the bonus that would be given to the employee of the week
largest_number = None

#For loop to go through number of properties sold list and find the highest value
for number in employees_prop_sold:
    #If condition to find the biggest value
    if largest_number is None or largest_number < number:
        largest_number = number

#Give the highest value which is the highest number of properties sold by an employee 15% bonus because he's the employee of the week
bonus = largest_number * 0.15


#Display the menu so the user can choose what he wants to see
while True:
    # Display the menu so the user can choose what he wants to see
    print("\nEnter 1 to see the employee list in descending order:\n"
          "Enter 2 to see the sales commission for each employee:\n"
          "Enter 3 to see the total sales commission for the week:\n"
          "Enter 4 to see the total number of properties sold in the week:\n"
          "Enter 5 to see the employee of the week award:\n"
          "Enter 6 to see the bonus amount received by the employee of the week:\n"
          "Enter Y to see the menu again:\n"
          "Enter N to exit:")
    # Asking the user to insert a number or a letter that displays the information that he wants
    choice = input("Enter the number or the letter of what you want to see: ")

    # Connecting every number or letter that the user can insert with the information that is supposed to appear to him
    if choice == "1":
        print("Employees name in a descending order based on the number of properties sold: " , employees_name)
    elif choice == "2":
     print("Sales commission for each employee:")
     for i in range(len(employees_comission)):
        print(f"{employees_name[i]}: {employees_comission[i]} £.", end=" ")
     print() 
    elif choice == "3":
        print(total_commission, "£")
    elif choice == "4":
        print(f"Total number of properties sold in a week: {number_prop_sold} property.")
    elif choice == "5":
        print(f"The employee of the week is: {best_employee}")
    elif choice == "6":
        print(f"The bonus amount received by the employee of the week: {bonus}£")
   
    elif choice.lower() == "y":
        print("")
    elif choice.lower() == "n":
        print("Thank you for your visit, see you soon!")
        break
    else:
        print("Invalid choice. Please try again with another letter or number")