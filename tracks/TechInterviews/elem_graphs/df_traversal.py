visited = []

def traverse(tree, i):
    global visited
    if i < len(tree):
        if visited[i] == False:
            visited[i] = True
            if tree[i] != "*":
                return str(traverse(tree,(2*i) + 1)) + str(tree[i]) + str(traverse(tree, (2*i) + 2))
    return ""
    
def depth_first(tree):
    global visited 
    visited = len(tree)*[False]
    for i in xrange(len(tree)):
        if visited[i] == False:
            visited[i] = True
            if (2 * i)+1 < len(tree):
                if (2*i) + 2 < len(tree):
                    print traverse(tree, (2 * i) + 1) + tree[i] + traverse(tree, (2 * i) + 2)
                else:
                    print traverse(tree, (2 * i) + 1) + tree[i]
            else: print tree[i]
