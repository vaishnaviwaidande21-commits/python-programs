stud = {
    101:{
        "name":"John",
        "age":18,
        "sub":("python","java","mern"),
        "marks":[90,89,78] },

    102:
    {
        "name":"Alice",
        "age":20,
        "sub":("python","java","mern"),
        "marks":[89,75,95]
    },

    103:
    {
        "name":"Max",
        "age":23,
        "sub":("python","java","mern"),
        "marks":[98,82,68]
    },

    104:
    {
        "name":"Jennie",
        "age":19,
        "sub":("python","java","mern"),
        "marks":[67,100,94]
    }
}

#1]
print("rollno \t name \t total marks \t percentage")
for k,v in stud.items():
    total=sum(v["marks"])
    print(f"{k}\t {v['name']}\t {total} ")

#2]
l1=[]
print("\nTopper Student :- ")
for k,v in stud.items():
    for v1 in v.values():
        per=(total/300)*100
        l1.append(per)
        top=(max(l1))
print(f"{k} \t {v['name']} \t {top}")

#3]
max_marks=0

for v in stud.values():
    if(v['marks'][0]>max_marks):
        max_marks=v['marks'][0]
        name = v['name']
print("\n highest marks in python = ",max_marks)
print("name of student having higest marks = ",name)

#4]
print("\nstudents having age > 19:- ")
for v in stud.values():
    if(v['age']>19):
        print(f"{v['name']} \t {v['age']}")

#5]
print("\nstudents having marks >70 ad <90 in mern :- ")
for v in stud.values():
    if(v['marks'][2]>70 and v['marks'][2]<90):
        print(f" {v['name']} \t {v['marks'][2]}")
