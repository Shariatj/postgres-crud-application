import psycopg2 as psycopg

# Database connection settings
DB_NAME = "students"
USER = "postgres"
HOST = "localhost"
PASSWORD = "student1"

# Function to establish a connection to the database
def create_conn():
    try:
        conn = psycopg.connect(
            f"dbname={DB_NAME} user={USER} host={HOST} password={PASSWORD}"
        )
        return conn
    except Exception as e:
        print(f"Unable to connect to the database: {e}")
        exit(1)

# Function to retrieve and display all records from the students table
def get_all_students():
    conn = create_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
        for row in rows:
            print(row)

# Function to insert a new student record into the students table
def add_student(first_name, last_name, email, enrollment_date):
    conn = create_conn()
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
            (first_name, last_name, email, enrollment_date),
        )
        conn.commit()

# Function to update the email address for a student with the specified student_id
def update_student_email(student_id, new_email):
    conn = create_conn()
    with conn.cursor() as cur:
        cur.execute(
            "UPDATE students SET email = %s WHERE student_id = %s",
            (new_email, student_id),
        )
        conn.commit()

# Function to delete the record of the student with the specified student_id
def delete_student(student_id):
    conn = create_conn()
    with conn.cursor() as cur:
        cur.execute(
            "DELETE FROM students WHERE student_id = %s",
            (student_id,),
        )
        conn.commit()

# Main function to interact with the user
def main():
    while True:
        print("\n1. Get all students")
        print("2. Add a new student")
        print("3. Update a student's email")
        print("4. Delete a student")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            get_all_students()
        elif choice == "2":
            first_name = input("Enter the student's first name: ")
            last_name = input("Enter the student's last name: ")
            email = input("Enter the student's email: ")
            enrollment_date = input("Enter the student's enrollment date (YYYY-MM-DD): ")
            add_student(first_name, last_name, email, enrollment_date)
        elif choice == "3":
            student_id = input("Enter the student's id: ")
            new_email = input("Enter the student's new email: ")
            update_student_email(student_id, new_email)
        elif choice == "4":
            student_id = input("Enter the student's id: ")
            delete_student(student_id)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
