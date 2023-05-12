import copy

def traced_prop_name(p):
    return str(p.name)+'('+p.ti+', '+p.tf+')_{'+p.left_indices.c+','+p.right_indices.c+'}'

def has_only_epsilons(commuting):
    only_epsilons = True 
    for elem in commuting:
        if elem.name!="\\epsilon":
            only_epsilons=False 
    return only_epsilons
