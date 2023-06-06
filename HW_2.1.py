def superset(set1, set2):
    if set1 == set2:
        print("Множества равны")
    elif set1.issuperset(set2):
        print(f"Объект {set1} является чистым супермножеством")
    elif set2.issuperset(set1):
        print(f"Объект {set2} является чистым супермножеством")
    else:
        print("Супермножество не обнаружено")

set1 = {5, 3}
set2 = {3, 4, 5}
superset(set1, set2)
input("press any key to close window")
