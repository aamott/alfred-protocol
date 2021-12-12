from skills_repository.alfred_skill import AlfredSkill

class HelloWorld(AlfredSkill):
    name = "Hello World"
    phrases = ["hello", "hello world"]

    def __init__(self):
        AlfredSkill.__init__(self)
        self.name = "Hello World"

    
    def run_skill(phrase):
        print("hello world!")
        
# AlfredProtocol will call create_skill to create the skill. 
# It should register an instance of your skill, like shown.
def register_skill(skill_register_func):
    skill = HelloWorld()
    skill_register_func(skill, skill.phrases)
