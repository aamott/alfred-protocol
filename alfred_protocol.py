# For importing skills
from importlib import import_module
import os
import string

from utilities.alfred_utils import AlfredUtils


#######################################
# AlfredProtocol class
# Description: pulls all our skills together to form a functioning
# voice assistant.
# Parameters: 
#######################################
class AlfredProtocol:
  """Acts as a digital assistant, trying to follow commands"""

  def __init__(self, alfred_core = None, skills = []):
    self._intents = skills
    if alfred_core:
      self._alfred_core = alfred_core
    else:
      self._alfred_core = AlfredUtils()
  

  def register_intent(self, intent_callback, phrases, skill_class = None):
    """Registers an intent to the intent list. 

    Arguments: 
    skill_callback -- function to run when skill is chosen. Should take phrase matched as a parameter.
                    Ex.  -- phrase: "say cookies" results in
                      skill_callback("say cookies)
    phrases -- string[]. A list of phrases that will be exactly matched to call function.
    """
    # DM: also, consider using a set rather than a list for its O(1) look up time.
    # error checking
    if not callable(intent_callback):
      return
    if len(phrases) < 1:
      return

    # make sure all phrases are lowercase and have no punctuation
    for phrase in phrases:
      phrase = phrase.lower()
      phrase = phrase.translate(str.maketrans('', '', string.punctuation))

    # register intent
    intent_data = {"intent": intent_callback, "phrases": phrases, "skill_class": skill_class}
    self._intents.append(intent_data)
      

  def choose_intent(self, command):
    """ Makes a best guess at which skill a command corresponds to (a.k.a. 'intent parsing')
    
    Arguments:
    command -- string. What the user wants.
    """
    
    # DM: O(n*m) where n==number of skills, m is number of phrases
    for intent_info in self._intents:
      for phrase in intent_info['phrases']:
        if command == phrase:
          top_intent = intent_info["intent"]
          # run the intent
          top_intent(phrase)


  def say(self, text):
    self._alfred_core.say(text)

  def listen(self):
    phrase = self._alfred_core.listen()
    return phrase



#################################
# Helper Functions
# Put Alfred Protocol together and run it in a loop
#################################
def register_skills(alfred_instance):
  """ Runs through the skills folder and tries to load each module in it and call create_skill to register it
  """
  
  skills_folder = "skills_repository"
  for filepath in os.listdir(os.path.abspath(skills_folder)): 

    # load module containing the skill
    module_name = skills_folder + '.' + filepath.strip(".py")
    skill_module = import_module(module_name)
    
    try:
      # create the skill
      if hasattr(skill_module, "create_skill"):
        skill = skill_module.create_skill( alfred_instance._alfred_core )

        # Ask skill to load intents
        skill.initialize_intents(alfred_instance.register_intent)

        print('Loaded Skill', skill.name)

    except Exception as e:
      print("Error while loading skill from module", skill_module)
      print("\t", e)


if __name__ == "__main__":
  # ###############################
  # Start
  alfred_instance = AlfredProtocol()
  
  register_skills(alfred_instance)
  print("\n\n\n")

  # TEST and say hello
  # alfred_instance.choose_intent("hello")

  #################################
  # Run
  command = ''
  while command != "quit" and command != "exit":
    command = input("> ")
    alfred_instance.choose_intent(command)