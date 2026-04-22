-- LAG 연습: 일별 매출 증감액
-- Date: 2026-04-22
-- 환경: DB Fiddle (PostgreSQL)

-- 테이블 생성
CREATE TABLE daily_sales (
    date DATE,
    sales INT
);

INSERT INTO daily_sales (date, sales) VALUES
('2026-04-15', 1000),
('2026-04-16', 1500),
('2026-04-17', 1200),
('2026-04-18', 1800),
('2026-04-19', 2000);

-- 풀이: 전날 대비 증감액
SELECT 
    date, 
    sales, 
    LAG(sales, 1) OVER (ORDER BY date) AS prev_sales,
    sales - LAG(sales, 1) OVER (ORDER BY date) AS diff 
FROM daily_sales;

-- 배운 것:
-- 1. LAG(컬럼, n) OVER (ORDER BY ...) = n번째 이전 행의 값
-- 2. 첫 행은 NULL (이전이 없음)
-- 3. 컬럼 간 산술 연산 (-, +, *, /) 가능
-- 4. NULL과 연산하면 결과는 NULL