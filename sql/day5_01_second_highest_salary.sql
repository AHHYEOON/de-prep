-- LeetCode 176: Second Highest Salary
-- https://leetcode.com/problems/second-highest-salary/
-- Date: 2026-04-23

-- 풀이: DENSE_RANK Window 함수
-- - RANK 대신 DENSE_RANK 사용 (동점 시 순위 건너뛰지 않음)
-- - 2등 없으면 NULL 반환 필요 → 바깥 SELECT로 감싸기
-- - 중복 제거 위해 DISTINCT

SELECT (
    SELECT DISTINCT salary
    FROM (
        SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
        FROM Employee
    ) AS ranked
    WHERE rnk = 2
) AS SecondHighestSalary;