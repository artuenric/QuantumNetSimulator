
from ..objects import Logger
class Host():
    def __init__(self, host_id: str, probability_on_demand_qubit_create: float = 0.5, probability_replay_qubit_create: float = 0.5, max_qubits_create: int = 10, memory_size: int = 10) -> None:
        # Sobre a rede
        self._host_id = host_id
        self._connections = []
        # Sobre o host
        self._memory = []
        self._memory_size = memory_size
        self._max_qubits_create = max_qubits_create
        self._probability_on_demand_qubit_create = probability_on_demand_qubit_create
        self._probability_replay_qubit_create = probability_replay_qubit_create
        # Sobre a execução
        self.logger = Logger.get_instance()
    
    def __str__(self):
        return f'{self.host_id}'
    
    @property
    def host_id(self):
        """
        Nome do host.

        Returns:
            str : Nome do host.
        """
        return self._host_id
    
    @property
    def connections(self):
        """
        Conexões do host.

        Returns:
            list : Lista de conexões.
        """
        return self._connections
    
    @property
    def memory(self):
        """
        Memória do host.

        Returns:
            list : Lista de qubits.
        """
        return self._memory
    
    def add_connection(self, host_id_for_connection: str):
        """
        Adiciona uma conexão ao host. A conexão é um host_id.

        Args:
            host_id_for_connection (str): Host ID do host que será conectado.
        """
        
        if type(host_id_for_connection) != str:
            raise Exception('O valor fornecido para host_id_for_connection não é uma string.')
        
        if host_id_for_connection not in self.connections:
            self.connections.append(host_id_for_connection)
        
        