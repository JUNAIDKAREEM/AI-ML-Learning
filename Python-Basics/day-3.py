# Day 3 - Dictionaries and Tuples

# Dictionary example
student = {
    "name": "AI Student",
    "branch": "AI & ML",
    "year": 2,
    "marks": 85
}

print("Student details:")
print(student)

# Access dictionary values
print("Name:", student["name"])
print("Marks:", student["marks"])

# Update value
student["marks"] = 90
print("Updated marks:", student["marks"])

# Add new key-value
student["college"] = "Engineering College"
print("Updated dictionary:", student)


# Tuple example
subjects = ("Maths", "Python", "Machine Learning")
print("Subjects:", subjects)

# Access tuple
print("First subject:", subjects[0])

# Loop through tuple
print("All subjects:")
for sub in subjects:
    print(sub)

#example:-
marks={"ram":90,"kareem":100,"jack":50,"bob":22}
print(marks)
print(marks.items())
print(marks.values())
marks.update({"harry":65})
print(marks)

