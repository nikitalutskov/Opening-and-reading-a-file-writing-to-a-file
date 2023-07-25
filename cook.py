def write_cook_book(file_name, cook_book):
    with open(file_name, 'w', encoding='utf-8') as file:
        for dish_name, ingredients in cook_book.items():
            file.write(dish_name + '\n')
            file.write(str(len(ingredients)) + '\n')
            for ingredient in ingredients:
                ingredient_info = f"{ingredient['ingredient_name']} | {ingredient['quantity']} | {ingredient['measure']}\n"
                file.write(ingredient_info)


def read_cook_book(file_name):
    cook_book = {}

    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        dish_name = lines[i].strip()
        ingredient_count = int(lines[i + 1])

        ingredients = []
        for j in range(ingredient_count):
            ingredient_info = lines[i + 2 + j].strip().split(' | ')
            ingredient_name = ingredient_info[0]
            quantity = int(ingredient_info[1])
            measure = ingredient_info[2]

            ingredient = {
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            }
            ingredients.append(ingredient)

        cook_book[dish_name] = ingredients
        i += 2 + ingredient_count

    return cook_book
# 1 TASK
file_name = 'recipes.txt'
cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}
    ]
}

write_cook_book(file_name, cook_book)
read_cook_book(file_name)
print(cook_book)
# 2 TASK
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cook_book(file_name)
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count

                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {
                        'measure': measure,
                        'quantity': quantity
                    }

    return shop_list
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count)
print(shop_list)
# 3 TASK
with open('1.txt', 'w') as file1:
    file1.write('Строка номер 1 файла номер 1\n')
    file1.write('Строка номер 2 файла номер 1\n')

with open('2.txt', 'w') as file2:
    file2.write('Строка номер 1 файла номер 2\n')
file1_lines = []
with open('1.txt', 'r') as file1:
    file1_lines = file1.readlines()
file1_lines_count = len(file1_lines)

file2_lines = []
with open('2.txt', 'r') as file2:
    file2_lines = file2.readlines()
file2_lines_count = len(file2_lines)

info_list = []
info_list.append(('1.txt', file1_lines_count, ''.join(file1_lines)))
info_list.append(('2.txt', file2_lines_count, ''.join(file2_lines)))

info_list.sort(key=lambda x: x[1])

with open('3.txt', 'w') as file3:
    for info in info_list:
        file3.write('{}\n'.format(info[0]))
        file3.write('{}\n'.format(info[1]))
        file3.write('{}\n'.format(info[2]))
        file3.write('\n')

