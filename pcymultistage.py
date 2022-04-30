import math
import os
import datetime
import numpy

fname = "retail.txt"
#input: threshold value, dataset
#output: find frequent itemsets

chunks = [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
threshold = [1, 5, 10]
exe_time = []
#==========================================
def pcyhash (tval, val):
    val = int(88162 * (val/100))
    support = int(val * (tval/100))
    singleton = {}
    pairs = set()
    pcyhash = {}
    hash2 = {}
    finalpairs = {}
    k = primefinal(val)
    k_new = primefinal(k+10)
    start = datetime.datetime.now()

    def hashfun (i, j):
        return i+j % k

    def hashfun2 (i, j):
        return i+j % k_new

    with open (fname, 'r') as f:
        for i in range(0, val):
            line = f.readline()
            line = list(map(int, line.split()))
            
            for j in line:
                if j not in singleton:
                    singleton[j] = 1
                else:
                    singleton[j] = singleton[j]+1
            
            for i in range(0, len(line)):
                for j in range(i+1, len(line)):
                    pairs.add((line[i], line[j])) 
                    hashkey = hashfun(line[i], line[j])
                    
                    if hashkey not in pcyhash:
                        pcyhash[hashkey] = 1
                    else:
                        pcyhash[hashkey] = pcyhash[hashkey]+1
        
        for key, value in pcyhash.copy().items():
            if value < support:
                pcyhash[key] = 0 #not frequent
            else:
                pcyhash[key] = 1 #frequent bucket

    '''
        creating a new dict containing bucket frequency
        figure out a new k value

        only store the pairs that meets the condition above
        do bitmap of hash2
        remove pairs that are not frequent in hash1 and hash2 (the value of the pair is 0)
    '''

    with open (fname, 'r') as f:
        for i in range(0, val):
            line = f.readline()
            line = list(map(int, line.split()))

            for i in range(0, len(line)):
                for j in range(i+1, len(line)):
                    hashkey = hashfun2(line[i], line[j])
                    old_hashkey = hashfun(line[i], line[j])

                    if singleton[line[i]] >= support and singleton[line[j]] >= support and pcyhash[old_hashkey] == 1:
                        if hashkey not in hash2:
                            hash2[hashkey] = 1
                        else:
                            hash2[hashkey] = hash2[hashkey]+1
                                
        for key, value in hash2.copy().items():
            if value < support:
                hash2[key] = 0 #not frequent
            else:
                hash2[key] = 1 #frequent bucket

        for pair in pairs.copy():
            hash1_key = hashfun(pair[0], pair[1])
            hash2_key = hashfun2(pair[0], pair[1])

            if pcyhash.get(hash1_key) != 1 or hash2.get(hash2_key) != 1 or singleton[pair[0]] < support or singleton[pair[1]] < support:
                pairs.remove(pair)

    with open (fname, 'r') as f:
        for i in range(0, val):
            line = f.readline()
            line = set(map(int, line.split()))

            for pair in pairs:
                if pair[0] in line and pair[1] in line:
                    if pair not in finalpairs:
                        finalpairs[pair] = 1
                    else:
                        finalpairs[pair] = finalpairs[pair]+1
    
    for key, value in finalpairs.copy().items():
        if value < support:
            finalpairs.pop(key)
    
    print(len(finalpairs))

    end = datetime.datetime.now()
    exe = (end-start).total_seconds() * 1000

    return exe
#==========================================
def prime(n): 
	isprime = True 
	if n<2: 
		isprime = False 
	else: 
		for i in range(2,n): 
			if n%i==0: 
				isprime = False 
				break 
	return isprime 
#==========================================
def primefinal(n):
    flag, i = True, 1 
    
    if prime(n): 
        num = n
    else: 
        while flag: 
            if prime(n+i) and prime(n-i): 
                num = n+i 
                flag = False 
            elif prime(n-i): 
                num = n-i 
                flag = False 
            elif prime(n+i): 
                num = n+i 
                flag = False 
            i += 1 
    
    return num
#==========================================
# pcyhash (1,1)