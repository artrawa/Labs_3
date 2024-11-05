# TODO Напишите функцию find_common_participants

def find_common_participants(first_string, second_string, separator = ","):

     first_list = first_string.split(separator)
     second_list = second_string.split(separator)

     first_set = set(first_list)
     intersection_set = first_set.intersection(second_list)
     intersection_list = list(intersection_set)
     sort_list = sorted(intersection_list)
     return sort_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group, participants_second_group, '|')


# TODO Провеьте работу функции с разделителем отличным от запятой
