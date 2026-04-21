### SQL - 서브쿼리 / CTE / GROUP BY

### GROUP BY 사고법
- "~별로" 집계 -> GROUP BY
- 예: "직원별 부서 개수" -> GROUP BY employee_id, COUNT(*)
- SELECT에는 "GROUP BY 컬럼" 또는 "집계함수"만 올 수 있음

### WHERE - IN (서브쿼리)
- 서브쿼리는 "단일 컬럼의 값 목록"을 반환해야 함
- 바깥 컬럼과 "같은 종류의 값" 이면 ok (이름은 달라도 됨)
- 예: WHERE employee_id IN (SELECT employee_id FROM ... GROUP BY ... HAVING ...)

### HAVING vs WHERE
- WHERE: GROUP BY 전에 적용 (각 행 필터링)
- HAVING: GROUP BY 후 적용 (그룹 필터링)
- HAVING COUNT(*) = 1 => "행이 1개인 그룹만"

### CTE (WITH 절)
- 서브쿼리에 이름 붙여서 미리 정의
- 여러 개는 콤마로: WITH a AS (...), b AS (...) SELECT ...
- UNION: 두 쿼리 결과 합치기 (종복 제거)
- UNION ALL: 중복 제거 안 함 (더 빠름)