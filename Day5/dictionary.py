student={
    "name":"Akanksha",
    "age":23,
    "course":"python"
}

# print(student)
print(student["name"])
student["college"]="ABC College"
# print(student)
# student.pop("age")
# print(student)
print(student.keys())
print(student.values())
print(student.items())
print(student.get("course"))
student.update({"name":"soni"})
print(student)



