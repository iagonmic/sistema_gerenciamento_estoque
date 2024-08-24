class Graph:

    def __init__(self):
        self.structure = {}

    def get_connectors(self, origin):
        if origin in self.structure:
            return self.structure.get(origin)
        
        return []
    
    def add_graph(self, origin, end, ordened: bool):
        connectors = self.get_connectors(origin)
        connectors.append(end)
        
        self.structure[origin] = connectors

        if ordened:
            self.add_graph(end, origin, False)