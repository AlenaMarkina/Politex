src = not False and True or False and not True

# TODO расписать упрощение выражения

# result = True and True or False and False  # избавляемся от not
# result = True or False  # избавляемся от and
# result = True  # избавляемся от or

result = True  # TODO подставить результат выражения

print(src == result)
