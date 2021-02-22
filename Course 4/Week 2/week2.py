'''
Week 2
Relational databases model data by storing rows and columns in tables. It can efficiently retrieve dsata from those tables and in particular wher there are multiple tables and the relationships between those tables involved in the query.

database - contains the tables
Relation (aka table) - contains tuples and attributes
tuples (aka rows)- set of fields that generally represents an 'object'
attribute (aka column/field) - one of the possibly many elements of data corresponding to the object represented by the row
schema (aka title)

SQL - Standard Query Language
C - create
R - read
U - update
D - delete

Two Roles in Large Projects
1. Application Developer - builds the logic, look, and feel of the application. also incharge with monitoring for problems
2. Database Administrator - monitors and adjusts the database as the program runs in production

Database Model / Database Schema - the structure or format of a database. This the the application of a data model when used in conjuction 
with a database manahgement system 

CREATE TABLE Users(name VARCHAR(128), email VARCHAR(128)) ## creates a table with schema name and email at 128 characters in each
INSERT INTO Users(name,email) VALUES('Kristn','kf@umich.edu') ## inserts row into a table
DELETE FROM Users WHERE email='fred@umich.edu' ## deletes a row in a table based on a selection criteria
UPDATE Users SET name='Charles' WHERE email='csev@umich.edu' ## allows the updating of a field with a where clause
SELECT* FROM Users WHERE email='csev@umich.edu' ## retrieves a group of records 
SELECT * FROM Users ORDER BY email ## order by clause selects states to get results sorted in ascending or descending order



'''
