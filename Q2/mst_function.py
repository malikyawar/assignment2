def MyMinimumSpanningTree(Graph: nx.Graph) -> nx.Graph:
    mst = nx.Graph()
    mst.add_nodes_from(Graph.nodes())

    edges = sorted(Graph.edges(data=True), key=lambda x: x[2]["weight"])

    parent = {node: node for node in Graph.nodes()}

    def find(node):
        while parent[node] != node:
            node = parent[node]
        return node
    def union(u, v):
        parent[find(v)] = find(u)

    print("Building Kruskal's algorithm for MST")

    for u, v, data in edges:
        if find(u) != find(v):
            mst.add_edge(u, v, weight=data["weight"])
            union(u, v)
            print(f"Added edge ({u}, {v}) with weight {data['weight']} to MST")
    print(mst)
