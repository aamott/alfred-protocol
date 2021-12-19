from skills_repository.alfred_skill import AlfredSkill

class HelloWorld2(AlfredSkill):
    name="Hello World 2"
    phrases = ["hello again", "hello world again"]
    
    def __init__(self):
        AlfredSkill.__init__(self)
        self.name = "Hello World2"

    
    def run_skill(phrase):
        print("hello world again!")

# AlfredProtocol will call create_skill to create the skill. 
# It should register an instance of your skill, like shown.
# def register_skill(skill_register_func):
#     skill = HelloWorld2()
#     skill_register_func(skill)