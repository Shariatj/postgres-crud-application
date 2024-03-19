
# Student Records Management Application

### Overview

**Developer:** [Shariat Jahan Shanu] ([101285602])

This project was developed as part of the requirements for COMP3005 Assignment 3 Question 1 - Winter 2024. It's a Python3 application designed to manage student records in a PostgreSQL database.

[Link to Video Demonstration](https://youtu.be/Ina--bNfCOc)

### Setting up the PostgreSQL Database

- Launch pgAdmin 4.
- Create a new database. I am using `students`.
- Open the query tool for the database you just created and run the `studentRecords.sql` file.
- This will create a `students` table and populate it with initial data.
- To verify that the setup was successful, execute the following SQL command:

```SQL
SELECT * FROM students;
```

You should be able to see all the columns and data that were inserted from the `studentsRecord.sql` file.

### Installing Python Dependencies

Install [psycopg 3](https://pypi.org/project/psycopg/):

```bash
pip3 install --upgrade pip           # to upgrade pip
pip3 install "psycopg[binary,pool]"  # to install package and dependencies
```

### Running the Application

1. Update the database connection settings at the top of `studentsRecord.py` to match your PostgreSQL database connection details.

2. Execute the following command in the terminal:

```bash
python3 ./studentsRecord.py
```

Enjoy managing your student records!
