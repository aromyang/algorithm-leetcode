# Write your MySQL query statement below
SELECT 
    a.machine_id,
    ROUND(SUM(CASE WHEN a.activity_type = 'end' THEN a.timestamp ELSE -a.timestamp END) / COUNT(DISTINCT a.process_id), 3) 
        AS processing_time
FROM Activity a
GROUP BY a.machine_id