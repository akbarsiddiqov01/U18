university={
    "kim":"kimyo",
    'cal':'calculus',
    "eco":"economy",
}
# print(university["kim"])
# print(university["cal"])
# print(university["eco"])
university["davhuq"]="davlat va huquq"
university.update({"kim":"kim bor"})
del university["cal"]
print(university)