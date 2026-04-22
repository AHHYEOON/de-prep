-- LeetCode 184: Department Highest Salary
-- https://leetcode.com/problems/department-highest-salary/
-- Date: 2026-04-22

-- Window Function 첫 문제!
-- RANK() + CTE + JOIN 조합

WITH ranked AS (
    SELECT 
        e.name AS Employee,
        e.salary AS Salary,
        e.departmentId,
        RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rnk
    FROM Employee e
)
SELECT 
    d.name AS Department,
    r.Employee,
    r.Salary 
FROM ranked r
JOIN Department d ON r.departmentId = d.id
WHERE r.rnk = 1;

-- 핵심 학습:
-- - Window 함수는 WHERE에서 직접 못 씀 → CTE로 감싸기
-- - PARTITION BY로 부서별 그룹 나누기
-- - RANK() DESC로 최고 연봉 1등
-- - 동점자 여러 명 자동 처리 (IT 부서 Jim/Max 둘 다)