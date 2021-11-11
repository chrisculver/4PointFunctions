def latexStr(gamma):
    tmp=gamma.name.split('_')
    if(tmp[0]=='\\gamma'):
        return tmp[0] + '_{' + tmp[1] + '_{' + gamma.indices[0] + gamma.indices[1] + '}}'
    else:
        return str(tmp)
  
def platexStr(p):
    return p.name + '(' + p.ti.replace('t','x') + p.ti + '\mid ' + p.tf.replace('t','x') + p.tf + ')' + '_{\\substack{' + p.left_indices.s + '\\\\' + p.left_indices.c + '}' +  '\\substack{' + p.right_indices.s + '\\\\' + p.right_indices.c + '}}'
    

def print_diagrams(total_diags):
    print('\\beqs')
    for i,d in enumerate(total_diags):
        #if(i==1 or i==6):
        tmp='d_{'+str(i)+'}='+str(d.coef) + ' '
        for p in d.props:
            tmp+=platexStr(p)
        for c in d.commuting:
            tmp+=latexStr(c)
        print(tmp+'\\\\')
    print('\\eeqs')
    
    
    
def print_diagrams_labelled(diags,sortd):
    print('\\beqs')
    newI=0
    for i,label in sortd.items():
        #if(i==1 or i==6):
        tmp='d_{'+str(i)+'}^{\\text{('+label+')}}='+str(diags[i].coef) + ' '
        for p in diags[i].props:
            tmp+=platexStr(p)
        for c in diags[i].commuting:
            tmp+=latexStr(c)
        print(tmp+'\\\\')
        newI+=1
    print('\\eeqs')