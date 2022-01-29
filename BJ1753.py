import sys
import heapq
class node():
    def __init__(self, n):
        self.n = n
        self.dist = float("inf")
        self.child = {}
        self.v = False
    @property
    def show(self):
        print(self.n, self.dist, self.child)

    def __lt__(self, other):
        return self.dist < other.dist 
    def __le__(self, other): 
        return self.dist <= other.dist
    def __gt__(self, other): 
        return self.dist > other.dist
    def __ge__(self, other): 
        return self.dist <= other.dist
    def __eq__(self, other): 
        return self.dist == other.dist
    
def make_dic(n, m):
    dic = {}
    for i in range(1, n+1):
        dic[i] = node(i)
    for i in range(m):
        x, y, dist = map(int,sys.stdin.readline().split())
        x_c = dic[x].child
        y_c = dic[y].child
        if y in x_c.keys():
            x_c[y] = min(x_c[y], dist)
        else:
            x_c[y] = dist
        
    return dic

def calcu_dist(dic, s):
    dic[s].dist = 0
    heap = [dic[s]]
    while len(heap) != 0:
        cur = heapq.heappop(heap)
        cur.v = True
        for i in cur.child.keys():
            if cur.child[i] + cur.dist < dic[i].dist:
                dic[i].dist = cur.child[i] + cur.dist
                heapq.heappush(heap, dic[i])
            
n,m = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())
dic = make_dic(n, m)
calcu_dist(dic, start)
for i in dic.keys():
    if dic[i].dist == float("inf"):
        print("INF")
    else:
        print(dic[i].dist)
