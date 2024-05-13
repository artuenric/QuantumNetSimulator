class Epr():
    def __init__(self, qubits: list) -> None:
        self._initial_fidelity = 1.0
        self._current_fidelity = None
        
        # Ainda vamos ver se isso vai ser necessário
        # self.qubits = qubits

    def __str__(self):
        return f'EPR({self.qubits})'

    def get_initial_fidelity(self):
        return self._initial_fidelity
    
    def get_current_fidelity(self):
        return self._current_fidelity