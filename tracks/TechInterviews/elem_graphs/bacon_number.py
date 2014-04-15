actors = [] ## List of actors with bacon number = bacon_number
adj = dict()
bacon_limit = 0

def get_dict(data):
    d = dict()
    for line in data:
        tokens = line.split(", ")
        if tokens[0] in d:
            d[tokens[0]].append(tokens[1])
        else:
            d[tokens[0]] = [tokens[1]]
        for i in xrange(2,len(tokens)):
            d[tokens[0]].append(tokens[i])
    return d

def traverse(key, cur_bacon):
    global actors
    global bacon_limit
    cur_bacon+=1
    if key in adj.keys():
        if cur_bacon < bacon_limit:
            for i in adj[key]:
                traverse(i,cur_bacon)
        else:
            for i in adj[key]:
                if i not in actors:
                    actors.append(i)

def list_actors(data, bacon_number):
    global adj
    global actors
    adj = get_dict(data)
    global bacon_limit
    bacon_limit = bacon_number
    if bacon_number !=0:
        traverse('Kevin Bacon', 0)
    else:
        print 'Kevin Bacon'
    print "\n".join(x for x in sorted(actors))
