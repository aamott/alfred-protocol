from skills_repository.alfred_skill import AlfredSkill

class HelloWorld(AlfredSkill):
    name="Hello World"
    
    def __init__(self):
        AlfredSkill.__init__(self)

    def initialize_intents(self, register_intent):
        """
        registers intents to AlfredProtocol

        Receives: a reference to AlfredProtocol's intent register function
        """
        register_intent(self.handle_say_hello, ["hello", "hello world"], self.name)

    
    def handle_say_hello(phrase):
        print("hello world!")

# Returns an instance of your skill
def create_skill():
    skill_instance =  HelloWorld()
    return skill_instance