def filterSpace(string):
    string = string.replace(" ","")
    return(string)
    
def newickParser(newick):
    newick = filterSpace(newick)
    nodes = []
    start = 0
    end = 0
    for i in range(len(newick)):
        if newick[i] == ")":
            end = i
            c= i-1
            closing_parenthesis = 1
            opening_parenthesis = 0
            while c >= 0:
                if newick[c] == "(":
                    opening_parenthesis += 1
                if newick[c] == ")":
                    closing_parenthesis += 1
                if opening_parenthesis == closing_parenthesis:
                    start = c
                    node = newick[start:end+1]
                    nodes.append(node)
                    break
                else:
                    c -= 1
    return(nodes)

def initializeDic(dic):        
    keys = list(dic.keys())
    values = list(dic.values())
    new_values = []
    for value in values:
        if value == 'A' or value == 'a':
            new_value = [0,99999999999, 99999999999, 99999999999]
        elif value == 'C' or value == 'c':
            new_value = [99999999999, 0, 99999999999, 99999999999]
        elif value == 'G' or value == 'g':
            new_value = [99999999999, 99999999999, 0, 99999999999]
        elif value == 'T' or value == 't':
            new_value = [99999999999, 99999999999, 0] 
        new_values.append(new_value)
    new_dic = dict(zip(keys, new_values))

    return(new_dic)


def matrixSum(a,b):
    new_matrix = []
    for i in range(len(a)):
        new_row = []
        rowA = a[i]
        rowB = b[i]
        for j in range(len(rowA)):
            new_row.append(rowA[j] + rowB[j])
        new_matrix.append(new_row)

    return(new_matrix)
    
def upperNode(a, b, cost_matrix, dicNodes):
    leftVector = dicNodes[a]
    rightVector = dicNodes[b]
    l = len(StepMatrix)
    leftMatrix = [leftVector] * l
    rightMatrix = [rightVector] * l
    leftMatrix = matrixSum(StepMatrix,leftMatrix)
    rightMatrix = matrixSum(StepMatrix,rightMatrix)
    newVector = [min(list(leftMatrix[i])) + min(list(rightMatrix[i])) for i in range(l)]
    
    return(newVector)

def makeTree(dic,tree, matrix):
    nodes = newickParser(tree)
    new_dic = dic.copy()
    for node in nodes:
        new_dic[node] = False
    keys = list(new_dic.keys())
    values = list(new_dic.values())
    count = values.count(False)
    while len(nodes) > 0:
        for i in range(len(values)):
            if values[i] == False:
                for a in keys:
                    for b in keys:
                        ab = "(" + str(a) + "," + str(b) + ")"
                        if keys[i] == ab:
                            if new_dic[a] != False and new_dic[b] != False:
                                new_value = upperNode(a, b, matrix, new_dic)
                                values[i] = new_value
                                new_dic[ab] = new_value
                                nodes.remove(ab)
    
    return(new_dic)


def traceback(dic):
    tags = ['A', 'C', 'G', 'T']
    keys = list(dic.keys())
    values = list(dic.values())
    values = [min(vector) for vector in values]
    lengths = [len(str(key)) for key in keys]
    root_index = lengths.index(max(lengths))
    min_parsimony = values[root_index]
    new_dic = dict(zip(keys, values))

    return((min_parsimony, new_dic))

def sankoff(newickTree, costMatrix, leavesDic):
    leavesDic = initializeDic(leavesDic)
    tree = makeTree(leavesDic,newickTree, costMatrix)
    final_tree = traceback(tree)

    return(final_tree)
