# from random import randint 

# sample = [x for x in randint(1, 100)]
# import random

# sample = []
# for i in range(5):
# 	sample.append(random.randint(1, 100))

# print(sample)
# # print(result)

# # def min_index(a:list):
# #     min = 0
# #     for i in range(len(a)):
# #         if a[i] < a[min]:
# #             min = i
# #     return min

# # # print(min_index(sample))

# # def machine_sorting(a:list):
# #     b = []
# #     while a: b.append(a.pop(min_index(a)))
# #     print(b)        

# # machine_sorting(sample)
# # print(sorting_machine(sample))

# def sor(a):
#     count = 0
#     for i in range(0, len(a)-1):
#         for j in range(i+1, len(a)):
#             if a[i] < a[j]:
#                 a[i], a[j] = a[j], a[i]
#                 count += 1
#     return a, count

# print(sor(sample))

sample1 = [7, 58, 65, 8, 95]
# sample1.sort()
# prin/t(sample1)

# def find_index(r, v): #리스트 r에서 v가 들어가야 하는 위치를 알려주는 함수 / 리스트 r은 sorting 되어 있다고 가정한다.
#     result_index = 0 # 결과 값은 일단 0부터 시작한다.
#     for i in range(len(r)):
#         if v < r[i]:
#             result_index = i
#             break
#     return result_index

# # print(find_index(sample1, 77))  

# def sort(r): #리스트 r에서 숫자를 차례대로 뺀다음 결과 list에 순서에 맞게 집어 넣는 함수 만들기
#     first_num = r.pop(-1)
#     result = [first_num]
#     while r:
#         a = r.pop(-1) #r에서 첫번째 수를 뺐다.
#         result.insert(find_index(result, a), a)
#     return result

# print(sort(sample1))


# def sort(a:list):
#     for i in range(1, len(a)):
#         key = a[i]
#         j = i - 1
#         while j>=0 and a[j] > key:
#             a[j+1] = a[j]
#             j -= 1
#         a[j+1] = key
#     return(a)

# print(sort(sample1))
# a = [1, 2, 3]
# b = {}
# for k, v in enumerate(a):
#     b[k] = v
# print(b)

# def sort(a):
#     n = len(a)
#     if n <=1 :
#         return a
#     mid = n // 2 # // 은 나눈 몫이 정수가 되는 것임 / 은 나눈몫이 실수 % 은 나머지가 나오는 것
#     g1 = sort(a[mid:])
#     g2 = sort(a[:mid])
#     result = []
#     while g1 and g2 : 
#         if g1[0] > g2[0]:result.append(g2.pop(0))
#         else : result.append(g1.pop(0))
#     while g1 : result.append(g1.pop(0))
#     while g2 : result.append(g2.pop(0))
#     return result

# # print(sort(sample1))
# def add_all(n):
#     if n == 1 : return 1
#     return  n + add_all(n-1)

# print(add_all(100))

# def factorial(n):
#     if n == 1 : return 1
#     return n*factorial(n-1)
# print(factorial(100))


def checkio(numbers_array: tuple) -> list:
    return numbers_array

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(list(checkio((-20, -5, 10, 15))))d

    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
