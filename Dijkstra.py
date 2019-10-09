#Find the shortest path in non-negative graph
#The time complexity of Dijkstra algorithm is O((|E|+|V|)log(|V|)) if using priority queue
import heapq

def Dijkstra(adj_list,s,e):
    n=len(adj_list)
    visit=[False for _ in range(n)]
    shortest_path=[float('inf') for _ in range(n)]
    shortest_path[s]=0
    Priority_Q=[[float('inf'),i] for i in range(n)]
    Priority_Q[s]=[0,s]
    heapq.heapify(Priority_Q)
    while Priority_Q!=[]:
        u=heapq.heappop(Priority_Q)[1]
        # visit can prevent duplicate nodes from priority queue
        if visit[u]==False:
            visit[u]=True
            for i in adj_list[u]:
                if shortest_path[i[0]]>shortest_path[u]+i[1]:
                    shortest_path[i[0]]=shortest_path[u]+i[1]
                    #when there is a update of the dist, just append the updated dist and node into the priority queue. This is to guarantee log(n) time.
                    heapq.heappush(Priority_Q,[shortest_path[u]+i[1],i[0]])

    return shortest_path[e] if shortest_path[e]!=float('inf') else -1

if __name__=="__main__":
    vertice,edge=list(map(int,input().split()))
    adj_list=[[] for _ in range(vertice)]
    for i in range(edge):
        EDGE=list(map(int,input().split()))
        #adj_list is a weighted list, the format is [node,weight]
        adj_list[EDGE[0]-1].append([EDGE[1]-1,EDGE[2]])
    # s is the start node, e is the end node
    s,e=list(map(int,input().split()))
    s,e=s-1,e-1
    print(Dijkstra(adj_list,s,e))