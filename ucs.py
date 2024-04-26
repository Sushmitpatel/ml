from queue import PriorityQueue

def ucs(graph,start,goal):
    pq=PriorityQueue()
    pq.put((0,start,[]))
    n = len(graph) + 3
    dis={}
    dis[start]=0
    while not pq.empty():
        cost,par,path=pq.get()
        if par==goal:
            return path,cost
        for child,e_cost in graph[par]:
                   if(child not in dis.keys()):
                       dis[child]=float('inf')
                   if(dis[child]>dis[par]+e_cost):
                    total_cost=cost+e_cost
                    dis[child]=total_cost
                    pq.put((total_cost,child,path+[(par,child)]))
    return [],0
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
path,cost=ucs(graph,start,goal)
if path:
    print(f"path from {start} node to {goal} node : {path}")
    print(f"total cost :{cost}")
else:
    print(f"no path found")
