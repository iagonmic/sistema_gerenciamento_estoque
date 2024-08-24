class Graph:

    def __init__(self):
        self.structure = {}

    def get_nodes(self, origin):
        if origin in self.structure.keys:
            return self.structure.get(origin)
        
        return []
    
    def add_node(self, origin, end, ordered: bool = False):
        nodes = self.get_nodes(origin)
        nodes.append(end)
        
        self.structure[origin] = nodes

        if not ordered:
            self.add_node(end, origin, True)

    def remove_node(self, origin, ordered: bool = False):
        if origin in self.structure.keys:
            origin_nodes = self.get_nodes(origin)  
            self.structure.pop(origin)

            if not ordered:
                for node in origin_nodes:
                    node_nodes = self.get_nodes(node)
                    node_nodes.remove(origin)

                    self.structure[node] = node_nodes

            