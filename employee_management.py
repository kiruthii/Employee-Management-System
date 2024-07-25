import mysql.connector

# Establishing the connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Gkiru00..',
    database='employee_db'
)

cursor = conn.cursor()

# Function to add an employee
def add_employee(name, age, department):
    sql = "INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)"
    values = (name, age, department)
    cursor.execute(sql, values)
    conn.commit()
    print("Employee added successfully")

# Function to display all employees
def display_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Sample usage
if __name__ == "__main__":
    print("1. Add Employee")
    print("2. Display Employees")
    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        department = input("Enter department: ")
        add_employee(name, age, department)
    elif choice == 2:
        display_employees()
    else:
        print("Invalid choice")

# Close the connection
cursor.close()
conn.close()
