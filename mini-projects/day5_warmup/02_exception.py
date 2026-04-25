print("=" * 40)
print("과제 1: 숫자 나누기")
print("=" * 40)

user_input = input("숫자를 입력하세요: ")

try:
    num = int(user_input)
    result = 2 / num
    print(f"결과: {result}")
except ValueError as e:
    print(f"[에러] 숫자가 아닙니다: {e}")
except ZeroDivisionError as e:
    print(f"[에러] 0으로 나눌 수 없습니다: {e}")
print("프로그램은 계속 진행됩니다.")

print("\n과제 2: 없는 파일 읽기")
print("=" * 40)

try:
    with open("없는파일.txt", "r", encoding="utf-8") as f:
        content = f.read()
    print(content)
except FileNotFoundError as e:
    print(f"[에러] 파일 없음: {e}")
print("프로그램은 계속 진행됩니다")

print("\n과제 3: 딕셔너리 키 조회")
print("=" * 40)

my_dict = {"name": "아현", "age": 25}

try:
    value = my_dict["email"]
    print(value)
except KeyError as e:
    print(f"[에러] 해당 키 없음: {e}")
print("프로그램은 계속 진행됩니다.")



print("\n과제 4: 여러 에러 처리")
print("=" * 40)

numbers = ["10", "5", "abc", "0", "20"]

for n in numbers:
    try:
        num = int(n)
        result = 100 / num
        print(f"{n} -> {result}")
    except ValueError as e:
        print(f"[에러] 숫자가 아닙니다: {e}")
    except ZeroDivisionError as e:
        print(f"[에러] 0으로 나눌 수 없습니다: {e}")
    
print("프로그램은 계속 진행됩니다.")