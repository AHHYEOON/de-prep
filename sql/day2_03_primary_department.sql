-- LeetCode 1789: Primary Department for Each Employee
-- https://leetcode.com/problems/primary-department-for-each-employee/
-- Date: 2026-04-20
--
-- 배운 것:
-- - CTE (WITH 절) 여러 개 정의
-- - HAVING COUNT(*) = 1
-- - UNION으로 두 조건 합치기

WITH explicit_primary AS (
    SELECT employee_id, department_id
    FROM Employee
    WHERE primary_flag = 'Y'
),
single_dept AS (
    SELECT employee_id, department_id
    FROM Employee
    WHERE employee_id IN (
        SELECT employee_id
        FROM Employee
        GROUP BY employee_id 
        HAVING COUNT(*) = 1
    )
)
SELECT * FROM explicit_primary
UNION 
SELECT * FROM single_dept;