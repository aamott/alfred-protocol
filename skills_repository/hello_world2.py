from skills_repository.alfred_skill import AlfredSkill

class HelloWorld2(AlfredSkill):
    name="Hello World 2"
    
    def __init__(self, alfred_core):
        """Initialize the Hello World skill class.
            All skills should have an init method which receives
            an instance of AlfredUtils. To find out more about 
            AlfredUtils, read its class file.  

        Args:
            alfred_core (class): Class holding essential tools, including say(phrase) and listen()
        """
        AlfredSkill.__init__(self)
        self._alfred_core = alfred_core


    def initialize_intents(self, register_intent):
        """ registers intents to AlfredProtocol

        Receives: a reference to AlfredProtocol's intent register function
        """
        register_intent(self.handle_say_hello, ["hello again", "hello world 2"], self)

    
    def handle_say_hello(self, phrase):
        """ Makes Alfred Protocol say, "hello world"
        
        Args:
            phrase (string): The phrase said that resulted in this function being called
        """
        self._alfred_core.say("Hello again, world!")



def create_skill(alfred_core):
    """ Skill creator function. Creates an instance of your skill to return. 

    Args:
        alfred_core (AlfredUtils): class instance with essential Alfred tools

    Returns:
        HelloWorld2: An instance of the HelloWorld2 skill
    """
    skill_instance =  HelloWorld2(alfred_core)
    return skill_instance