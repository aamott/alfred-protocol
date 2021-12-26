from abc import ABC, abstractmethod, abstractproperty
IGNORE = True
class AlfredSkill(ABC):
    @abstractmethod 
    def initialize_intents(self, register_intent):
        """
        registers intents to AlfredProtocol

        Receives: a reference to AlfredProtocol's intent register function
        """
        pass
