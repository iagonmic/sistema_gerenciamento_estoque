class Graph:

    def __init__(self):
        self.structure = {}

    def get_nodes(self, origin):
        if origin in self.structure:
            return self.structure.get(origin)
        
        return []
    
    def add_node(self, origin, end, ordered: bool):
        nodes = self.get_nodes(origin)
        nodes.append(end)
        
        self.structure[origin] = nodes

        if not ordered:
            self.add_node(end, origin, True)