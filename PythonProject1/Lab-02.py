# Dictionary
myemployees:{}

def add_employees():
    myemployee_name = (input("Enter employe's name: "))
    basic_pay = int(input("Enter basic pay: "))
    allowance = int(input("Enter allowance: "))
    deductions = int(input("Enter deductions: "))
    taxes = int(input("Enter taxes: "))
    gross_pay = basic_pay + allowance
    net_pay = gross_pay - deductions - taxes

    myemployees.update = ({
        myemployee_name: {
        "Employee Name": myemployee_name,
        "Basic Pay": basic_pay,
        "Allowance": allowance,
        "Deductions": deductions,
        "Taxes": taxes,
        "Gross Pay" : gross_pay,
        "Net Pay": net_pay
        }
    })


    print("Employee added successfully")

def delete_employees():
    myemployee_name = input("Enter employe's name to delete:")
    if myemployee_name in myemployees:
        del myemployees[myemployee_name]
        print("Employee deleted successfully")

    else:
        print("Employee does not exist")


def modify_employees():
    myemployee_name = input("Enter employe's name to modify:")
    if myemployee_name in myemployees:
        myemployee_name = int(input("Enter employe's name:"))
        basic_pay = int(input("Enter basic pay:"))
        allowance = int(input("Enter allowance:"))
        deductions = int(input("Enter deductions:"))
        taxes = int(input("Enter taxes:"))
        gross_pay = basic_pay - allowance
        net_pay = gross_pay - deductions - taxes

        myemployees[myemployee_name] = {
            "Employee Name": myemployee_name,
            "Basic Pay": basic_pay,
            "Allowance": allowance,
            "Deductions": deductions,
            "Taxes": taxes,
            "Gross_pay": gross_pay,
            "Net Pay": net_pay
        }
        print("Employee modified successfully")
    else:
        print("Employee does not exist")


def display_employees():
    if (myemployees) == 0:
        print("No Employee found")
    else:
        for myemployee_name in myemployees:
            print("Employee Name: ", myemployee_name)
            print("Basic Pay: ", myemployees[myemployee_name]["Basic Pay"])
            print("Allowance: ", myemployees[myemployee_name]["Allowance"])
            print("Deductions: ", myemployees[myemployee_name]["Deductions"])
            print("Taxes: ", myemployees[myemployee_name]["Taxes"])
            print("Gross Pay:",myemployees[myemployee_name]["Gross Name"])
            print("Net Pay: ", myemployees[myemployee_name]["Net Pay"])


while True:
    print("1. Add employees")
    print("2. Delete employees")
    print("3. Modify employees")
    print("4. Display employees")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_employees()
    elif choice == 2:
        delete_employees()
    elif choice == 3:
        modify_employees()
    elif choice == 4:
        display_employees()
    elif choice == 5:
        print("exit")
        break

    else:
        print("Invalid choice")
