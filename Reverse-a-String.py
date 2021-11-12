def reverse1(string):
    return string[::-1]


def reverse2(string):
    my_list = []
    for i in range(len(string)-1, -1, -1):
        my_list.append(string[i])
        print(my_list)
    return "".join(my_list)


print(reverse2("Hi, how are you?"))
