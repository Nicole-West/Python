# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, arg=','):
    first_group_list = list(set(participants_first_group.split(arg)))
    second_group_list = list(set(participants_second_group.split(arg)))
    result = set(first_group_list).intersection(second_group_list)
    return list(result)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group, participants_second_group, '|')