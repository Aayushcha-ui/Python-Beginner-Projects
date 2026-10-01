employees = {}


def add_employee():
    employees_id = int(input("Enter your Employee ID: "))
    name = input("Enter your name: ")
    salary = int(input("Enter your salary: "))

    employees[employees_id] = {
        "name": name,
        "salary": salary
    }

    print("Employee added successfully!")


def main():
    while True:
        print("\n EMPLOYEE PAYROLL SYSTEM")
        print("1. Add Employee")
        print("2. Calculate Salary")
        print("3. Generate Payslip")
        print("4. Search Employee")
        print("5. Save Payroll Data")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_employee()

        elif choice == 2:
            print("Calculate Salary")

        elif choice == 3:
            print("Generate Payslip")

        elif choice == 4:
            print("Search Employee")

        elif choice == 5:
            print("Save Payroll Data")

        elif choice == 6:
            print("Done!")
            break

        else:
            print("Something went wrong!")
def calculate_salary():
    employees_id = int(input("Enter your Employee ID :"))
    
    if employees_id not in employees :
        print("Your id is not exist")
        return
    salary = employees[employees_id]["salary"]
    print("Employee Name:", employees[employees_id]["name"])
    print("Salary:", salary)
def Payslip ():
    employees_id = int(input("Enter your Employee ID :"))
    
    if employees_id not in employees :
        print("Your id is not exist")
        return
    salary = employees[employees_id]["salary"]
    name = employees[employees_id]["name"] 
    print("\n===== PAYSLIP =====")
    print("Employee ID:", employees_id)
    print("Employee Name:", name)
    print("Salary:", salary)
def search_employee():
    employees_id = int(input("Enter your Employee ID: "))

    if employees_id in employees:
        print("Employee ID:", employees_id)
        print("Employee name:", employees[employees_id]["name"])
        print("Employee salary:", employees[employees_id]["salary"])
    else:
        print("Employee not found")
        
def save_payroll():
    with open("payroll.txt", "w") as file:
        for employee_id in employees:
            name = employees[employee_id]["name"]
            salary = employees[employee_id]["salary"]

            file.write("Employee ID: " + str(employee_id) + "\n")
            file.write("Employee Name: " + name + "\n")
            file.write("Salary: " + str(salary) + "\n")

    print("Payroll data saved successfully!")
    
     
    

main()