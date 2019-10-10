#Given n points on a plane and an integer k, compute the largest possible value of d such that the given points can be partitioned into k non-empty subsets in such a way that
# the distance between any two points from different subsets is at least d.

# Thought: consider the minimum spanning tree, if there are k clusters, the largest d should be (k-2)th largest branch in the MST
import heapq
import numpy as np

def Find_cluster(adj_list,weight,no_cluster):
        n=len(adj_list)
        visit=[False for _ in range(n)]
        branch=[]
        Priority_Q=[[0,0]]
        while Priority_Q !=[]:
                u=heapq.heappop(Priority_Q)
                distance=u[0];node=u[1]
                if visit[node]==False:
                        visit[node]=True
                        branch.append(distance)
                        for i in range(len(adj_list[node])):
                                if visit[adj_list[node][i]]==False:
                                        heapq.heappush(Priority_Q,[weight[node][i],adj_list[node][i]])
        branch.sort(reverse=True)
        return round(branch[no_cluster-2],10)

if __name__=="__main__":
        vertice=int(input())
        coordinates=[]
        for i in range(vertice):
                Cor=list(map(int,input().split()))
                coordinates.append(Cor)
        no_cluster=int(input())

        adj_list=[[] for _ in range(vertice)]
        weight=[[] for _ in range(vertice)]
        for i in range(vertice):
                for j in range(vertice):
                        if i!=j:
                                adj_list[i].append(j)
                                weight[j].append(np.sqrt((coordinates[i][0]-coordinates[j][0])**2+(coordinates[i][1]-coordinates[j][1])**2))
        print(Find_cluster(adj_list,weight,no_cluster))




