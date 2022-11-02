#Cricket
import csv
T1=input("Enter the name of the first team")
T2=input("Enter the name of the second team")
q=int(input("Enter the no. of players in each team"))
t1=[]
t2=[]
print("Enter the player in",T1"Team")
for i in range(q):
    K=input("Enter the name of the playerEnter the suffix of (C) and (WK) for captain and wicket-keeper respectively")
    t1.append(K)
for i in range(q):
    L=input("Enter the name of the playerEnter the suffix of (C) and (WK) for captain and wicket-keeper respectively")
    t2.append(L)
import random
x=random.choices([T1,T2])
