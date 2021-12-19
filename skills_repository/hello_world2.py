from skills_repository.alfred_skill import AlfredSkill

class HelloWorld2(AlfredSkill):
    name="Hello World 2"
    
    def __init__(self):
        AlfredSkill.__init__(self)

    def initialize_intents(self, register_intent):
        """
        registers intents to AlfredProtocol

        Receives: a reference to AlfredProtocol's intent register function
        """
        register_intent(self.handle_say_hello, ["hello again", "hello world again"], self.name)

    
    def handle_say_hello(phrase):
        print("hello world again!")

<<<<<<< HEAD
# AlfredProtocol will call create_skill to create the skill. 
# It should register an instance of your skill, like shown.
# def register_skill(skill_register_func):
#     skill = HelloWorld2()
#     skill_register_func(skill)
=======
# Returns an instance of your skill
def create_skill():
    skill_instance =  HelloWorld2()
    return skill_instance
>>>>>>> 6e3346afbedeab46eafe65593706ad058ba42ea7
