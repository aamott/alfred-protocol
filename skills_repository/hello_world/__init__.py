from skills_repository.alfred_skill import AlfredSkill

class HelloWorld(AlfredSkill):
    name="Hello World"
    
    def __init__(self, alfred_core):
        """Initialize the Hello World skill class.
            All skills should have an init method which receives
            an instance of AlfredCore. To find out more about 
            AlfredCore, read its class file.  

        Args:
            alfred_core (class): Class holding essential tools, including say(phrase) and listen()
        """
        AlfredSkill.__init__(self)
        self._alfred_core = alfred_core


    def initialize_intents(self, register_intent):
        """ registers intents to AlfredProtocol

        Receives: a reference to AlfredProtocol's intent register function
        """
        register_intent(self.handle_say_hello, ["hello", "hello world"], self)

    
    def handle_say_hello(self, phrase):
        """ Makes Alfred Protocol say, "hello world"
        
        Args:
            phrase (string): The phrase said that resulted in this function being called
        """
        self._alfred_core.say("hello world!")



def create_skill(alfred_core):
    """ Skill creator function. Creates an instance of your skill to return. 

    Args:
        alfred_core (AlfredCore): class instance with essential Alfred tools

    Returns:
        HelloWorld: An instance of the HelloWorld skill
    """
    skill_instance =  HelloWorld(alfred_core)
    return skill_instance