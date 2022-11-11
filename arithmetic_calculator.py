lst = ['44 + 815', '909 - 2', '45 + 43', '123 + 49',
       '888 + 40', '653 + 87']

def arithmetic_arranger(lst, displayMode = False):
    
    if len(lst) > 5:
        return 'Error: Too many problems.'
    
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''

    for problem in lst:
        operator = problem.split(" ")[1]
        
        try:
            if operator != '+' and operator != '-':
                raise BaseException
        except:
            return "Error: Operator must be '+' or '-'."

        
        fnum = problem.split(" ")[0]
        snum = problem.split(" ")[2]
        space = max(len(fnum), len(snum))
        
        try:
            if len(fnum)>4 or len(snum)>4:
                raise BaseException
        except:
            return 'Error: Numbers cannot be more than four digits.'
        
        try:
            fint = int(fnum)
        except:
            return 'Error: Numbers must only contain digits.'

            
        try:
            sint = int(snum)
        except:
            return 'Error: Numbers must only contain digits.'


        
        line1 += fnum.rjust(2+space) + '    '
        line2 += operator + snum.rjust(1+space) + '    '
        line3 += '-'*(space+2)+'    '
        

        if operator == '+':
            sum1 = int(fnum)+int(snum)
        else:
            sum1 = int(fnum)-int(snum)
            
        line4 += str(sum1).rjust(2+space) + '    '
        

    if displayMode:
        return line1.rstrip()+'\n'+line2.rstrip()+'\n'+line3.rstrip()+'\n'+line4.rstrip()
    else: 
        return line1.rstrip()+'\n'+line2.rstrip()+'\n'+line3.rstrip()

print(arithmetic_arranger(lst, True))
