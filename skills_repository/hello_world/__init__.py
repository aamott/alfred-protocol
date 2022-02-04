from skills_repository.alfred_skill import AlfredSkill

class HelloWorld(AlfredSkill):
    name="Hello World"
    
    def __init__(self, alfred_utils):
        """Initialize the Hello World skill class.
            All skills should have an init method which receives
            an instance of AlfredUtils. To find out more about 
            AlfredUtils, read its class file.  

        Args:
            alfred_utils (class): Class holding essential tools, including say(phrase) and listen()
        """
        AlfredSkill.__init__(self)
        self._alfred_utils = alfred_utils


    def initialize_intents(self, register_intent):
        """ registers intents to AlfredProtocol

        Receives: a reference to AlfredProtocol's intent register function
        """
        register_intent(self.handle_say_hello, ["hello", "hello world"], self)
        register_intent(self.handle_repeat_after_me, ["repeat", "repeat after me"], self)

    
    def handle_say_hello(self, phrase):
        """ Makes Alfred Protocol say, "hello world"
        
        Args:
            phrase (string): The phrase said that resulted in this function being called
        """
        self._alfred_utils.say("hello world!")

    def handle_repeat_after_me(self, phrase):
        new_phrase = self._alfred_utils.listen()
        self._alfred_utils.say(new_phrase)



def create_skill(alfred_utils):
    """ Skill creator function. Creates an instance of your skill to return. 

    Args:
        alfred_utils (AlfredUtils): class instance with essential Alfred tools

    Returns:
        HelloWorld: An instance of the HelloWorld skill
    """
    skill_instance =  HelloWorld(alfred_utils)
    return skill_instance