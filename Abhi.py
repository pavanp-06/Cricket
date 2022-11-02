#Cricket
import csv
import random
T1=input("Enter the name of the first team")
T2=input("Enter the name of the second team")
q=int(input("Enter the no. of players in each team"))
t1=[]
t2=[]
print("Enter the player in",T1, "Team") 
for i in range(q):
    K=input("Enter the name of the playerEnter the suffix of (C) and (WK) for captain and wicket-keeper respectively")
    t1.append(K)
for i in range(q):
    L=input("Enter the name of the playerEnter the suffix of (C) and (WK) for captain and wicket-keeper respectively")
    t2.append(L)
x=random.choices([T1,T2])
print("Toss won by",x)
ov = int(input("Enter the number of overs: "))
'''Y = []
for i in range(ov):
    l=[]
    for j in range(6):
        print("Enter O-1run,T=2run,H=3run,F=a four,s=a six")
        m=input("Enter the run scored in the ",j,"ball")
        l.append(m)
    Y.append(l) 
print(Y)'''''''''
with open("T1bsc.csv","r",newline="")as f:
    p1=input("Enter the name of the opening player")
    p2=input("Enter the non-strike batsmen")
    if p1 in t1 and p2 in t1:
        pass
    p1s=0
    p2s=0
    p1b=0
    p2b=0
    p14=0
    p24=0
    p16=0
    p26=0
    for i in range(ov*6):
        print("Enter O-1run,T=2run,H=3run,F=a four,s=a six,w=wicket")
        o=input(i+1,"ball")
