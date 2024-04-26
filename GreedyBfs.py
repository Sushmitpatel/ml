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
def greedy_best_first_search(graph,start,goal):
    pq=PriorityQueue()
    visited=set()
    pq.put((heuristic_values[start],start,[],0))
    while not pq.empty():
        heuristic_cost,par,path,cost=pq.get()
        while not pq.empty():
            pq.get()
        if par==goal:
            return path,cost
        if par not in visited:
            visited.add(par)
        for child,e_cost in graph[par]:
            if child not in visited:
                neighbour_h=heuristic_values[child]
                total_cost=cost+e_cost
                pq.put((neighbour_h,child,path+[(par,child)],total_cost))
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
goal='G'
path,cost=greedy_best_first_search(graph,start,goal)
if path:
    print(f"path from {start} node to {goal} node : {path}")
    print(f"total cost :{cost}")
else:
    print(f"no path found")
