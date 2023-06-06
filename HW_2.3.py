def set_gen(numbers):
    result_set = set()
    count_dict = {}

    for num in numbers:
        if num not in result_set:
            result_set.add(num)
            count_dict[num] = 1
        else:
            count_dict[num] += 1
            string_num = str(num) * count_dict[num]
            result_set.add(string_num)

    return result_set

# Пример использования функции
numbers = [1, 2, 3, 4, 4, 4, 5, 5, 6]
result = set_gen(numbers)
print(result)
input("press any key to close window")
