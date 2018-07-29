import json


class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Test("Dan", 3)

print p1.name

x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y.age)

thistuple = ("apple", "banana", "cherry")
for val in thistuple:
    print(val)
