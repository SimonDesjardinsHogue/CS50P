#students = ["Hermione", "Harry", "Ron"]
#houses = ["Gryffindor", "Gryffindor", "Grffindor", "Slytherin"]
#for student in students:
#  prints(students)
#  
# for i in range(len(students)):
#   print(i + 1, students[1])
#
#
# using dict
students = {
  "Hermione": "Gryffindor,
  "Harry": "Gryffindor",
  "Ron": "Gryffindor",
  "Draco": "Slytherin",
}

for student in students:
  print(student, students [student], sep=", ")

  
  # avec list de dict
  
  students = [
    {"name":"Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name":"Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name":"Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name":"Draco", "house": "Slytherin", "patronus": None}
  ]
  
  for student in students:
    print(student["name"], student["house], student["patronus"], sep". ")
