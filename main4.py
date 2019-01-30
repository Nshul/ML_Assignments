import csv
import numpy as np

# Create datatype to read csv
datatype = []
datatype.append(("|U10"))
for i in range(17):
    datatype.append(("|U1"))

zooData = np.genfromtxt('zoodata/zoo.data', delimiter=',', dtype=datatype)
# print(zooData)
# create initial Specification
hypothesis = np.full((7, 17), "phi")

for i in zooData:
    currHypNo = int(i[17])-1
    for idx in range(17):
        if i[idx].item() != hypothesis[currHypNo][idx].item():
            if hypothesis[currHypNo][idx] == "phi":
                hypothesis[currHypNo][idx] = i[idx]
            elif hypothesis[currHypNo][idx].item() == '?':
                # We do nothing
                pass
            else:
                hypothesis[currHypNo][idx] = '?'

print("Mammal:    ",end='')
print(hypothesis[0])
print("Bird:      ",end='')
print(hypothesis[1])
print("Reptile:   ",end='')
print(hypothesis[2])
print("Fish:      ",end='')
print(hypothesis[3])
print("Amphibians:",end='')
print(hypothesis[4])
print("Insect:    ",end='')
print(hypothesis[5])
print("Other:     ",end='')
print(hypothesis[6])