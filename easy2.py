
# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.


one_f = ['qiwi', 'banana', 'mango', 'orange']
two_f = ['banana', 'apple', 'qiwi', 'mandarina']
three_f = []


#  нам нужно пройтись по обоим спискам и сравнить их, если нахоядтся одинаковые элементы, то мы добавляем их в новый список

for i in one_f:
    for j in two_f:
        if i != j:
            pass
        else:
            three_f.append(i)
print(three_f)

#  готова