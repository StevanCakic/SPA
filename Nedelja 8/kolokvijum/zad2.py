def append_to_file(list_of_students):
    with open("studenti.txt","a") as file:
        for student in list_of_students:
            line = ""
            line = line + student["ime"] + "," + student["prezime"]+ "," + str(student["godina"]) + ","+str(student["prosjek"])
            file.write(line + "\n")

append_to_file([{"ime": "Marko", "prezime":"Markovic", "godina": 2, "prosjek": 8.6 },   {"ime": "Boris", "prezime":"Boricic", "godina": 3, "prosjek": 7.9 },     {"ime": "Novak", "prezime": "Novovic",  "godina": 3, "prosjek": 6.9 }])
append_to_file([{"ime": "Marko", "prezime": "Markovic", "godina": 3, "prosjek": 7}, {"ime": "Janko", "prezime": "Jankovic", "godina":2, "prosjek": 6.23},{"ime": "Marija", "prezime": "Jovanovic", "godina":1, "prosjek": 7.75}])

def get_students_with_greater_grade(year, grade):
    if grade == "A":
        grade = 9.5
    if grade == "B":
        grade = 8.5
    if grade == "C":
        grade = 7.5
    if grade == "D":
        grade = 6.5
    if grade == "E":
        grade = 6
    lista_dict=[]

    with open("studenti.txt","r") as file:
        data = file.read().split("\n")
        for student in data:
            podaci = student.split(",")
            if len(podaci) == 4:
                if podaci[2] == str(year) and float(podaci[3])>= grade:
                    st_dict = {"ime": podaci[0], "prezime": podaci[1], "godina":podaci[2], "prosjek": podaci[3]}
                    lista_dict.append(st_dict)
    return lista_dict

print(get_students_with_greater_grade(3,"C"))
print(get_students_with_greater_grade(2,"E"))
