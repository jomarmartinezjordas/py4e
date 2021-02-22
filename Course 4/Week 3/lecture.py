'''
BUilding a Data Model
- Basic Rule: Don't put the same string data in twice - use a relationship instead
- When there is one thing the 'real world', there should be one copy of that thing in the database

Primary key - way for us to refer to a particular row; one key for every row ; aka unique number
Logical key - that unuique thing that we might use to look up this row from the outside world
Foreign key - column points that we add to be the starting point of the arrows

### Creating the Genre Table using SQL
CREATE TABLE Artist(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT)

### Creating the Genre Table using SQL
CREATE TABLE Genre(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT)

### Creating the Album Table using SQL
CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    name TEXT)

### Creating the Tracks Table using SQL
CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER)