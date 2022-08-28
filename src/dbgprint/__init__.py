from termcolor import colored
import colorama
colorama.init()

def div(i):
    prefix = colored('### ', 'red')
    word = colored(str(i), 'yellow')
    affix = colored(' ###', 'red')
    print('\n' + prefix + word + affix)

def prefixer(prefix, affix):
    output = colored(prefix + ':', 'red') + ' ' + affix
    print(output)
    return(output)

def data(var, varName='', action=''):
    varContent = colored(str(var), 'yellow')
    varColored = colored(str(varName), 'cyan')
    actionName = colored(str(action), 'cyan')
    output = varColored + ' = ' + actionName + ': ' + varContent

    return(prefixer('data', output))

def ds(var, varName=''):
    varContent = colored(str(var), 'yellow')
    varType = colored(str(type(var)), 'white')
    varColored = colored(varName, 'cyan')
    output = varColored + ': ' + varType + ': ' + varContent

    return(prefixer('data-struct', output))

def pivot(var, varName=''):
    varContent = colored(str(var), 'yellow')
    varColored = colored(varName, 'cyan')
    output = varColored + ': ' + varContent

    dataName = colored('pivot:', 'red', 'on_red')
    output = '\n' + dataName + ' ' + output
    print(output)
    return(output)

def pivotEnd(var, varName=''):
    varContent = colored(str(var), 'yellow')
    varColored = colored(varName, 'cyan')
    output = varColored + ': ' + varContent

    return(prefixer('pivotEnd', output))
