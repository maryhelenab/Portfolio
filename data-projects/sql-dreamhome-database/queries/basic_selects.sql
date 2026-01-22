-- Basic SELECT queries for the Dreamhome database
-- These queries retrieve and filter data from individual tables

USE DreamHome;

-- List all properties available for rent
SELECT *
FROM property_for_rent;

-- List all branches
SELECT *
FROM branch;

-- List all staff members
SELECT *
FROM staff;

-- List staff members working at branch B5
SELECT *
FROM staff
WHERE bno = 'B5';

-- List staff members working at branch B5 or B3
SELECT *
FROM staff
WHERE bno IN ('B5', 'B3');

-- List staff contact details
SELECT sno, fname, lname, address, telno
FROM staff;

-- List properties with rent greater than 400
SELECT pno, street, city, rent
FROM property_for_rent
WHERE rent > 400;

-- List properties with rent between 355 and 470
SELECT pno, street, city, rent
FROM property_for_rent
WHERE rent BETWEEN 355 AND 470;
