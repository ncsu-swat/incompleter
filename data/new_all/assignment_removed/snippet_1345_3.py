import collections, re
n = int(input('Number of subjects: '))
item_order = collections.OrderedDict()
for i in range(n):
    sub_marks_list = re.split('(\\d+)$', input('Input Subject name and marks: ').strip())
    item_price = int(sub_marks_list[1])
    if subject_name not in item_order:
        item_order[subject_name] = item_price
    else:
        item_order[subject_name] = item_order[subject_name] + item_price
for i in item_order:
    print(i + str(item_order[i]))