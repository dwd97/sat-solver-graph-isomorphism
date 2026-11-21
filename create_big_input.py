import random

NR_VERTICES = 50

graph1 = []
graph2 = []

for i in range(NR_VERTICES):
    graph1.append(i)
    graph2.append(i)

random.shuffle(graph2)

with open("sample_inputs/big.in", "w") as f:
    NR_EDGES = (NR_VERTICES*(NR_VERTICES - 1)) // 2
    f.write(f"{NR_VERTICES} {NR_EDGES}\n")
    for i in range(0,len(graph1)):
        for j in range(i+1, len(graph1)):
            f.write(f"{graph1[i]} {graph1[j]}\n")

    f.write(f"{NR_VERTICES} {NR_EDGES}\n")
    for i in range(0,len(graph2)):
        for j in range(i+1, len(graph2)):
            f.write(f"{graph2[i]} {graph2[j]}\n")
