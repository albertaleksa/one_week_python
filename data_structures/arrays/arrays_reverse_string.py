def reverse_string(string):
    # check
    if not string or type(string) != str or len(string) < 2:
        return "wrong input"
    data = []
    for i in range(len(string)-1, -1, -1):
        data.append(string[i])
    # data = list(string)
    # n = len(data)
    # for i in range(n // 2):
    #     data[i], data[n-i-1] = data[n-i-1], data[i]

    return "".join(data)


print(reverse_string("Hi, you all"))
print(reverse_string("Hi"))

print((lambda string: string[::-1])("Hi, my name is A"))

