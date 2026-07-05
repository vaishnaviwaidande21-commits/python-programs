players=((1,"Virat",98),
         (2,"Rohit",100),
         (3,"Vaibhav",99),
         (4,"Mahi",101))


max_score=players[0][2]
name = players[0][1]

for i in players:
    if(i[2]>max_score):
        max_score=i[2]
        name=i[1]
print("Maximun score = ",max_score)
print(" Player name = ",name)


total=0
for i in players:
    total = total + i[2]
print("\ntotal score = ",total)
