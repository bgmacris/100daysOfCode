def f_len(word):
    count = 0
    for i in word:
        count += 1
    return  count

def f_split(text_string, delimiter):
    lista = []
    word = ''
    for char in text_string:
        if char == delimiter:
            lista.append(word)
            word = ''
        else:
            word = word + char
    if word != '': lista.append(word)
    return lista


def f_sort(num_list):
    for num in range(1, len(num_list)):
        cur_val = num_list[num]
        pos = num
        while pos > 0 and num_list[pos-1] > cur_val:
            num_list[pos] = num_list[pos-1]
            pos = pos - 1
        num_list[pos] = cur_val
    return num_list

def f_join(list_string, delimiter):
    text_string = ''
    for string in list_string:
        text_string = text_string + string + delimiter
    return text_string[:-1]

def f_sum(int_string):
    total = 0
    for i in int_string:
        total = total + i
    return total

def f_max(int_string):
    return f_sort(int_string)[-1]

def f_min(int_string):
    return f_sort(int_string)[0]

print(f_len('word'))
print(f_split('hola, mundo', ','))
print(f_join(['hola', 'mundo'], '-'))
print(f_sum([1, 2, 3]))
print(f_max([3, 5, 1, 2]))
print(f_min([3, 5, 1, 2]))
