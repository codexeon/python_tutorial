import json
import camelcase
import mymodule

x = mymodule.greeting("Jonathan")
print(len(x))

b = "Hello, World!"
print(b[2:4])

i = 1
while i < 6:
    print(i)
    i += 1
cars = ["Ford", "Volvo", "BMW"]
cars.sort()
print(cars[-1])


def x(a, b): return a * b


b = x(1, 2)
print(b)

print(x(5, 6))
x = "test"
c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))


class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Test("Dan", 3)

print p1.name

x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])

thistuple = ("apple", "banana", "cherry")
for val in thistuple:
    print(val)
