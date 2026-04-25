with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Hello, 아현!")

with open("hello.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

with open("numbers.txt", "w", encoding="utf-8") as f:
    for i in range(1,11):
        f.write(str(i) + "\n")