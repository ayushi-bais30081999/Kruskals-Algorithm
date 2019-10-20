parent = dict()
rank = dict()
sum=0

def make_set(v):    
    parent[v] = v
    rank[v] = 0    

def find(v):    
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1, v2):    
    root1 = find(v1)
    root2 = find(v2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for v in graph['v']:
        make_set(v)
    minimum_spanning_tree = set()   
 
    edges = sorted(graph['edges'], key=lambda e: e[2])


    for edge in edges:
        v1, v2, weight = edge
        if find(v1) != find(v2):     
            union(v1, v2)
            minimum_spanning_tree.add(edge)
    return sorted (minimum_spanning_tree)



nagpur,pune,jaipur,ahmedabad,hyderabad,shimla,banglore,goa,mumbai,delhi=0,1,2,3,4,5,6,7,8,9



graph = {
    'v': [0,1, 2, 3, 4, 5, 6, 7, 8, 9],
    'edges': set([     
        (0,1,706),
        (0,2,951),
        (0,8,804),
        (0,9,1078),
        (1,2,1170),
        (1,4,562),
        (1,6,840),
        (2,9,281),
        (2,3,677),
        (3,8,524),
        (3,7,1095),
        (3,4,1220),
        (4,5,1938),
        (4,6,575),
        (5,6,2526),
        (5,9,341),
        (6,7,566),
        (6,8,980),
        (7,8,584),
        (8,9,1423),
        (8,9,980)
          ])
    }

a = kruskal(graph)
print(a)

for i in range(0,len(a)):
        sum=sum + a[i][2]
print("length of spanning tree is:",sum) 

#nagpur,pune,jaipur,ahmedabad,hyderabad,shimla,banglore,goa,mumbai,delhi
  #0     1    2      3          4         5      6       7    8      9
 
   












