# Kruskals-Algorithm
Implementation of Kruskals Algorithm in Python.
      
      Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected garph. The algorithm operates by adding the egdes one by one in the order of their increasing lengths, so as not to form a cycle.Here is the description for my source code of implementing kruskal's algorithm in python.
      
      Here,I had used dict() in-build-function creates dictionary which is collection of key-value pairs.Various methods are used to implement kruskal's algorithm i.e. make_set(v) it creates set of every vertices, find(v) is used for path compression to find root, union(v1,v2) detects the cycle i.e. if there exist no connectivity(complete graph) between the two nodes then the vertex is added, kruskal(graph) function having graph(node1,node2,weight) as parameter is passed.kruskal(graph) call the above mentioned function to get the edges that are added in minimum cost tree/graph.Finally, the weight of edges(i.e. find using kruskal(graph)) is added to get the minimum cost of tree/graph.
      
     The above is the description of Kruskal's Algorithm implementation.
      
