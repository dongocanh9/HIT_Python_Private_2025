def sum_digit(x):
    s=0
    for i in str(x):
        s+=int(i)
    return s
a=[123,456,789]
result=([sum_digit(x) for x in a ])
print(result)