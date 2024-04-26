from queue import PriorityQueue
heuristic_values={
    'A':7,
    'B':6,
    'C':8,
    'D':4,
    'E':3,
    'F':5,
    'G':0
}
def ucs(graph,start,goal):
    pq=PriorityQueue()
    pq.put((0,start,[]))
    g_value={}
    g_value[start]=0
    while not pq.empty():
        f_cost,par,path=pq.get()
        if par==goal:
            return path
        for child,e_cost in graph[par]:
                   tentative_g=g_value[par]+e_cost
                   if(tentative_g<g_value.get(child,float('inf'))):
                    g_value[child]=tentative_g
                    total_cost=tentative_g+heuristic_values[child]
                    pq.put((total_cost+heuristic_values[child],child,path+[(par,child)]))
    return []
graph={
    'A':[('B',5),('C',3)],
    'B':[('A',5),('D',8),('E',2)],
    'C':[('A',3),('F',4)],
    'D':[('B',8)],
    'E':[('B',2),('G',5)],
    'F':[('C',4)],
    'G':[('E',5)],
}
start='A'
goal='F'
path=ucs(graph,start,goal)
if path:
    print(f"path from {start} node to {goal} node : {path}")
else:
    print(f"no path found")
