# What is A? 
# What is B? 
# What is C? 
# What is D? 
# What is E F G?
# What is the vertices? (Nodes) 

# nodes = ['loyal', 'disloyal', 'interested', 'disinterested', 'loyal-disinterested', 'disloyal-interested', 'loyal-interested', 'disployal-disinterested']

vertices = [a,b,c,d,e,f,g]
edges = [
    ('A', 'B', 15),
    ('B', 'A', 9),
    ('B', 'C', 13),
    ('D', 'C', 5),
    ('D', 'E', 12),
    ('E', 'F', 45),
    ('F', 'G', 10),
    ('E', 'G', 30),
    ('C', 'A', 7),
]

def DFS(start_node, key):
    next_nodes.push(start_node)
    seen_nodes.add(start_node)
    while not next_nodes.empty < next_nodes.pop() if node.key == key:
    return node
for n in node.connected_nodes:
    if not n in seen_nodes next_nodes.push(n) seen_nodes.add(n):
return None
DFS(edges, vertices)
