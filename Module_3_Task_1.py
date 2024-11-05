# TODO Напишите функцию для поиска индекса товара


def first_in_list(fi, il):
    output = None
    for i in range(len(items_list)):
        if fi != il[i]:
            continue
        else:
            output = i
            break
    return output

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = first_in_list(find_item, items_list)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
