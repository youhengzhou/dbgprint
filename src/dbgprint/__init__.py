import collections
import json
from termcolor import colored, cprint
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
    def toDict(self):
        output = {}
        output['val'] = self.val
        if not self.next:
            output['next'] = 'None'
        else:
            output['next'] = self.next.val
        return output

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
    def toDict(self):
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
        return output

def printList(root, option=''):
    if not root:
        return None
    if option == 0:
        p(root.val)
    if option == 1:
        p(root.toString())
    if option == 2:
        d(root.toDict())
    printList(root.next,option)

def bfs(root, option=''):
    line = collections.deque()
    line.append(root)

    levelOfList = []
    levelOfListDetailed = []
    levelOfDictLevel = 0
    levelOfDict = {}
    while True: # main routine, run until line is blank
        if not line:
            return levelOfList, levelOfDict, levelOfListDetailed

        i = 0 # sr1, run until level end is hit
        levelList = []
        levelListDetailed = []
        levelDictItem = 0
        levelDict = {}
        levelEnd = len(line) 
        while True:
            if i >= levelEnd:
                break
            
            node = line.popleft()
            if node:
                nodeLeft = ''
                nodeRight = ''
                if node.left:
                    nodeLeft = str(node.left.val)
                if node.right:
                    nodeRight = str(node.right.val)

                levelList.append(node.val)
                levelListDetailed.append('[' + nodeLeft + '-(' + str(node.val) + ')-' + nodeRight + ']')
                levelDict[levelDictItem] = node.toDict()
                line.append(node.left)
                line.append(node.right)
                
            i += 1
            levelDictItem += 1

        if levelList:
            if option == 0:
                p(levelList)
            if option == 1:
                d(levelDict)
            if option == 2:
                p(levelListDetailed)
            levelOfList.append(levelList)
            levelOfListDetailed.append(levelListDetailed)
            levelOfDict[levelOfDictLevel] = levelDict
            levelOfDictLevel += 1

index = [0]
dfsOutputList = []
dfsOutputDict = {}
def dfs(root, option=''):
    if not root:
        return None
    
    # if option == 0:
    #     trace('Node', index[0], root.toString())
    # if option == 1:
    #     trace('Node', index[0], root.toDict())

    trace('Node', index[0], root.toString())
    index[0] += 1

    dfsOutputList.append(root.toString())
    dfsOutputDict[index[0]] = root.toDict()

    # mr = dfs(root.left,option)
    # sr1 = dfs(root.right,option)

    mr = dfs(root.left)
    sr1 = dfs(root.right)

    return dfsOutputList, dfsOutputDict

def initList(input=''):
    if input == '':
        root = ListNode(1)
        root.next = ListNode(2)
        root.next.next = ListNode(3)
        root.next.next.next = ListNode(4)
        root.next.next.next.next = ListNode(5)
        return root

    root = ListNode(input[0])
    pointer = root
    for i in range(1,len(input)):
        pointer.next = ListNode(input[i])
        pointer = pointer.next
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
    #prefix = colored('### ', 'red')
    #word = colored(str(i), 'yellow')
    #affix = colored(' ### ', 'red')
    #print(prefix + word + affix)
    cprint(str(i), 'yellow')

def d(dictionary):
    cprint(json.dumps(dictionary, indent=4), 'yellow')

def prefixer(prefix, affix):
    output = colored(prefix + ':', 'red') + ' ' + affix
    print(output)
    return(output)

def data(varName='', varContent='', note=''):
    varName = colored(str(varName), 'cyan')

    varContent = colored(str(varContent), 'yellow')

    if not note == '':
        note = ' (' + colored(str(note), 'grey') + ')'

    output = varName + ' = ' + varContent + note
    return(prefixer('DataPrint', output))

def trace(varName='', varIndex='', varContent='', pathStart='', pathEnd=''):
    varName = colored(str(varName), 'cyan')

    if varIndex == '':
        varIndex = colored(str('None'), 'yellow')
    else:
        varIndex = colored(str(varIndex), 'yellow')
        
    if varContent == '':
        varContent = colored(str('None'), 'yellow')
    else:
        varContent = colored(str(varContent), 'yellow')

    if not pathStart == '':
        pathStart = '(' + colored(str(pathStart), 'grey') + ') '
    if not pathEnd == '':
        pathEnd = ' (' + colored(str(pathEnd), 'grey') + ')'

    output = varName + ' = ' + pathStart + str(varIndex) + ' = ' + str(varContent) + pathEnd

    traceStart = colored('### Trace:', 'red', 'on_red')
    traceEnd = colored('Trace ###', 'red', 'on_red')
    output = '\n' + traceStart + ' ' + output + ' ' + traceEnd
    print(output)
    return(output)
