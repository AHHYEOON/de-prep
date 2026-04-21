sql-- LeetCode 595: Big Countries
-- https://leetcode.com/problems/big-countries/
-- Date: 2026-04-20

SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;