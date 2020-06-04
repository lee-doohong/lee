def show_all(s):
    for i in s : 
        print(i, end = ' ')

# st = [2*i for i in range(1, 10)]
# show_all(st)

# def time2():
#     for i in range(1,10):
#         yield 2* i


show_all((2*i for i in range(1,10)))