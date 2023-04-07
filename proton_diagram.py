import WickContractions
import copy

class ProtonDiagram:
    """Container for the commuting objects and propagators that need to be
        computed after wick contractions.  The correlation function is a linear
        combination of diagrams.  Either quarks or propagators could be
        passed to the correlator but not both.
        :param coef: Diagram coefficient
        :param commuting: Commuting objectings
        :param qs: List of quarks to turn into propagators
        :param props: List of propagators (should only be used for testing)
    """

    def __init__(self, diagram):
        self.coef = diagram.coef 
        self.color_objs = [elem for elem in diagram.commuting if elem.name=="\\epsilon"]
        self.spin_objs = [elem for elem in diagram.commuting if elem not in self.color_objs]
        self.props = diagram.props

    def __str__(self):
        """Printer to str
        """
        #ci_str = ''.join([str(c) for c in self.)
        #prop_str = ''.join([str(p) for p in self.props])
        return str(self.coef) + "TODO"

    def __eq__(self, other):
        """Equality comparison
        """
        return (self.coef == other.coef) and (self.objs==other.spin_objs) and (self.color_objs==other.color_objs) and (self.props==other.props)


    def spin_prod_string(self):
        pd0=copy.deepcopy(self)
        spinProd=[pd0.props[0]]
        traces=[]
        startSpin=pd0.props[0].left_indices.s
        startIdx=0
        curSpin=pd0.props[0].right_indices.s
        pd0.props.pop(0)

        more_tracing = True 

        while more_tracing:
            loopSpin=copy.deepcopy(curSpin)

            for gam in pd0.spin_objs:
                if curSpin == gam.indices[0]:
                    spinProd+=[gam]
                    pd0.spin_objs.remove(gam)
                    curSpin=gam.indices[1]
                elif curSpin == gam.indices[1]:
                    gam.name+="^T"
                    spinProd+=[gam]
                    pd0.spin_objs.remove(gam)
                    curSpin=gam.indices[0]

            for prop in pd0.props:
                if prop.left_indices.s == curSpin:
                    spinProd+=[prop]
                    pd0.props.remove(prop)
                    curSpin=prop.right_indices.s 
                elif prop.right_indices.s == curSpin:
                    prop.name+="^T"
                    spinProd+=[prop]
                    pd0.props.remove(prop)
                    curSpin=prop.left_indices.s

            if pd0.props==[] and pd0.spin_objs==[]:
                more_tracing=False
                break 

            if curSpin==startSpin: # trace is completed
                spinProd+=[pd0.props[0]]
                startSpin=pd0.props[0].left_indices.s
                curSpin=pd0.props[0].right_indices.s
                pd0.props.pop(0)
                #TODO add to traces
                traces+=[(startIdx,len(spinProd)-1)]
                startIdx=len(spinProd)-1

            if curSpin==loopSpin: # cur spin chain doesnt end in trace # but what about the trace backwards?

                if pd0.props!=[]:
                    spinProd+=[pd0.props[0]]
                    startSpin=pd0.props[0].left_indices.s
                    curSpin=pd0.props[0].right_indices.s
                    pd0.props.pop(0)
                else:
                    spinProd+=[pd0.spin_objs[0]]
                    startSpin=pd0.spin_objs[0].indices[0]
                    curSpin=pd0.spin_objs[0].indices[1]
                    pd0.spin_objs.pop(0)
                
                # if/else structure added for d30

            
         #   elif curSpin==loopSpin:
        #        print("Found same spin at end of loop, stuck at ",curSpin)
       #         print("  SpinProd=",[str(p) for p in spinProd])
      #          print()
     #           print("  Props=",[str(p) for p in pd0.props])
    #            print()
   #             print("  Spins=",[str(p) for p in pd0.spin_objs])
  #              print()
 #               print("  traces=",traces)
#                raise ValueError("spin didn't change")

            

        tst=str(pd0.coef)
        for elem in pd0.color_objs:
            tst+=str(elem)
        for i,elem in enumerate(spinProd):
            for t in traces:
                if i==t[0]:
                    tst+="\\text{tr}\\left["
                if i==t[1]:
                    tst+="\\right]"
            if type(elem) is WickContractions.corrs.propagator.FullPropagator:
                tst+=str(elem.name)+'('+elem.ti+', '+elem.tf+')_{'+elem.left_indices.c+','+elem.right_indices.c+'}'
            else:
                tst+=str(elem.name+" ")

        return tst