USE DreamHome;

-- Subqueries for the Dreamhome database
-- These queries use nested SELECT statements to answer analytical questions

-- List staff members earning more than the average salary
SELECT fname,
       lname,
       salary
FROM staff
WHERE salary > (
    SELECT AVG(salary)
    FROM staff
);

-- List properties with rent above the average rent
SELECT pno,
       street,
       city,
       rent
FROM property_for_rent
WHERE rent > (
    SELECT AVG(rent)
    FROM property_for_rent
);

-- Find branches that have more than the average number of staff
SELECT bno,
       staff_count
FROM (
    SELECT bno,
           COUNT(sno) AS staff_count
    FROM staff
    GROUP BY bno
) AS branch_stats
WHERE staff_count > (
    SELECT AVG(staff_total)
    FROM (
        SELECT COUNT(sno) AS staff_total
        FROM staff
        GROUP BY bno
    ) AS avg_calc
);

-- List renters who have viewed more properties than the average number of viewings
SELECT r.rno,
       r.fname,
       r.lname,
       COUNT(v.pno) AS total_viewings
FROM renter r
INNER JOIN viewing v
    ON r.rno = v.rno
GROUP BY r.rno, r.fname, r.lname
HAVING COUNT(v.pno) > (
    SELECT AVG(viewing_count)
    FROM (
        SELECT COUNT(pno) AS viewing_count
        FROM viewing
        GROUP BY rno
    ) AS viewing_avg
);
