-- LeetCode 1148: Article Views I  
-- https://leetcode.com/problems/article-views-i/
-- Date: 2026-04-20

-- 풀이 1: 기본 WHERE
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;

-- 풀이 2: WHERE IN 서브쿼리 (연습용)
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id IN (
    SELECT author_id FROM Views WHERE author_id = viewer_id
)
ORDER BY id;

-- 풀이 3: FROM 절 서브쿼리 (연습용)
SELECT DISTINCT id
FROM (
    SELECT author_id AS id FROM Views WHERE author_id = viewer_id   
) AS t
ORDER BY id;