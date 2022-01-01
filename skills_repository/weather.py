try:
    from skills_repository.alfred_skill import AlfredSkill
except:
    from alfred_skill import AlfredSkill

import requests

class Weather(AlfredSkill):
    name = "Get Weather"
    phrases = ["weather"]

    def __init__(self,alfred_core,api_key='c94f92f9da0a404ff27481f339dae314'):
        '''
        args: alfred_core, api_key:str
        new api_key can be made from openweathermap.org
        '''
        AlfredSkill.__init__(self)
        self._alfred_core = alfred_core
        self.api_key = api_key
    def get_weather(self):
        '''get json data of weather from api'''
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID={self.api_key}")
        j = response.json()
        return j
    def get_temp(self,w=None):
        '''Get temperature of rexburg idaho through api, return temperature in fahrenheit
        Requires network call
        '''
        # say("Getting weather from API")
        if w is None:
            w = self.get_weather()
        temp_k = w['main']['temp']
        temp_f = (temp_k - 273.15) * 9/5 + 32
        return temp_f
    def get_wind(self,w=None):
        '''return wind speed and direction
            return in format: {'speed':float,'deg':int}
        '''
        if w is None:
            w = self.get_weather()
        wind = w['wind']
        return wind
    def run_temp(self,*args):
        '''
        Makes alfred protocol say the weather for Rexburg Idaho in Fahrenheit
        '''
        temp_f = self.get_temp()
        self._alfred_core.say("The temperature in Rexburg Idaho is")
        self._alfred_core.say(f"{int(temp_f)} degrees fahrenheit")
    def run_wind(self,*args):
        wind = self.get_wind()
        directions = {0:'North',1:'North-East',2:"East",3:"South-East",4:"South",5:"South-West",
        6:"West",7:"North-West"}
        self._alfred_core.say(f"The wind in Rexburg Idaho is {wind['speed']} meters per second in a {directions[((wind['deg']+22.5)//45)%8]} direction")
        # self._alfred_core.say("The wind in Rexburg Idaho is")
        
    
    def initialize_intents(self, register_intent):
        register_intent(self.run_temp,self.phrases,self)
        register_intent(self.run_wind,['wind'],self)
        return super().initialize_intents(register_intent)


# AlfredProtocol will call create_skill to create the skill. 
# It should register an instance of your skill, like shown.
AlfredSkillSubtype = lambda:Weather('c94f92f9da0a404ff27481f339dae314')
# def register_skill(skill_register_func):
#     skill = Weather('c94f92f9da0a404ff27481f339dae314')
#     skill_register_func(skill)

def create_skill(alfred_core):
    skill_instance = Weather(alfred_core)
    return skill_instance

if __name__ == '__main__':
    '''test functionability of weather skill'''
    import sys
    sys.path.append('..')
    test = 3
    if test==1:
        '''test base functionality'''
        from core.alfred_core import AlfredCore
        ac = AlfredCore()
        weather = Weather(ac)
        weather.run_temp()
    elif test==2:
        '''test temp functionality with AlfredProtocol'''
        from alfred_protocol import AlfredProtocol
        AP = AlfredProtocol()
        skill = create_skill(AP._alfred_core)
        skill.initialize_intents(AP.register_intent)
        AP.choose_intent('weather')
    elif test==3:
        '''test wind functionality with AlfredProtocol'''
        from alfred_protocol import AlfredProtocol
        AP = AlfredProtocol()
        skill = create_skill(AP._alfred_core)
        skill.initialize_intents(AP.register_intent)
        AP.choose_intent('wind')