class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)


routes = [
    ("Mumbai","Pune"),
    ("Mumbai", "Surat"),
    ("Surat", "Bangaluru"),
    ("Pune","Hyderabad"),
    ("Pune","Mysuru"),
    ("Hyderabad","Bangaluru"),
    ("Hyderabad", "Chennai"),
    ("Mysuru", "Bangaluru"),
    ("Chennai", "Bangaluru")
]

route_graph = Graph(routes)