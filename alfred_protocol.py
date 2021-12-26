# For importing skills
from importlib import import_module
import os
from utilities.AudioUI import AudioUI

# For working with audio
from gtts import gTTS
from playsound import playsound

#######################################
# AlfredProtocol class
# Description: pulls all our skills together to form a functioning
# voice assistant.
# Parameters: 
#######################################
class AlfredProtocol:
  """Acts as a digital assistant, trying to follow commands"""

  def __init__(self, skills = []):
    self._intents = skills
  

  def register_intent(self, intent_callback, phrases, skill_name):
    """Registers an intent to the intent list. 

    Arguments: 
    skill_callback -- function to run when skill is chosen. Should take phrase matched as a parameter.
                    Ex.  -- phrase: "say cookies" results in
                      skill_callback("say cookies)
    phrases -- string[]. A list of phrases that will be exactly matched to call function.
    """
    # DM: phrases should probably be converted to lowercase
    # DM: also, consider using a set rather than a list for its O(1) look up time.
    # DM:   Note: might not be worthwhile if number of phrases is low
    intent_data = {"intent": intent_callback, "phrases": phrases, "skill name": skill_name}
    self._intents.append(intent_data)
      

  def choose_intent(self, command):
    """ Makes a best guess at which skill a command corresponds to (a.k.a. 'intent parsing')
    
    Arguments:
    command -- string. What the user wants.
    """
    
    # choose the intent
    # DM: O(n*m) where n==number of skills, m is number of phrases
    for skill_info in self._intents:
      for phrase in skill_info['phrases']:
        if phrase == command:
          top_intent = skill_info["intent"]
          # run the intent
          top_intent()

  def say(self, text):
    # send audio to google
    google_audio = gTTS(text)

    # save audio
    filename = "speech.mp3"
    google_audio.save(filename)

    # play speech
    playsound(filename)



def register_skills(alfred_instance):
  """ Runs through the skills folder and tries to load each module in it and call create_skill to register it
  """
  
  skills_folder = "skills_repository"
  for filepath in os.listdir(os.path.abspath(skills_folder)): 

    # load module containing the skill
    module_name = skills_folder + '.' + filepath.strip(".py")
    skill_module = import_module(module_name)
    if 'IGNORE' in dir(skill_module):
        continue
    try:
      # TODO: consider passing in commonly needed methods, like say and listen, when creating skill instance
      skill = skill_module.create_skill()

      # Ask skill to load intents
      skill.initialize_intents(alfred_instance.register_intent)

      print('Loaded Skill', skill.name)

    except : # TODO: Fix trying to load alfred_skill base class and __pycache__
      print("Skipping invalid skill, ", skill_module)


if __name__ == "__main__":
  # ###############################
  # Start
  alfred_instance = AlfredProtocol()
  
  register_skills(alfred_instance)

  # clear the terminal a bit    
  print("\n\n\n")

  # TEST 
  alfred_instance.choose_intent("hello")

  # Run
  command = ''
  while command != "quit" and command != "exit":
    command = input("> ")
    alfred_instance.choose_intent(command)