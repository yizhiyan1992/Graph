#use python3
def reach(adj_list,node,visit,cluster,cc):
        if visit[node]==False:
                visit[node]=True
                cluster[node]=cc
                if adj_list[node]!=[]:
                        for i in range(len(adj_list[node])):
                                reach(adj_list,adj_list[node][i],visit,cluster,cc)


def DFS(adj_list,A,B):
        visit=[False for _ in range(len(adj_list))]
        cluster=[0 for _ in range(len(adj_list))]
        cc=1
        for i in range(len(adj_list)):
               reach(adj_list,i,visit,cluster,cc)
               cc+=1
        if cluster[A]==cluster[B]:
                return 1
        else:
                return 0


if __name__=="__main__":
        vertice,edge=list(map(int,input().split()))
        adj_list=[[] for _ in range(vertice)]
        for i in range(edge):
                input_edge=list(map(int,input().split()))
                adj_list[input_edge[0]-1].append(input_edge[1]-1)
                adj_list[input_edge[1]-1].append(input_edge[0]-1)
        start,end=list(map(int,input().split()))
        start,end=start-1,end-1
        print(DFS(adj_list,start,end))







