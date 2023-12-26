# exm_list = [3, 4, 5, 9]
#
# print(list("Arindam"))
# print(3 in exm_list)
# print(3 not in exm_list)
# print(10 in exm_list)
# print(10 not in exm_list)

# mixed = ["false", 365, 4.24, "this is a string"]
# print(mixed[3])
# print(mixed[1]+5)
# print(mixed[0]+"ify")
# print(mixed[-2])
#
# print(mixed[:3])
# print(mixed[2:])
# print(mixed)
# mixed[1] = 400
#
# print(mixed)
#
# assign_list = [[0, 2], [4, 6], [8, 10], [12, 14]]
# print(assign_list[0])
# print(assign_list[3][1])
# assign_list2 = ["chair", "table", "desk", "lamp", "bed"]
# print(assign_list2[-5])
# print("Most people own at least {} {}s".format(assign_list[0][1], assign_list2[0]))
# assign_list3 = [0.98, 8.76, 6.54, 4.32]
# print(assign_list3[1:])
# print(assign_list3[1:3])
# print(assign_list3[0:2])
#
# planets = ["ab", "bc", "ab", "cd", "de"]
# del planets[2]
# print(planets)
# print(planets.remove("ab"))
# print(planets)
# print(planets.append("mars"))
# print(planets)
# print(planets.insert(0, "earth"))
# print(planets)
# animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
# del animals[4]
# print(animals)
# animals.remove("elephant")
# print(animals)
# animals.append("arctic fox")
# print(animals)
# animals.insert(2, "snowy owl")
# animals.sort(reverse=True)
# print(animals)
# print(animals.index("reindeer"))
# print(animals.pop())
# consoles = {"nintendo": "wii", "microsoft": "xbox"}
# print(consoles["microsoft"])
# print(consoles)
# print("microsoft" in consoles)
# print(consoles.items())
#
# for key, value in consoles.items():
#     print(key, value)
#
# dict_personas = {"Queen": "Bohemian Rhapsody",
#                  "Bee Gees": "Stayin' Alive",
#                  "U2": "One",
#                  "Michael Jackson": "Billie Jean",
#                  "The Beatles": "Hey Jude",
#                  "Bob Dylan": "Like A Rolling Stone"
#                  }
# print(len(dict_personas))
#
# print(dict_personas.keys())
# for key in dict_personas.keys():
#     print(key)
#
# for value in dict_personas.values():
#     print(value)

# for key, value in dict_personas.items():
#     print(key,value)

# print(dict_personas.get("Promise of the Real"))
#
# dict_new = dict.fromkeys("bcd", "consonent")
# print(dict_new)
#
# fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
# print(fast_food_items.pop("McDonald's"))
# print(fast_food_items.popitem())

# internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
# new_celebs = internet_celebrities.copy()
# internet_celebrities.clear()
# print(internet_celebrities)
# print(new_celebs)
# another_one = {"shroud": "Twitch"}
# internet_celebrities.update(another_one)
# empty = dict()
# print(empty)
# letter_dict = dict(a=1, b=2, c=3)
# print(letter_dict)

# tuple_1 = tuple("a", "b")
# tuple_5 = tuple([3.15, 2.204, 10])
# tuple_6 = tuple("eddffr")
# print(tuple_1)
# print(tuple_5)
# print(tuple_6)
# major_cities = ("Tokyo", "Kolkata", "Delhi")
# count = 0
# back = len(major_cities) - 1
# while count < len(major_cities):
#     print(major_cities[count])
#     count += 1
#
# while back >= 0:
#     print(major_cities[back])
#     back -= 1
#
# nexted = ((1, 2, 3), (4, 5, 6))
#
# fruits = {"apple", "tomato"}
# fruits.add("orange")
# print(fruits)
#
#
# def sleep_in(weekday, vacation):
#     if not weekday or vacation:
#         return True
#     else:
#         return False


s = "hi"
st = ""
for times in range(1, 4):
    st += s
    print(st)

n = 111
print(abs(100-n))

