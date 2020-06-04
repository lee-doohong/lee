# # data = [1, 2, 3, 4, 5]
# # result = []
# # while data:
# #     b = data.pop()
# #     result.append(b)

# # print(result)

# from datetime import datetime, timedelta

# time1 = datetime(2020, 2, 22, 9)
# print(time1)
# time2 = datetime.now()
# print(time2)
# print(time2 - time1)
# for i in range(50) : 
#     print(time1+timedelta(days = 5*i))
"^는 문자열의 처음을 의미하고 $은 문자열의 마지막을 의미한다."
"[]는 []사이의 문자들과 매치라는 의미"
"{}는 반복횟수를 고정시키는 것, a{2, 3}는 a가 2~3번 반복되면 매치한다는 의미이다."
"|는 A|B A or B 라는 의미"
"+, *, [], {}등의 메타문자는 매치가 진행될때 현재 매치되고 있는 문자열의 위치가 변경된다. 이를 소비된다고 표현한다 -> 무슨소리지.."
"\A는 re.MULTILINE 옵션과 관계없이 전체 문자열의 처음하고만 매치된다. \Z는 문자열의 끝과 매치된다. 역시 re.MULTILINE 옵션과 관계 없이 문장의 젤마지막"
import re

# p = re.compile(r'\section')
# m = p.match(' ection')
# print(m)
p = re.compile('\Bclass\B')
print(p.search("no Aclass at all"))
# data = """section python one 
# life is too short
# python two
# you need python
# python three"""

# print(p.findall(data))
# m = p.match('PYTHON')
# print(m)

