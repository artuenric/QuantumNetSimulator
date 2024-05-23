from ...objects import Logger, Qubit

class PhysicalLayer():
    def __init__(self, physical_layer_id: int):
        """
        Inicializa a camada física.
        
        args:
            physical_layer_id : int : Id da camada física.
        """
        
        self._physical_layer_id = physical_layer_id
        self._qubits = []
        self.logger = Logger()
        
    def __str__(self):
        """ Retorna a representação em string da camada física. 
        
        returns:
            str : Representação em string da camada física."""
        return f'Physical Layer {self.physical_layer_id}'
    def entangle(self, qubit1: Qubit, qubit2: Qubit):
        """
        Entrelaça dois qubits.
        
        args:
            qubit1 : Qubit : Qubit 1.
            qubit2 : Qubit : Qubit 2.
        """
        
        qubit1.entangle(qubit2)
        self.qubits.append(qubit1)
        self.qubits.append(qubit2)
    @property
    def physical_layer_id(self):
        """
        Retorna o id da camada física.
        
        returns:
            int : Id da camada física.
        """
        
        return self._physical_layer_id
    
    @property
    def qubits(self):
        """
        Retorna os qubits da camada física.
        
        returns:
            list : Lista de qubits da camada física.
        """
        
        return self._qubits
    
    def epr_pair(self):
        """
        Cria um par de qubits entrelaçados.
        
        returns:
            Qubit, Qubit : Par de qubits entrelaçados.
        """
        qubit1 = Qubit()
        qubit2 = Qubit()
        qubit1.entangle(qubit2)
        self.qubits.append(qubit1)
        self.qubits.append(qubit2)
        return qubit1, qubit2
    
    def fidelity_measurement(self, qubit1: Qubit, qubit2: Qubit):
        fidelity = qubit1.fidelity(qubit2)
        self.logger.log(f'A fidelidade entre o qubit {qubit1} e o qubit {qubit2} é {fidelity}')
        return fidelity
    
    
    def Entanglement_Creation_Heralding_Protocol(self):
        """ Protocolo de criação de emaranhamento com sinalização.
        
        
        returns:
            bool : True se o protocolo foi bem sucedido, False caso contrário."""
        qubit1, qubit2 = self.epr_pair()
        fidelity = self.fidelity_measurement(qubit1, qubit2)
        if fidelity > 0.9:
            self.logger.log('O protocolo de criação de emaranhamento foi bem sucedido.')
            return True
        else:
            self.logger.log('O protocolo de criação de emaranhamento falhou.')
            return False
        
    pass