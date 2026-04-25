# Python 기본 문법 치트시트

작성일: 2026-04-19
작성자: Ahhyeon Jo

---

## 1. 변수와 자료형

### 변수 선언
```python
a = 0
```

### 숫자 자료형
- int: 정수 자료형
- float: 실수 자료형

### 문자열 (str)
- 선언: a = 'a'
- 주요 메서드 5개 (본인이 아는 것만):
  1. split() : 특정 문자를 기준으로 나눠서 리스트로 반환하는 메서드 ("a.b.c".split(".") -> ['a','b','c']) 
  2. replace(a,b) : a 문자를 b로 치환
  3. strip() : 앞뒤 공백(또는 지정 문자) 제거/ lstrip(), rstirp() 도 있음(오른쪽,왼쪽만 제거)
  4. lower(), upper(): 대소문자 변환
  5. join() : 문자열을 특정 문자를 기준으로 하나의 문자열로 합쳐 반환 (''.join(list))


### 불리언 (bool)
- True / False
- 언제 쓰는가: 참과 거짓을 구별할 때 사용

---

## 2. 리스트 (list)

### 선언과 기본 조작
```python
# 빈 리스트 생성: a = []
# 요소 추가: a.append()
# 요소 제거: a.remove(값)-> 값으로 제거(첫 번째 매칭만)
            del a[i]: 인덱스로 제거
            pop([i]): 제거 + 값 반환
# 인덱싱 (첫 번째 요소, 마지막 요소): a[1], a[-1]
# 슬라이싱 (처음 3개, 마지막 3개): a[:3], a[-3:]
```

### 자주 쓰는 메서드
- append(): 요소 추가
- pop(): 요소 삭제
- sort(): 요소 정렬
- reverse(): 요소 역정렬
- len(): 길이 반환
- index(값) : 값이 처음 등장하는 인덱스 반환
 주의 : list.index()의 함정
        - 같은 값이 여러 개면 항상 "처음에 등장하는 인덱스" 반환
        - 중복 있는 리스트에선 서로 다른 요소도 같은 인덱스로 보일 수 있음
        - 인덱스로 순화하고 싶으면 range(len(nums)) 또는 enumerate 사용

### 리스트 컴프리헨션
```python
# 예: 1~10 중 짝수만 제곱한 리스트
# [a**2 for a in range(1,11) if a%2 == 0]
```

---

## 3. 튜플 (tuple)

- 리스트와의 차이점: 
    - 리스트와 똑같은데 수정 불가능(immutable)함.
    - 한 번 만들면 값을 못 바꿈
    - 중복 가능 , 순서 있음(리스트랑 같음)
- 언제 쓰는가: 바뀌면 안 되는 값 (좌표, 설정값 등)
```python
# 예시: a = (1,2,3)
```

---

## 4. 딕셔너리 (dict)

### 선언과 기본 조작
```python
# 빈 dict 생성: a = {}
# 키-값 추가:a[key] = value
# 조회: a[key], a.get(key)
# 삭제: del a[key], a.pop(key)
# 키 존재 확인: key in a
```

### 자주 쓰는 메서드
- get(key): key를 통해 값을 가져오는 메서드, 없으면 None을 반환(기본값 설정할 수 있음) 
- keys(): 딕셔너리에서 키들만 추출하여 반환
- values(): 딕셔너리의 값들만 추출하여 반환
- items(): 딕셔너리의 키와 값의 쌍을 반환

### 순회 (for 반복문)
```python
# dict의 모든 키-값 순회: 
  for key, val in a.items():
    print(key, val)
```

---

## 5. 셋 (set)

- 특징 (핵심 한 줄): 중복 자동 제거되고 순서 없음
- 언제 쓰는가: 중복 제거, 존재 확인(이 값이 이 컬렉션에 있는지 확인하는 것)
```python
# 선언: s1 = set()
# 추가/제거: s1.add() -> 1개의 값만 추가할 때
            s1.update() -> 여러개의 값을 추가할 떄
            s1.remove() -> 특정 값을 제거하고 싶을 때
            s1.discard() -> remove와 비슷하지만 존재하지 않는 값을 제거하려 해도 오류 발생x
            s1.clear() -> 집합의 모든 값을 제거할 떄
# 교집합, 합집합, 차집합:
교집합 : s1 & s2 , s1.intersection(s2)
합집합 : s1 | s2, s1.union(s2)
차집합 : s1 - s2, s1.difference(s2)
# 존재 확인
my_set = {1,2,3,4,5}
print(3 in my_set) # True
# 셋으로 존재 확인 하는 이유: 리스트보다 속도가 빠름 (셋과 딕셔너리는 해시 기반)
```

---

## 6. 조건문

```python
# if-elif-else 기본 구조:
  if 조건:
    실행
  elif 다른 조건:
    실행
  else :
    실행

# 삼항 연산자 (한 줄 if): 결과 참일 때 if 조건 else 거짓일때
# 예시 
result = a ** 2 if a > 0 else 0
```

---

## 7. 반복문

### for 문
```python
# range로 반복: for i in range(10)
# 리스트 순회: for i in a
# enumerate (인덱스와 함께): enumerate(iterable, start = 0) -> 인덱스와 값을 순서쌍으로 반환 (시작 인덱스 설정 가능, 0이 기본값) 
fruits = ['apple', 'banana', 'cherry']
for idx, fruit in enumerate(fruits):
  print(idx, fruit)
# 0 apple
# 1 banana
# 2 cherry
# zip (두 리스트 동시 순회): 두 리스트를 묶어 반복자로 반환
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
  print(name, age)
```

### while 문
```python
# 기본: 
while 조건:
  실행할 코드
  증감이나 조건 변경

# break, continue 의미: break는 즉시 구문을 탈출하기, continue는 그 다음으로 넘어가기
```

---

## 8. 함수

```python
# 기본 함수 정의: 자주 사용하는 계산을 계속 가져다 사용할 수 있도록 하는 것

# 기본 인자 (default argument): 함수 호출 시 값을 안 넘겨도 기본값을 쓰는 인자
def greet(name, greeting="Hello"):
  return f"{greeting}, {name}"

greet("Ahhyeon")
greet("Ahhyeon", "안녕")
# *args, **kwargs 간단 설명:
```

### 람다 함수
```python
# lambda 예시: lambda x, y : x+y
```

---

## 9. 기타 자주 쓰는 것

### print 꿀팁
- f-string: f"{a}"
- 여러 값 출력:f"{a}, {b}"
```python
name = "Ahhyeon"
age = 25
msg = f"내 이름은 {name}이고 {age}살"
# 내 이름은 Ahhyeon이고 25살"

print(f"{3+5}") # "8"
```

### 입력 받기
- input(): 
- 숫자 입력 받기: n = int(input())

### 타입 변환
- int(), str(), float(), list()

---

## 10. 내가 까먹었던 것 / 헷갈리는 것

- 튜플은 수정 불가, 셋은 중복 제거

### Python vs 다른 언어
- 변수 선언 시 'var', 'String' 같은 키워드 없음 (동적 타이핑)
- '++', '--' 연산자 없음 -> '+= 1', '-= 1' 사용
  - '++x' 는 부호 두 번으로 조용히 동작 (증가 x, 함정)
- 세미콜론 ';' 없음 (있어도 동작하지만 관례적으로 안 씀)

### 리스트
- 'list.index(값)' : 처음 등장하는 인덱스만 반환 -> 중복 있으면 함정
- for i in nums 는 "값"을 순회, for i in range(len(nums))는 "인덱스"를 순회, enumerate(nums) 쓰면 둘 다 동시에 가능
- 슬라이싱 끝 인덱스는 미포함

### 딕셔너리
- 딕셔너리의 in 연산자는 "키"만 확인 (값은 안 봄)
- 딕셔너리에는 .index()가 없음 (리스트 전용)
- 값 꺼내기 : 
  - 키가 확실히 있을 때 => 'dict[key]'
  - 없을 수도 있을 때 => 'dict.get(key, 기본값)'
- 설계 원칙 : '검색 기준이 되는 것'을 키로 정해야 함
- dict에 요소 추가는 append가 아니라 a[key] = value

### 시간복잡도 감각
- O(n²) 중첩 루프 -> 리스트 커지면 바로 느려짐
- O(n) 한번 순회 -> 딕셔너리 활용 (값 검색 O(1))
- 해시맵 패턴 : 이미 본 것을 딕셔너리에 저장S

### Python 스코프 / 들여쓰기
- 'return'은 만나는 즉시 함수 종료 -> 위치(들여쓰기) 매우 중요
- 이중 for문에서 'return Flase' 위치:
  - 안쪽 for 안: 첫 번째 i만 체크하고 종료 (버그)
  - 바깥 for 안: 바깥 첫 순회만 하고 종료 (버그)
  - 바깥 for 밖: 모든 i 다 체크한 후 종료 (올바른 위치)

### set 활용 패턴
- 'seen = set()' (빈 셋, {}는 딕셔너리니 주의)
- 'if x in seen: ... ' -> O(1)
- "이미 본 것" 저장하는 패턴 = 해시셋 기본 사용법
- 'len(list) != len(set(list))' -> 중복 존재 확인 원라이너

### 함수 시그니처 / 타입 힌트
- def 함수(인자: 타입) -> 반환타입:
- self: 클래스 메서드 첫 인자 (고정, 자동 전달됨)
- List[int]: int로 구성된 리스트 (from typing import List)
- -> bool: 반환값이 bool
- 힌트는 "강제"가 아니라 "표시" (안 지켜도 에러 안 남)
- 그래도 쓰는 이유: VS Code 자동완성 + 팀 협업 + mypy 검증

### 파일 I/O 주의 사항
- with open() 자동 close 보장, 반드시 사용
- encoding="utf-8" 꼭 사용 (Windows 한글 깨짐 방지)
- f.read()는 문자열 반환 - 받아서 써야 함
- f.write()는 문자열만 받음 (int, float 안 됨)
- 여러 줄 쓸 땐 "\n" 직접 추가
- write()는 인자 1개만 받음 (print와 달리)

### Python의 엄격한 타입 철학
- "Explicit is better than implicit" (Zen of Python)
- 자동 형변환 안 해줌 -> 버그 예방
- 항상 str(x), f"{x}" 로 명시적 변환