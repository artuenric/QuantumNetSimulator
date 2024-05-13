import networkx as nx

class Network():
    """
    Um objeto para utilizar como rede.
    """
    def __init__(self) -> None:
        self.G = None
        self._channels = None
        self._topology = None
        self._controller = None
    
    def add_host(self, host):
        """
        Adiciona um nó à rede.
        """
        # Adiciona o nó ao grafo da rede, se não existir
        if not self.G.has_node(host):
            self.G.add_node(host)
        
        # Adiciona as conexões do nó ao grafo da rede, se não existirem
        for connection in host.connections:
            if not self.G.has_edge(host, connection):
                self.G.add_edge(host, connection)
        