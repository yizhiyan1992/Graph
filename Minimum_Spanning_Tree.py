#problem statement: Given several points and coordinates, find the shortest length to connect all points.

# solution: Minimum Spanning Tree Problem
# Here, I use Prim's Algorithm, the time complexity is O((|V|+|E|)log(|V|))

import numpy as np
import heapq
def MinimumSpanningTree(adj_list,dist):
        n=len(adj_list)
        visit=[False for _ in range(n)]
        Priority_Q=[[0,0]]
        optimal_distance=0
        heapq.heapify(Priority_Q)
        while Priority_Q !=[]:
                u=heapq.heappop(Priority_Q)
                node=u[1];distance=u[0]
                if visit[node]==False:
                        visit[node]=True
                        optimal_distance=optimal_distance+distance
                        for i in range(len(adj_list[node])):
                                if visit[adj_list[node][i]]==False:
                                        heapq.heappush(Priority_Q,[dist[node][i],adj_list[node][i]])
        return round(optimal_distance,9)

if __name__=="__main__":
        vertice=int(input())
        adj_list=[[] for _ in range(vertice)]
        dist= [[] for _ in range(vertice)]
        coordinate=[[] for _ in range(vertice)]
        for i in range(vertice):
                Coordinate=list(map(int,input().split()))
                coordinate[i]=Coordinate
        for i in range(vertice):
                for j in range(vertice):
                        if i!=j:
                                adj_list[i].append(j)
                                dist[i].append(np.sqrt((coordinate[i][0]-coordinate[j][0])**2+(coordinate[i][1]-coordinate[j][1])**2))
        print(MinimumSpanningTree(adj_list,dist))


