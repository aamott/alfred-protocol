from skills_repository.alfred_skill import AlfredSkill
import requests

class Weather(AlfredSkill):
    name = "Get Weather"
    phrases = ["Weather"]

    def __init__(self,api_key):
        AlfredSkill.__init__(self)
        self.api_key = api_key
    def run_skill(self,ap_instance):
        ap_instance.audio_ui.say("The temperature in Rexburg Idaho is")
        # time.sleep(0.1)
        temp_f = self.get_weather()
        ap_instance.audio_ui.say(f"{int(temp_f)} degrees fahrenheit")
    def get_weather(self):
        # say("Getting weather from API")
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID={self.api_key}")
        j = response.json()
        temp_k = j['main']['temp']
        temp_f = (temp_k - 273.15) * 9/5 + 32
        return temp_f


# AlfredProtocol will call create_skill to create the skill. 
# It should register an instance of your skill, like shown.
AlfredSkillSubtype = lambda:Weather('c94f92f9da0a404ff27481f339dae314')
# def register_skill(skill_register_func):
#     skill = Weather('c94f92f9da0a404ff27481f339dae314')
#     skill_register_func(skill)

