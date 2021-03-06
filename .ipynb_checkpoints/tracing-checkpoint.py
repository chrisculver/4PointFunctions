import copy

def traced_prop_name(p):
    return str(p.name)+'('+p.ti+', '+p.tf+')'

def diagram_as_trace_string(d):
    tst=copy.deepcopy(d)

    s='\\text{tr}\\left['

    # Start with the first prop.
    s+=traced_prop_name(tst.props[0])
    
    lastProp=copy.deepcopy(tst.props[0])
    startSpin=lastProp.left_indices.s
    startColor=lastProp.left_indices.c
    lastSpin=lastProp.right_indices.s
    lastColor=lastProp.right_indices.c

    tst.props.remove(tst.props[0])

    more_tracing=True

    while more_tracing:
        sStart=copy.deepcopy(s)
    
        for com in tst.commuting:
            if com.indices[0] == lastSpin:
                lastSpin=com.indices[1]
                s+=com.name
                tst.commuting.remove(com)
            if com.indices[0] == lastColor:
                lastColor=com.indices[1]
                s+=com.name
                tst.commuting.remove(com)

        for p in tst.props:
            if (p.left_indices.s == lastSpin) and (p.left_indices.c == lastColor):
                s+=traced_prop_name(p)
                lastSpin=p.right_indices.s
                lastColor=p.right_indices.c
                tst.props.remove(p)
            
            #elif p.left_indices.s == lastSpin:
            #    s+=traced_prop_name(p)
            #    lastSpin=p.right_indices.s
        
        if tst.props==[] and tst.commuting==[]:
            more_tracing=False
    
        if lastSpin==startSpin and lastColor==startColor and len(tst.props)>0:
            s+='\\right]'
            s+='\\text{tr}\\left['
            s+=traced_prop_name(tst.props[0])
    
            lastProp=copy.deepcopy(tst.props[0])
            startSpin=lastProp.left_indices.s
            startColor=lastProp.left_indices.c
            lastSpin=lastProp.right_indices.s
            lastColor=lastProp.right_indices.c

            tst.props.remove(tst.props[0])
    
        if s==sStart:
            print('\n')
            for p in tst.props:
                print(p)
            for c in tst.commuting:
                print(c)
            print('lastSpin={}, lastColor={}'.format(lastSpin, lastColor))
            print('s={}'.format(s))
            raise ValueError('s didnt change after iterating over all props and commuting objs')
    return s+'\\right]'