import json
from termcolor import colored
import colorama
colorama.init()

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def toString(self):
        output = {}
        output['val'] = self.val
        if not self.next:
            output['next'] = 'None'
        else:
            output['next'] = self.next.val
        strOutput = json.dumps(output)
        return strOutput

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def toString(self):
        output = {}
        output['val'] = self.val
        if not self.left:
            output['left'] = 'None'
        else:
            output['left'] = self.left.val
        if not self.right:
            output['right'] = 'None'
        else:
            output['right'] = self.right.val
        strOutput = json.dumps(output)
        return strOutput

def initList():
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)
    return root

def initTree():
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(5)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(6)
    '''
            3
    1               5
        2       4      6
    '''
    return root

def o(i):
    prefix = colored('~~~###output', 'red')
    extraGreen = colored('___', 'green')
    extraYellow = colored('___', 'yellow')
    word = colored(str(i), 'yellow')
    affix = colored('output###~~~', 'red')
    print('\n' + prefix + extraYellow + extraGreen + word + extraGreen + extraYellow + affix + '\n')

def div(i):
    prefix = colored('### ', 'red')
    word = colored(str(i), 'yellow')
    affix = colored(' ###', 'red')
    print('\n' + prefix + word + affix + '\n')

def p(i):
    prefix = colored('### ', 'red')
    word = colored(str(i), 'yellow')
    affix = colored(' ### ', 'red')
    print(prefix + word + affix)

def d(dictionary):
    print(json.dumps(dictionary, indent=4))

def prefixer(prefix, affix):
    output = colored(prefix + ':', 'red') + ' ' + affix
    print(output)
    return(output)

def data(varName='', varContent='', codeContent=''):
    varName = colored(str(varName), 'cyan')

    varContent = colored(str(varContent), 'yellow')

    codeContent = colored(str(codeContent), 'grey')

    output = varName + ' = ' + varContent + ' (' + codeContent + ')'

    return(prefixer('DataPrint', output))

def trace(varName='', varIndex='', varContent='', pathContentStart='', pathContentEnd=''):
    varName = colored(str(varName), 'cyan')

    if not varIndex:
        varIndex = colored(str('None'), 'yellow')
    else:
        varIndex = colored(str(varIndex), 'yellow')
        
    if not varContent:
        varContent = colored(str('None'), 'yellow')
    else:
        varContent = colored(str(varContent), 'yellow')

    if not pathContentStart == '':
        pathContentStart = '(' + colored(str(pathContentStart), 'grey') + ') '
    if not pathContentEnd == '':
        pathContentEnd = ' (' + colored(str(pathContentEnd), 'grey') + ')'

    output = varName + ' = ' + pathContentStart + '[' + str(varIndex) + '] = ' + str(varContent) + pathContentEnd

    traceStart = colored('### Trace', 'red', 'on_red')
    traceEnd = colored('Trace ###', 'red', 'on_red')
    output = '\n' + traceStart + ' ' + output + ' ' + traceEnd
    print(output)
    return(output)
