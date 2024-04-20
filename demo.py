### Q1. What is a database? Differentiate between SQL and NoSQL databases.
'''
- Database: A database is an organized collection of structured information, or data, typically stored electronically in a computer system. It is designed to allow the retrieval, insertion, and manipulation of data.

- SQL (Relational) Databases:
  - SQL databases are relational databases that use Structured Query Language (SQL) for defining and manipulating data.
  - They have a predefined schema where data is stored in tables with rows and columns.
  - Examples: MySQL, PostgreSQL, SQLite, SQL Server, etc.

- NoSQL (Non-Relational) Databases:
  - NoSQL databases are non-relational, meaning they do not use a tabular schema like SQL databases.
  - They are more flexible in terms of data storage, allowing for unstructured and semi-structured data.
  - Examples: MongoDB, Cassandra, Redis, Couchbase, etc.
'''
### Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.
'''
- DDL (Data Definition Language):
  - DDL is a set of SQL commands used to define the database structure or schema.
  - Examples of DDL commands:
    - CREATE: Used to create a new table, database, view, or index.
    - DROP: Used to delete an existing database, table, view, or index.
    - ALTER: Used to modify an existing database, table, or view structure.
    - TRUNCATE: Used to remove all records from a table, but the table structure remains.
  
  Example:
  ```sql
  CREATE TABLE Employees (
      ID INT PRIMARY KEY,
      Name VARCHAR(50),
      Age INT
  );
'''

### Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.
'''
- DML (Data Manipulation Language):
  - DML is a set of SQL commands used to manage data within database objects.
  - Examples of DML commands:
    - INSERT: Used to insert new records into a table.
    - UPDATE: Used to modify existing records in a table.
    - *DELETE: Used to remove existing records from a table.

  Examples:
  ```sql
  -- INSERT
  INSERT INTO Employees (ID, Name, Age) VALUES (1, 'John', 30);

  -- UPDATE
  UPDATE Employees SET Age = 31 WHERE ID = 1;

  -- DELETE
  DELETE FROM Employees WHERE ID = 1;
'''

### Q4. What is DQL? Explain SELECT with an example.
'''
- DQL (Data Query Language):
  - DQL is a subset of SQL used to retrieve data from a database.
  - The main command in DQL is **SELECT**, used to fetch data from one or more tables.

  Example:
  ```sql
  SELECT * FROM Employees;
'''

### Q5. Explain Primary Key and Foreign Key.
'''
- Primary Key:
  - A primary key is a column (or combination of columns) that uniquely identifies each row in a table.
  - It must contain unique values and cannot contain NULL values.
  - Example: ID column in Employees table.

- Foreign Key:
  - A foreign key is a column or a set of columns in a table whose values reference a primary key in another table.
  - It establishes a link between two tables.
  - Example: DepartmentID in Employees table referencing the ID column in the Departments table.
'''
### Q6. Write a Python code to connect MySQL to Python. Explain the cursor() and execute() method.


import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

'''
- cursor() method:
  - The `cursor()` method creates a cursor object which is used to execute SQL queries.
  - It allows Python code to execute SQL commands against the database.
  - The `cursor()` method is called on the database connection object (`mydb`).

- execute() method:
  - The `execute()` method of the cursor object is used to execute SQL queries.
  - It takes an SQL query as a parameter and executes it against the connected database.
  - In the example above, `mycursor.execute("SELECT * FROM Employees")` executes a SELECT query to fetch all records from the Employees table.
'''
### Q7. Give the order of execution of SQL clauses in an SQL query.
'''
The general order of execution of SQL clauses in an SQL query is:

1. SELECT: Determines which columns to retrieve.
2. FROM: Specifies the table(s) from which to retrieve the data.
3. WHERE: Filters the rows based on specified conditions.
4. GROUP BY: Groups the rows sharing a common value into summary rows.
5. HAVING: Filters groups based on specified conditions.
6. ORDER BY: Sorts the result set in ascending or descending order.
7. LIMIT/OFFSET: Limits the number of rows returned or skips a specified number of rows.

This is a generalized order, and not all queries will necessarily include all of these clauses.
'''
