#use python3
# to see if there exists a cycle in a graph
# The cycle exist if and only if there is a back edge in the graph ( the edge connect the current searching node to its ancestor (i.e. nodes still in circulation))
# To solve this problem, we can build a Stack, push the element when visit the Stack, and pop the element when finish its exploration

def explore(adj_list,visit,i,cycle,Stack):
    if visit[i]==False:
        visit[i]=True
        Stack.append(i)
        for j in adj_list[i]:
            if j in Stack:
                cycle=1
                return cycle
            cycle=explore(adj_list,visit,j,cycle,Stack)
        Stack.pop(-1)
    return cycle

def If_cycle(adj_list):
    n=len(adj_list)
    visit=[False for i in range(n)]
    cycle=0
    for i in range(n):
        Stack=[]
        cycle=explore(adj_list,visit,i,cycle,Stack)
        if cycle==1:
            break
    return cycle
if __name__=="__main__":
    vertice,edge=list(map(int,input().split()))
    directed_adj_list=[[] for _ in range(vertice)]
    for i in range(edge):
        Edge=list(map(int,input().split()))
        directed_adj_list[Edge[0]-1].append(Edge[1]-1)
    print(If_cycle(directed_adj_list))
