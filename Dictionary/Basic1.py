stud={
    "name":"vaishnavi",
    "age": 17,
    "branch":"CO",
    "marks":[10,20,30,40]
}
U
print(stud.keys())
print(stud.values())
print(stud.items())

for key,values in stud.items():
    print(key,values)


for values in stud.values():
    if type(values)==list:
        for i in values:
            print(i)
        continue
    print(values)
