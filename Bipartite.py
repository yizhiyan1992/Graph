import queue
#The definition of Bipartite:
# An undirected graph is called bipartite if its vertices can be split into two parts such that each edge of the graph joins to vertices from different parts.
# An alternate definition is that a graph is bipartite if its vertices can be colored with two colors such that the endpoints of each edge have different colors.

# This problem can be solved by BFS. (We can label odd distance with one color and even distance with another color, and finally look through the adjacent list)

#The time complexity is O(|E|+|V|)
#Be aware that the graph may be disconnected, and thus we need to go through all vertice.
def Bipartite(adj_list):
    n=len(adj_list)
    distance=[float('inf') for _ in range(n)]
    color=[None for _ in range(n)]
    for i in range(n):
        if color[i]==None:
            Q=queue.Queue()
            Q.put(i)
            distance[i]=0
            color[i]=1
            while not Q.empty():
                p=Q.get()
                for j in adj_list[p]:
                    if distance[j]==float('inf'):
                        distance[j]=distance[p]+1
                        if distance[j]%2==0:
                            color[j]=1
                        else:
                            color[j]=-1
    bipartite=1
    #go through all edges, if two nodes have same color, then this is not a bipartite.
    for i in range(n):
        for j in adj_list[i]:
            if color[i]==color[j]:
                bipartite=0
    return bipartite


if __name__=="__main__":
    vertice,edge=list(map(int,input().split()))
    adj_list=[[] for _ in range(vertice)]
    for i in range(edge):
        EDGE=list(map(int,input().split()))
        adj_list[EDGE[0]-1].append(EDGE[1]-1)
        adj_list[EDGE[1]-1].append(EDGE[0]-1)
    print(Bipartite(adj_list))
