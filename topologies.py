# get the time order of each diagram, 
# this will let us determing the topology.
def diagram_time_order(total_diags,log=False):
    diagrams = {}

    for i,d in enumerate(total_diags):
        top = []
        d_str='d_' + str(i) + ':  '
        for p in d.props:
            d_str+=p.tf + '->' + p.ti + '   '
            top.append([p.tf.split('_')[1],p.ti.split('_')[1]])
        diagrams[i]=top
        if(log):
            print(d_str)
    return diagrams

import WickContractions
from WickContractions.wick.utilities import permutations

def swap(list, i, j):
    list[i], list[j] = list[j], list[i]
    return list

def cyclic_permutations(list):
    return [[list[i-j] for i in range(len(list))] for j in range(len(list))]

#I kind of forget what this does...
def connect_times(topList):
    for idx,d in topList.items():
        for p in range(len(d)):
            if d[p][1] != d[(p+1)%len(d)][0]:
                for pp in range(p,len(d)):
                    if d[p][1] == d[pp][0]:
                        swap(d,(p+1)%len(d),pp)

def name_topologies(topList):
    for idx,d in topList.items():
        for label,top in refTopologies.items():
            if d in permutations(top):
                topList[idx]=label







# ref topologies from Dr.Lee's notes.
refTopologies={}
refTopologies['A']=[['1','0'],['0','2'],['2','3'],['3','1']]
refTopologies['A-bwd']=[['0','1'],['1','3'],['3','2'],['2','0']]
refTopologies['B']=[['1','0'],['0','3'],['3','2'],['2','1']]
refTopologies['B-bwd']=[['0','1'],['1','2'],['2','3'],['3','0']]
refTopologies['C']=[['2','0'],['0','3'],['3','1'],['1','2']]
refTopologies['C-bwd']=[['0','2'],['2','1'],['1','3'],['3','0']]
refTopologies['D']=[['0','3'],['3','0'],['2','1'],['1','2']]
refTopologies['El']=[['2','2'],['3','1'],['1','0'],['0','3']]
refTopologies['El-bwd']=[['2','2'],['1','3'],['3','0'],['0','1']]
refTopologies['Er']=[['1','1'],['3','2'],['2','0'],['0','3']]
refTopologies['Er-bwd']=[['1','1'],['2','3'],['3','0'],['0','2']]
refTopologies['F']=[['0','3'],['3','0'],['1','1'],['2','2']]