def combine_diagrams(total):
    for i in range(len(total)-1,-1,-1):
        for j in range(len(total)-1,-1,-1):
            if(i!=j):
                if((total[i].commuting==total[j].commuting) and (total[i].props==total[j].props)):
                #if(total[i]==total[j]):
                    total[i].coef+=total[j].coef
                    total.pop(j)
                    break
                
    for i in range(len(total)-1,-1,-1):
        if(total[i].coef==0):
            total.pop(i)