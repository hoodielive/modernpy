
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

graph = { v: {} for v in vertices }

for start, end, weight in edges:
    graph[start][end] = weight

def connected(graph, start, end):
    if seen is None:
        seen = set()
    if start in seen:
        return False
    send.add(start)
    if end in graph[start]:
        return True
    for neighbor in graph[start]:
        if connected(graph, neighbor, end, seen)
        return True
    return False

def fastest_route(graph, start, end):
    # <disconnected>
    vertices = set(graph)
    times = { v: float('inf') for v in vertices }
    times[start] = 0

    while vertices:
        fastest = min(vertices, lambda v: times[v])
        for neighbor in graph[fastest]:
            t = graph[fastest][times]
            overall = ntimes
