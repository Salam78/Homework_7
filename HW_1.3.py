fruits = ("banana", "apple", "bananamango", "mango", "strawberry-banana")

fruit = input("Введите название фрукта: ")
count = 0
for item in fruits:
    if fruit in item:
        count += 1

print(f"Количество раз, когда {fruit} является частью элемента:", count)
input("press any key to close window")
