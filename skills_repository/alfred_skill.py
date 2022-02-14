from abc import ABC, abstractmethod, abstractproperty

class AlfredSkill(ABC):
    @abstractmethod 
    def initialize_intents(self, register_intent):
        """ registers intents to AlfredProtocol

        Receives: a reference to AlfredProtocol's intent register function
        """
        pass