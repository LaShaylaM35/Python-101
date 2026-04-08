name = input("Input your name: ")
age = input("Input your age: ")
height = 1.69
student = False
age = int(age)
person = {
    "name" : name,
    "age" : age
}
print(person)
print (person["name"])
print (person["age"])
print(f"Height:         {height}")
print(f"Student:        {student}")