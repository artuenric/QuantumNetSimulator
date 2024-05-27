from ...objects import Logger, Qubit, Epr
from ...components import Host
from random import randrange

class PhysicalLayer():
    def __init__(self, physical_layer_id: int = 0):
        """
        Inicializa a camada física.
        
        args:
            physical_layer_id : int : Id da camada física.
        """
    
        self._physical_layer_id = physical_layer_id
        self._qubits = []
        self.logger = Logger.get_instance()
        
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
        return Epr([qubit1, qubit2])
    
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

    def create_epr_pair(self, qubit1: Qubit, qubit2: Qubit):
        """
        Cria um par de qubits entrelaçados.
        
        returns:
            Qubit, Qubit : Par de qubits entrelaçados.
        """
        epr = self.entangle(qubit1, qubit2)
        # Adicionar esse EPR em algum lugar
        return epr
      
    def fidelity_measurement_only_one(self, qubit: Qubit):
        """
        Mede a fidelidade de um qubit.

        Args:
            qubit (Qubit): Qubit.

        Returns:
            float: Fidelidade do qubit.
        """
        fidelity = qubit.fidelity()
        self.logger.log(f'A fidelidade do qubit {qubit} é {fidelity}')
        return fidelity
    
    def fidelity_measurement(self, qubit1: Qubit, qubit2: Qubit):
        """
        Mede a fidelidade entre dois qubits.

        Args:
            qubit1 (Qubit): Qubit 1.
            qubit2 (Qubit): Qubit 2.

        Returns:
            float: Fidelidade entre os qubits.
        """
        fidelity = qubit1.fidelity(qubit2)
        self.logger.log(f'A fidelidade entre o qubit {qubit1} e o qubit {qubit2} é {fidelity}')
        return fidelity
    
    def entanglement_creation_heralding_protocol(self, alice: Host, bob: Host):

        """ 
        Protocolo de criação de emaranhamento com sinalização.
        
        returns:
            bool : True se o protocolo foi bem sucedido, False caso contrário.
        """
        # Alice e Bob criam um par EPR
        qubit1 = alice.get_last_qubit()
        qubit2 = bob.get_last_qubit()
        self.create_epr_pair(qubit1, qubit2)
        # Checa a fidelidade
        fidelity = self.fidelity_measurement(qubit1, qubit2)
        
        # Adicionar par EPR no canal
        
        # Pode dar errado tanto pela probabilidade, quanto pela fidelidade
        if fidelity > 0.9:
            self.logger.log('O protocolo de criação de emaranhamento foi bem sucedido.')
            # Adicionar par EPR no canal
            return True
        self.logger.log('O protocolo de criação de emaranhamento falhou.')
        return False
    
    #    1.1. ECHP_on_demand:

    #-Fidelidade_inicial: Fidelidade_qubit1* Fidelidade_qubit2
    def echp_on_demand(self, alice: Host, bob: Host):
    #-Proabilidade de Sucesso do ECHP: Prob_replay_epr_create * Fidelidade_qubit1* Fidelidade_qubit2
        prob_replay_epr_create = 0.9
        qubit1 = alice.get_last_qubit()
        qubit2 = bob.get_last_qubit()
        fidelidade_qubit1 = self.fidelity_measurement_only_one(qubit1)
        fidelidade_qubit2 = self.fidelity_measurement_only_one(qubit2)
        proabilidade_de_sucesso_do_echp = prob_replay_epr_create * fidelidade_qubit1* fidelidade_qubit2
        self.logger.log(f'A probabilidade de sucesso do ECHP é {proabilidade_de_sucesso_do_echp}')
        return proabilidade_de_sucesso_do_echp

    def echp_on_replay(self, alice: Host, bob: Host):
        #o ECHP_on_replay é quando a fidelidade decaiu e o protocolo é refeito
