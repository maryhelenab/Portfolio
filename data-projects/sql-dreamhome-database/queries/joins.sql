USE DreamHome;

-- JOIN queries for the Dreamhome database
-- These queries combine data from multiple related tables

-- List renters who have viewed properties along with any comments
SELECT r.fname,
       r.lname,
       v.pno,
       v.comment
FROM renter r
INNER JOIN viewing v
    ON r.rno = v.rno;

-- List staff members with their branch details
SELECT s.sno,
       s.fname,
       s.lname,
       b.bno,
       b.street,
       b.city
FROM staff s
INNER JOIN branch b
    ON s.bno = b.bno;

-- Show the staff member responsible for property PA14
SELECT s.fname,
       s.lname,
       p.pno
FROM property_for_rent p
INNER JOIN staff s
    ON p.sno = s.sno
WHERE p.pno = 'PA14';

-- List branches and properties located in the same city
SELECT b.bno,
       b.city,
       p.pno,
       p.street
FROM branch b
INNER JOIN property_for_rent p
    ON b.city = p.city;

-- List all branches and any associated properties (including branches without properties)
SELECT b.bno,
       b.city,
       p.pno
FROM branch b
LEFT JOIN property_for_rent p
    ON b.bno = p.bno;

-- Display full details of staff working in Glasgow branches
SELECT s.*
FROM staff s
INNER JOIN branch b
    ON s.bno = b.bno
WHERE b.city = 'Glasgow';

-- Display owners and properties for rent in Glasgow
SELECT o.fname,
       o.lname,
       p.pno,
       p.street,
       p.city
FROM owner o
INNER JOIN property_for_rent p
    ON o.ono = p.ono
WHERE p.city = 'Glasgow';
