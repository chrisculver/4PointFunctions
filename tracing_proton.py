import copy

def traced_prop_name(p):
    return str(p.name)+'('+p.ti+', '+p.tf+')_{'+p.left_indices.c+','+p.right_indices.c+'}'


def diagram_as_trace_string(d):
    diag=copy.deepcopy(d)

    s='\\text{tr}\\left['

    s+=traced_prop_name(diag.props[0])
    print(s)

    lastProp=copy.deepcopy(diag.props[0])
    startSpin=lastProp.left_indices.s
    lastSpin=lastProp.right_indices.s

    diag.props.remove(diag.props[0])

    more_tracing=True 

    while more_tracing:
        sStart=copy.deepcopy(s)

        for com in diag.commuting:
            if com.indices[0] == lastSpin:
                lastSpin=com.indices[1]
                s+=com.name
                diag.commuting.remove(com)
        
        for p in diag.props:
            if(p.left_indices.s == lastSpin):
                s+=traced_prop_name(p)
                lastSpin=p.right_indices.s
                diag.props.remove(p)

        if diag.props==[] and diag.commuting==[]:
            more_tracing=False
        
        if lastSpin==startSpin:
            s+='\\right]'
            s+='\\text{tr}\\left['
            s+=traced_prop_name(diag.props[0])

            lastProp=copy.deepcopy(diag.props[0])
            startSpin=lastProp.left_indices.s
            lastSpin=lastProp.right_indices.s

            diag.props.remove(diag.props[0])

        if s==sStart:
            print('\n')
            for p in diag.props:
                print(p)
            for c in diag.commuting:
                print(c)
            print('lastSpin={}'.format(lastSpin))
            print('s={}'.format(s))
            raise ValueError('s didnt change after iterating over all props and commuting objs')

    return s+'\\right]'