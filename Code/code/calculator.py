def add(first, second):

    if not isinstance(first, int):
        return 'not a valid integer'
    if not isinstance(second, int):
        return 'not a valid integer'
    else:
        sum = first + second
        return sum

result = add('7', 5) 
print(type(6))