# SQL 치트시트

작성일: 2026-04-21
작성자: Ahhyeon Jo

---

## 1. 기본 SELECT

```sql
-- 기본 구조
SELECT 컬럼1, 컬럼2
FROM 테이블명
WHERE 조건
ORDER BY 컬럼 ASC/DESC;
```

### 실무 스타일
- SQL 키워드는 대문자 (SELECT, FROM, WHERE)
- 끝에 세미콜론(;)
- 정렬 기본값: ASC (생략 가능)

---

## 2. DISTINCT, AS, LIMIT

- `DISTINCT`: 중복 제거
- `AS`: 별칭 (컬럼/테이블 이름 바꾸기)
- `LIMIT n`: n개까지만 출력
- `LIMIT n OFFSET m`: m개 건너뛰고 n개 출력
    예: LIMIT 5 OFFSET 10 -> 11번째부터 5게 (페이지네이션에 사용)

---

## 3. GROUP BY & 집계함수

### 사고법
> "~별로" 세고/합치고 싶을 때 → GROUP BY ..

### 집계 함수
- COUNT(*): 행 개수 
- SUM(): 총합
- AVG(): 평균
- MAX(), MIN(): 최대/최소

### GROUP BY + SELECT 규칙
- SELECT에 올 수 있는 것: GROUP BY 컬럼, 집계 함수
- 올 수 없는 것: 올 수 있는거 외 전부

### WHERE vs HAVING
- WHERE: HAVING절 보다 먼저 실행, 행 조건 
- HAVING: WHERE절 이후 실행, 그룹별 조건 

예시:
```sql
-- 부서별 평균 연봉, 평균 50000 이상인 부서만
SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) >= 50000;
```

---

## 4. JOIN (어제 간단히 복습만)

### INNER JOIN 
- 두 테이블 중 **ON 조건이 매칭되는 행만** 출력
- 한쪽에만 있는 행은 제외

### LEFT JOIN (LEFT OUTER JOIN)
- **왼쪽 테이블 전체** + 오른쪽은 매칭되는 것만
- 매칭 안 되면 오른쪽 컬럼은 NULL

### RIGHT JOIN (RIGHT OUTER JOIN)
- **오른쪽 테이블 전체** + 왼쪽은 매칭되는 것만
- 실무에선 잘 안 씀 (LEFT로 바꿔 쓰는 게 일반적)

### FULL OUTER JOIN
- 양쪽 다 전체, 매칭 안 되는 쪽은 NULL
- MYSQL은 직접 지원 X -> UNION으로 구현

### 기본 문법
```sql
SELECT 컬럼들
FROM 테이블A a
LEFT JOIN 테이블B b ON a.key = b.key;
```

### JOIN 시 주의
- ON 조건 빠뜨리면 Cartesian Product (행 수 폭발)
- 같은 컬럼명 있으면 `테이블.컬럼` 으로 구분

### JOIN 실행 순서
- FROM + JOIN이 가장 먼저 (WHERE보다 먼저)
- LEFT JOIN + WHERE 조건 시 주의:
    - WHERE에 걸면 INNER JOIN처럼 동작 (NULL 제거됨)
    - LEFT JOIN 의도 유지하려면 ON 절에 조건 포함

---

## 5. 서브쿼리 (Subquery)

### 3가지 위치

**1) WHERE 절 서브쿼리**
```sql
-- 평균 이상인 사람
SELECT name FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

**2) WHERE ~ IN (서브쿼리)**
- 서브쿼리 결과가 "값 목록"
- 바깥 컬럼과 "같은 종류의 값"이어야 비교 가능
- 컬럼명은 달라도 OK

```sql
-- 예시
WHERE employee_id IN (
    SELECT employee_id FROM ... GROUP BY ... HAVING ...
)
```

**3) FROM 절 서브쿼리 (가상 테이블)**
```sql
SELECT ...
FROM (
    SELECT ... FROM ... WHERE ...
) AS 별칭
```

### ⚠️ IN 서브쿼리 주의
- 서브쿼리는 "단일 컬럼"만 반환해야 함
- 여러 컬럼 비교 필요하면 JOIN 사용

### 서브쿼리 읽는 법
- 안쪽부터 실행된다고 생각
- 안쪽 결과 → 바깥이 받아서 사용

---

## 6. CTE (WITH 절)

### 개념
- 서브쿼리에 이름 붙여서 미리 정의
- 본 쿼리에서 테이블처럼 사용

### 문법
```sql
WITH 이름 AS (
    서브쿼리
)
SELECT * FROM 이름;
```

### 여러 CTE
```sql
WITH cte1 AS (...),
     cte2 AS (...)
SELECT ...
FROM cte1 JOIN cte2 ON ...;
```

### 언제 쓰나
- 여러 개의 서브쿼리가 필요할 떄
- 같은 서브쿼리를 여러 번 참조해야 할 떄
- 쿼리가 복잡해서 "단계별로 쪼개서" 읽기 쉽게 만들고 싶을 때
- 재귀 쿼리: 계층 구조 탐색 (직원-상사, 카테고리 트리 등)

---

## 7. UNION / UNION ALL

- `UNION`: 두 쿼리 결과 합치기, **중복 제거**
- `UNION ALL`: 합치기만, 중복 유지 (더 빠름)

### 조건
- 컬럼 개수 같아야 함
- 컬럼 타입 같아야 함
- 컬럼 이름은 **첫 번째 쿼리 기준**으로 표시됨

```sql
SELECT name FROM group_a
UNION
SELECT name FROM group_b;
```

---

## 8. Window Function (오늘 배울 것 - 빈 칸으로 두기)

### 개념
- 각 행을 유지하면서 옆에 "그룹 기반 집계값" 추가
- GROUP BY는 행을 줄이지만, Window는 행 수 유지

### 기본 문법
```sql
함수() OVER (
    PARTITION BY 그룹기준
    ORDER BY 정렬기준
)
```
- PARTITION BY : GROUP BY와 비슷한 역할 (생략 가능)
- ORDER BY : 그룹 안에서의 순서 (순위/누적합/LAG 등에 필요)

### 주요 함수
| 함수 | 용도 |
|------|------|
| RANK() | 순위 (동점 같은 등수, 다음 건너뜀: 1,2,3.4) |
| DENSE_RANK() | 순위 (동점 같은 등수, 건너뛰지 않음: 1,2,2.3) |
| ROW_NUMBER() | 단순 순번 (동점 무시: 1,2,3,4) |
| SUM() OVER | 누적합 또는 그룹 합계 |
| AVG() OVER | 그룹 평균 |
| LAG(컬럼, n) | n번째 이전 행의 값 (첫 행은 NULL) |
| LEAD(컬럼, n) | n번째 다음 행의 값 |

### 주의
- WHERE 절에서 Window Function 직접 사용 불가
- -> CTE 또는 FROM 서브쿼리로 감싸야 함

### 실무 패턴
- "부서별 1등" -> RANK() + WHERE rnk = 1
- "이번 달 vs 지난 달" -> LAG() 활용
- "누적 매출" -> SUM() OVER (ORDER BY date)
- "최근 N일 이동평균" -> AVG() OVER (ORDER BY date ROWS BETWEEN)

### Window 함수 사용 위치
- SELECT 절
- ORDER BY 절 (잘 안씀)
- x(안되는 것) WHERE, HAVING, GROUP BY 절 -> CTE로 감싸야 함

### Window 함수 + WHERE 필터링 공식
항상 CTE 또는 서브쿼리 감싸기:

```sql
WITH ranked AS (
    SELECT ..., RANK() OVER (...) AS rnk FROM ...
)
SELECT * FROM ranked WHERE rnk = 1;
```
---

## 9. 내가 헷갈렸던 것 / 까먹은 것

- WHERE IN 서브쿼리에서 SELECT에 뭘 넣어야 할지 헷갈림
 -> 바깥 WHERE의 컬럼과 같은 "종류의 값"을 반환하게 SELECT
- UNION은 컬럼 개수/타입이 일치해야 함
- CTE 여러 개 정의 시 WITH 한 번만 쓰고 콤마로 연결
- GROUP BY 결과에서 조건 걸고 싶으면 WHERE 아니라 HAVING
- LIMIT OFFSET의 정확한 의미(m개 건너뛰고 n개)