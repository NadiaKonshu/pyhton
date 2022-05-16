def my_func(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    result = sum(my_list) - min(my_list)
    return result
print(my_func(5,2,1))