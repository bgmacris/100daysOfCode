def insertion_sort(num_list):
    for num in range(1,len(num_list)):
        cur_val = num_list[num]
        pos = num		
        while pos > 0 and num_list[pos-1] > cur_val :
            num_list[pos] = num_list[pos-1]
            pos = pos -1
        num_list[pos]= cur_val      
    return num_list


print(insertion_sort([100,15,93,43,77,31,11,27,20]))