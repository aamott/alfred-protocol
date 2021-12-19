class AlfredSkill:
    name = "Generic Skill"
    phrases = []

    def __init__(self):
        pass
    
    @classmethod
    def register_skill(cls,skill_register_func,*args,**kwargs):
        skill = cls(*args,**kwargs)
        skill_register_func(skill, skill.phrases)

ARGS = []
KWARGS = {}