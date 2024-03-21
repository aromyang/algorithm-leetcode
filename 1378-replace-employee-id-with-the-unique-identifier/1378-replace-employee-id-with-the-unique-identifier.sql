# Write your MySQL query statement below
SELECT COALESCE(eu.unique_id, NULL) as unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu ON e.id = eu.id;