import queue
#use Breadth First Search to find the shortest path for unweighted graph

# Basic idea: use queue to store each node, pop one element each time, and detect if connected nodes are visited already or not
# If not visit, push element, assign the distance +1
# Do it until the queue is empty

#Run time analysis: Each node is only added to the queue once, the edges of each node will be detected twice (because this is undirected graph.
#The time complexity is O(|E|+|V|)

def BFS(adj_list,start,end):
    n=len(adj_list)
    distance=[float('inf') for _ in range(n)]
    distance[start]=0
    Q=queue.Queue()
    Q.put(start)
    while not Q.empty():
        p=Q.get()
        for i in adj_list[p]:
            if distance[i]==float('inf'):
                distance[i]=distance[p]+1
                Q.put(i)

    if distance[end]==float('inf'):
        return -1
    else:
        return distance[end]

if __name__=="__main__":
    vertice,edge=list(map(int,input().split()))
    adj_list=[[] for _ in range(vertice)]
    for i in range(edge):
        EDGE=list(map(int,input().split()))
        adj_list[EDGE[0]-1].append(EDGE[1]-1)
        adj_list[EDGE[1]-1].append(EDGE[0]-1)
    start,end=list(map(int,input().split()))
    start,end=start-1,end-1
    print(BFS(adj_list,start,end))