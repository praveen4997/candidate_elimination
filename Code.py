from CL import CandidateElimination as cl
import csv

with open('zoo.csv') as csvFile:
    eg = [tuple(line) for line in csv.reader(csvFile)]

animal_types = ['mammal', 'bird', 'reptilia', 'fish', 'amphibias', 'insect', 'other']
animal_features=['animal name','hair','feathers','eggs','milk','airborne','aquatic','predator','toothed','backbone','breathes','venomous','fins','legs',' tail','domestic','catsize',' type'] 
examples=[]
print("Choose animal type you want to Classify:")
print("\n1.mammal\n2.bird\n3.reptilia\n4.fish\n5.amphibias\n6.insect\n7.other")
inp=input("Enter your option: ")
for row in eg:
    type_index=len(row)-1
    l=list(row)
    if row[type_index] == inp : 
        l[type_index]="Yes"
    else:
        l[type_index]="No"
    examples.append(l)


cl.candidate_elimination(examples)