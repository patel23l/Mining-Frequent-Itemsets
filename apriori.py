import math
import os
import datetime
import numpy
import matplotlib.pyplot as plt

fname = "retail.txt"
#input: threshold value, dataset
#output: find frequent itemsets

# def graph():
#     plt.plot(chunks, exe_time[:13])
#     plt.title("A-Priori")
#     plt.xlabel('Dataset Size')
#     plt.ylabel('Runtime (ms)')
#     plt.show()

chunks = [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
threshold = [1, 5, 10]
exe_time = []

def apriori (tval, val):
    start = datetime.datetime.now()
    val = int(88000 * (val/100))
    f = open(fname, "r")

    support = int(val * (tval/100))

    lstmap = {}
    
    for i in range(0, val):
        line = f.readline()
        lst = line.split()
        for j in lst:
            if j not in lstmap:
                lstmap[j] = 1
            else:
                lstmap[j] = lstmap[j]+1
    
    for key, value in lstmap.copy().items():
        if value < support:
            lstmap.pop(key)
        
    lstmap1 = set()
    asd = list(lstmap.keys())

    for i in range(0, len(asd)):
        for j in range(i+1, len(asd)):
            x = (asd[i], asd[j])
            lstmap1.add(x)
    pairlst = {}
    
    f = open(fname, "r")
    
    for k in range(0, val):
        line1 = f.readline()
        lst1 = set(line1.split())

        for x, y in lstmap1:
            if x in lst1 and y in lst1:
                if (x, y) not in pairlst:
                    pairlst[(x,y)] = 1
                else:
                    pairlst[(x,y)] = pairlst.get((x,y)) + 1
    for key, value in pairlst.copy().items():
        if value < support:
            pairlst.pop(key)
    
    end = datetime.datetime.now()
    exe = (end-start).total_seconds() * 1000
    print(exe)
    return exe
#==========================================
# for i in threshold:
#     for j in chunks:
#         apriori(i, j)

# for i in chunks: 
#     apriori(1, i)

# graph(0, 12)
# graph(12, 24)
# graph(24, 36)