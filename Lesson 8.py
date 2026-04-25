# school={
#     "class":[1,2,3,4,5,6,7],
#     "age":[12,16,17,161,15,18],
#     "group":["A","B","D","E","G"]
# }
# for i,g in school.items():
#     print(i,g)
# school.update({"class":[1,34,5,6,7,8,9]})
# a=school.copy()
# print(school)
# school={"crew":[34,35,32,33,30,25,30]}
# print(school)
# # del school["age"]
# # print(school)
# school.popitem()
# print(school)
# print(a)
# school.clear()
# print(school)

a={1,54,65,3,2,4,67,69}
b={2,1,5,7,67,69,54,43,30}
union=a.union(b)
intersection=a.intersection(b)
dif=a.difference(b)
difb=b.difference(a)
print(union)
print(intersection)
print(dif)
print(difb)