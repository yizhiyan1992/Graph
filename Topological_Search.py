#use python3

# Topological search
#Step1: Use DFS to find the queue based on the post-visit (do DFS on reverse graph, in this case we can find the sink nodes in original graph)
#Step2: Do DFS on the original graph (this time, visit the node based on the queue obtained before)

# set a clock to count pre and post visit and derive the queue
class Visit():
    def __init__(self,n):
        self.clock=1
        self.pre_order=[0 for _ in range(n)]
        self.post_order=[0 for _ in range(n)]
        self.queue=[]

    def pre_visit(self,i):
        self.pre_order[i]=self.clock
        self.clock+=1
    def post_visit(self,i):
        self.post_order[i]=self.clock
        self.clock+=1
        self.queue.append(i)

def explore(adj_list,visit,i,Visit_order=None,Topo_order=None):
    if visit[i]==False:
        if Topo_order!=None:
            Topo_order.append(i)
        if Visit_order!=None:
            Visit_order.pre_visit(i)
        visit[i]=True
        for j in adj_list[i]:
            explore(adj_list,visit,j,Visit_order)
        if Visit_order!=None:
            Visit_order.post_visit(i)
    return

# do depth-first search
def DFS(adj_list):
    n=len(adj_list)
    visit=[False for _ in range(n)]
    for i in range(n):
        explore(adj_list,visit,i,Visit_order=Visit_order,Topo_order=None)
    return

# after we obtain the stack, do the topological search on original graph
def Topological_ordering(adj_list,Visit_order):
    n=len(adj_list)
    visit=[False for _ in range(n)]
    Topo_order=[]
    for i in range(n):
        explore(adj_list,visit,Visit_order.queue[n-i-1],Visit_order=None,Topo_order=Topo_order)
    Topo_order.reverse()
    Topo_order=list(map(lambda x:x+1,Topo_order))
    return Topo_order

if __name__=="__main__":
    vertice,edge=list(map(int,input().split()))
    adj_list=[[] for _ in range(vertice)]
    reverse_adj_list=[[] for _ in range(vertice)]
    Visit_order=Visit(vertice)
    for i in range(edge):
        Edge=list(map(int,input().split()))
        adj_list[Edge[0]-1].append(Edge[1]-1)
        reverse_adj_list[Edge[1]-1].append(Edge[0]-1)
    DFS(reverse_adj_list)
    Topo_order=Topological_ordering(adj_list,Visit_order)
    Topo_order=list(map(str,Topo_order))
    print(' '.join(Topo_order))