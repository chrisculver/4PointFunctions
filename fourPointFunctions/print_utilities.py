def latexStr(gamma):
    tmp=gamma.name.split('_')
    if(tmp[0]=='\\gamma'):
        return tmp[0] + '_{' + tmp[1] + '_{' + gamma.indices[0] + gamma.indices[1] + '}}'
    else:
        return str(tmp)

# prop latex string
def platexStr(p):
    return p.name + '(' + p.ti.replace('t','x') + p.ti + '\mid ' + p.tf.replace('t','x') + p.tf + ')' + '_{\\substack{' + p.left_indices.s + '\\\\' + p.left_indices.c + '}' +  '\\substack{' + p.right_indices.s + '\\\\' + p.right_indices.c + '}}'
    
def proplatexStrSpaceTime(p):
    return p.name + '(' + p.ti.replace('t','x') + ',' + p.tf.replace('t','x') + ')' + '_{\\substack{' + p.left_indices.s + '\\\\' + p.left_indices.c + '}' +  '\\substack{' + p.right_indices.s + '\\\\' + p.right_indices.c + '}}'
    

def proton_diagram_str(d):
    s=str(d.coef)+' '
    for c in d.commuting:
        s+=str(c)
    for p in d.props:
        s+=proplatexStrSpaceTime(p)

    s+='\\\\'

    return s

def proton_diagram_str_no_epsilon(d):
    s=str(d.coef)+' '
    for c in d.commuting:
        if c.name!="\\epsilon":
            s+=str(c)
    for p in d.props:
        s+=proplatexStrSpaceTime(p)

    s+='\\\\'

    return s




def diagram_as_latex_str(d,i):
    #if(i==1 or i==6):
    s=''
    tmp='d_{'+str(i)+'}='+str(d.coef) + ' '
    for p in d.props:
        tmp+=platexStr(p)
    for c in d.commuting:
        tmp+=latexStr(c)
    s+=tmp+'\\\\'
    return s


def labelled_diagram_as_latex_str(d,i,label):
    s=''
    tmp='d_{'+str(i)+'}^{\\text{('+label+')}}='+str(d.coef) + ' '
    for p in d.props:
        tmp+=platexStr(p)
    for c in d.commuting:
        tmp+=latexStr(c)
    s+=tmp+'\\\\'
    return s
    
    
    
def print_diagrams_labelled(diags,sortd):
    print('\\beqs')
    for i,label in sortd.items():
        #if(i==1 or i==6):
        tmp='d_{'+str(i)+'}^{\\text{('+label+')}}='+str(diags[i].coef) + ' '
        for p in diags[i].props:
            tmp+=platexStr(p)
        for c in diags[i].commuting:
            tmp+=latexStr(c)
        print(tmp+'\\\\')
    print('\\eeqs')
    
    
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