from termcolor import colored
import colorama
colorama.init()

def b(i):
    prefix = colored('### ', 'red')
    word = colored(str(i), 'yellow')
    afrix = colored(' ###', 'red')
    print('\n' + prefix + word + afrix)

def bEnd(i):
    prefix = colored('### ', 'red')
    word = colored(str(i), 'yellow')
    afrix = colored(' ###', 'red')
    print(prefix + word + afrix)

def data(var, varName='', action=''):
    varContent = colored(str(var), 'yellow')
    varColored = colored(str(varName), 'cyan')
    actionName = colored(str(action), 'cyan')
    output = varColored + ' = ' + actionName + ': ' + varContent

    dataName = colored('data:', 'red')
    output = dataName + ' ' + output
    print(output)
    return(output)

def ds(var, varName=''):
    varContent = colored(str(var), 'yellow')
    varType = colored(str(type(var)), 'white')
    varColored = colored(varName, 'cyan')
    output = varColored + ': ' + varType + ': ' + varContent

    dataName = colored('data-struct:', 'red')
    output = dataName + ' ' + output
    print(output)
    return(output)

def pivot(var, varName=''):
    varContent = colored(str(var), 'yellow')
    varType = colored(str(type(var)), 'white')
    varColored = colored(varName, 'cyan')
    # output = varColored + ': ' + varType + ': ' + varContent
    output = varColored + ': ' + varContent

    dataName = colored('pivot:', 'red', 'on_red')
    output = '\n' + dataName + ' ' + output
    print(output)
    return(output)

def pivotEnd(var, varName=''):
    varContent = colored(str(var), 'yellow')
    varType = colored(str(type(var)), 'white')
    varColored = colored(varName, 'cyan')
    # output = varColored + ': ' + varType + ': ' + varContent
    output = varColored + ': ' + varContent

    dataName = colored('pivotEnd:', 'red', 'on_red')
    output = dataName + ' ' + output
    print(output)
    return(output)
