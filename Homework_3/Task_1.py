# Дан список повторяющихся элементов. Вернуть список с дублирующимися
# элементами. В результирующем списке не должно быть дубликатов.
# [1, 2, 3, 1, 2] -> [1, 2]
def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))


my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(find_duplicates(my_list))
