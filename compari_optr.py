# print(4 > 3)
# print(4 < 3)
# print(4.0 == 4)
# print(4 != 3)
# print(4 >= 3)
# print("Hello" == "Hello")
# print("hello" != "world")

# boolean operator
# print(4 > 1 and "word" == "word")
# print(8.64 == 8.6400 and 2 != 2)
# print("earth" == "Earth" and 6 <= 3)
# print(10 == 5 and 10 != 5)

# print(4 > 1 or "word" == "word")
# print(8.64 == 8.6400 or 2 != 2)
# print("earth" == "Earth" or 6 <= 3)
# print(10 == 5 or 10 != 5)

# print(not 4536 > 0)
# print(not "python" != "Python")

# veg = input("Type your fav vaeg:")
#
# if veg == "corn":
#     print("the veg is corn.")
# else:
#     print("the veg is not corn")
# gpa = float(input("entr you gpa:"))
#
#
# if gpa >= 3.7:
#     inst_app = input("is approved ins?")
#     if inst_app == "yes" or inst_app == "y":
#         print("applicant qualify")
#     else:
#         print("not an approved inst")
# else:
#     print("gpa not qualify for loan")

# score = int(input("enter your score:"))
#
# if score < 0 or score > 100:
#     print("Not a valid score")
# elif score >= 90:
#     print("A grade")
# else:
#     if score >= 80:
#         print("B grade")
#     else:
#         if score >= 70:
#             print("C grade")
#         else:
#             if score >= 60:
#                 print("D grade")
#             else:
#                 print("F grade")

# string_ex = input("enter something")
#
# if string_ex:
#     print("yes u entered")
# else:
#     print("you need to enter here")

list1 = [100, 200, 300]
list1.reverse()
print(list1)

list2 = ["M", "na"]
list3 = ["y", "me"]
list4 = [i + j for i, j in zip(list2, list3)]
print(list4)

numbers = [1,2,3,4,5]
result = []
for i in numbers:
    result.append(i*i)
    print(result)

list5 = ["Hello", "take"]
list6 = ["Dear", "Sir"]
list7 = []
for i in list5:
    for j in list6:
        list7.append(i+" "+j)
print(list7)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
res = dict(zip(keys, values))
print(res)
#################################Dictionary###########################
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}
dict4 = dict1.copy()
dict4.update(dict2)
print(dict3)
print(dict4)

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class']['student']['name'])
print(sampleDict['class']['student']['marks']['history'])

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

emp = dict.fromkeys(employees, defaults)
print(emp['Emma'])

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
rest = dict()
for k in keys:
    rest.update({'lastname' : 'arindam', 'city' : 'kolkata'})
    rest.update({k: sample_dict[k]})

rest.pop('name')
print(rest)

sample_dict = {'a': 100, 'b': 200, 'c': 300}
for k in sample_dict.values():
    print(k)
#################################### Tuple #################################
tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple1[::-1]
print(tuple1)

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][0])

tuple1 = (50,)
print(tuple1)

tuple1 = (10, 20, 30, 40)
a, b, c, d = tuple1
print(a)

tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple1)

tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)

tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[0]))
print(tuple1)

tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(10))