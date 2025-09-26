student = {"name": "ariana", "age": "19", "grade": "14"}
age = student.get("age")
student.update({"age": "21", "color": "red"})
for key, value in student.items():
    print(key, ":", value)
print(f"student information is {student}")
