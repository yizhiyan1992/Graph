#Find if there is a negative cycle in the graph
#Thought: Use Bellman-Ford algorithm, and detect if there is any edge releasing at Nth iteration.
#Instead of assign infinite value to the initial distance, we can just set all initial distance to 0. Because if there is a negative cycle, the optimal distance will get lower and lower
#Time complexity: O(|v||E|)

import copy
def Negative_cycle(adj_list,weight):
    n=len(adj_list)
    dist=[0 for _ in range(n)]
    #do N iterations
    for i in range(n):
        print(dist)
        if i==n-1:
            # use deep copy when assign a list to a new variable!!!
            Distance=copy.deepcopy(dist)
        # relax all edges
        for j in range(n):
            for k in range(len(adj_list[j])):
                if dist[adj_list[j][k]]>dist[j]+weight[j][k]:
                    dist[adj_list[j][k]]=dist[j]+weight[j][k]
    if Distance==dist:
        return 0 #No negative cycle
    else:
        return 1 #There is at least one negative cycle

if __name__=="__main__":
    vertice,edge=list(map(int,input().split()))
    adj_list=[[] for _ in range(vertice)]
    weight=[[] for _ in range(vertice)]
    for i in range(edge):
        EDGE=list(map(int,input().split()))
        adj_list[EDGE[0]-1].append(EDGE[1]-1)
        weight[EDGE[0]-1].append(EDGE[2])
    print(Negative_cycle(adj_list,weight))