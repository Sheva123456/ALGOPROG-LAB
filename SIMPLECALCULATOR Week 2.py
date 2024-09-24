num1 = input('First number:')
def main(): 
    num2 = input('Second number')
    task = input('What do you wish to do (ADD/MIN/DIV/MUL):')
    if task.upper() == 'ADD':
        output = float(num1)+float(num2)
        print(output) 
    elif task.upper() == 'MIN' :
        output = float(num1) - float(num2)
        print(output)
    elif task.upper() == 'DIV':
        output = float(num1) / float(num2) 
        print(output)
    elif task.upper() == 'MUL':
        output = float(num1)*float(num2)
        print(output)
    else :
        print('Type properly') 
    
    Repeat = input('Would you like to do another operation?(Y/N)').upper()
    if Repeat == 'Y':
        output= num1 
        main()
    else:
        print('bye')
main()
