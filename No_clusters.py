#use python3
def reach(adj_list,node,visit,cluster,cc):
        if visit[node]==False:
                visit[node]=True
                cluster[node]=cc
                if adj_list[node]!=[]:
                        for i in range(len(adj_list[node])):
                                reach(adj_list,adj_list[node][i],visit,cluster,cc)


def DFS(adj_list):
        visit=[False for _ in range(len(adj_list))]
        cluster=[0 for _ in range(len(adj_list))]
        cc=1
        for i in range(len(adj_list)):
               reach(adj_list,i,visit,cluster,cc)
               cc+=1
        return len(set(cluster))


if __name__=="__main__":
        vertice,edge=list(map(int,input().split()))
        adj_list=[[] for _ in range(vertice)]
        for i in range(edge):
                input_edge=list(map(int,input().split()))
                adj_list[input_edge[0]-1].append(input_edge[1]-1)
                adj_list[input_edge[1]-1].append(input_edge[0]-1)
        print(DFS(adj_list))







