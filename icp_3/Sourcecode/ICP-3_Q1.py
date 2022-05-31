class Employee:
    
    # Initialize the class attribute variable
    num_employees = 0

    def __init__(self, id_num, name, department, salary, balance):
        self.id = id_num
        self.name = name
        self.department = department
        self.salary = float(salary)
        self.balance = balance
        self.isEmployed = True

    def pay(self):
        # Add the salary to the balance to pay the employee
        self.balance += self.salary

    def fire(self):
        # Set the salary to zero and state the employee is no longer employed
        self.salary = 0
        self.isEmployed = False

    def is_employed(self):
        return self.isEmployed


class FullTime(Employee):
    def __init__(self, id_num, name, department, salary, balance):
        # Call the parent constructor
        Employee.__init__(self, id_num, name, department, salary, balance)
        self.type = "F"

    def give_raise(self, percent=10):
        # Give raise by multiplying the current salary with 0.1 or given percentage and adding it to the
        # current salary value
        self.salary += self.salary * (percent * 0.01)


class PartTime(Employee):
    def __init__(self, id_num, name, department, salary, balance):
        # Call the parent constructor
        Employee.__init__(self, id_num, name, department, salary, balance)
        self.type = "P"

    def give_raise(self, percent=5):
        # Give raise by multiplying the current salary with 0.05 or given percentage and adding it to the
        # current salary value
        self.salary += self.salary * (percent * 0.01)


def average_salary(employees):
    full_tot = 0
    num_full = 0
    part_tot = 0
    num_part = 0

    # Loop through all the employees and add the salaries to the variable
    for emp in employees:
        if emp.type == "F":
            full_tot += emp.salary
            num_full += 1
        elif emp.type == "P":
            part_tot += emp.salary
            num_part += 1

    # Calculate the averages for the full and part time employees
    full_avg = full_tot / num_full
    part_avg = part_tot / num_part

    return full_avg, part_avg


if __name__ == '__main__':
    # Read the input file and create an output file
    infile = open("input.txt", "r")
    outfile = open("output.txt", "w")
    line = infile.readline()

    # Create a list to hold all the class objects
    employees = []

    # Read all the lines in the input file
    while line != "":
        words = line.split()
        # Identify the keyword used
        if words[0] == "NEW":
            # Identify what type of employee is being added and increase employee count
            if words[len(words) - 1] == "F":
                employees.append(FullTime(words[1], words[2] + " " + words[3], words[4], words[5], 0))
                employees[0].__class__.num_employees += 1
            elif words[len(words) - 1] == "P":
                employees.append(PartTime(words[1], words[2] + " " + words[3], words[4], words[5], 0))
                employees[0].__class__.num_employees += 1

        elif words[0] == "RAISE":
            # Look through list of employees and find employee to give raise to
            for employee in employees:
                if employee.id == words[1]:
                    if len(line) == 3:
                        # If specific value for raise is given, send that value to the function
                        employee.give_raise(int(words[2]))
                    else:
                        employee.give_raise()
        elif words[0] == "PAY":
            # Loop through all employees and pay them once
            for employee in employees:
                employee.pay()
        elif words[0] == "FIRE":
            # Find employee to fire
            for employee in employees:
                if employee.id == words[1]:
                    employee.fire()

        # Read the next line of the file
        line = infile.readline()

    # Write the employee information to the output file
    outfile.write("Emp. Name, ID ###, Department:\n")
    # Loop through all the employee information
    for employee in employees:
        outfile.write(employee.name + ", " + employee.id + ", " + employee.department + "\n")
        if employee.is_employed():
            outfile.write("Current salary: $" + str(round(employee.salary, 2)) + "\n")
        else:
            outfile.write("Not employed with the company.\n")

        outfile.write("Pay earned to date: $" + str(round(employee.balance, 2)) + "\n")
        if employee.type == "F":
            outfile.write("Full-Time Employee\n")
        else:
            outfile.write("Part-Time Employee\n")
        outfile.write("\n")

    # State total number of employees and average salaries for both types of employees.
    full, part = average_salary(employees)
    outfile.write("Total number of employees: " + str(employees[0].__class__.num_employees) + "\n")
    outfile.write("Average salary paid to all Full-Time employees: $" + str(round(full, 2)) + "\n")
    outfile.write("Average salary paid to all Part-Time employees: $" + str(round(part, 2)))
    
    
    
