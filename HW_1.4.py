car_brands = ("BMW", "Nissan", "Ford", "Toyota", "Hyundai", "Lada")

brand = input("Введите название производителя: ")
replacement = input("Введите слово для замены: ")

new_car_brands = tuple(replacement if item == brand else item for item in car_brands)
print("Измененный кортеж:", new_car_brands)
input("press any key to close window")
