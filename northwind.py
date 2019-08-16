import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# read available tables
query = """SELECT name 
FROM sqlite_master 
WHERE type='table' 
ORDER BY name;"""
curs.execute(query)
table_avail = curs.fetchall()
print("Tables available: ", table_avail)

# See schema
query = """SELECT sql 
FROM sqlite_master 
WHERE name = 'Customer'"""
curs.execute(query)
schema = curs.fetchall()
print("Schema used: ", schema)

# What are the ten most expensive items (per unit price) in the database?
query = """SELECT ProductName, UnitPrice 
FROM Product 
ORDER BY UnitPrice DESC
LIMIT 10;"""
curs.execute(query)
top_ten = curs.fetchall()
print("Top ten expensive items: ", top_ten)

# Average age of Employees at time of hiring
query = """SELECT HireDate, AVG(BirthDate)
FROM Employee
GROUP BY HireDate
UNION
SELECT HireDate, AVG(BirthDate) FROM Employee"""
curs.execute(query)
avg_age = curs.fetchall()
print("Avg age of employees at hiring :", avg_age)

# STRETCH GOAL: Looks like cites in Washington State hires older people
query = """SELECT HireDate, AVG(BirthDate), City
FROM Employee
GROUP BY City
UNION
SELECT HireDate, AVG(BirthDate), City FROM Employee"""
curs.execute(query)
stretch = curs.fetchall()
print("Age hired difference by city: ", stretch)

# What are the ten most expensive items (per unit price) in the database AND their Supplier?
# Join Product and Supplier on UnitPrice = Company name
query = """SELECT ProductName, UnitPrice, CompanyName
FROM Product
INNER JOIN Supplier 
ON UnitPrice = CompanyName
ORDER BY UnitPrice DESC
LIMIT 10;"""
curs.execute(query)
top_ten_sup = curs.fetchall()
print("Top ten expensive items and suppliers: ", top_ten_sup)

# Who is the employee with the most territory

query = """SELECT FirstName, COUNT(TerritoryId) 
FROM Employee
INNER JOIN EmployeeTerritory 
ON FirstName = TerritoryId"""
curs.execute(query)
T = curs.fetchall()
