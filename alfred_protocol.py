# For importing skills
import importlib
import os

# import skills_repository
# from pkgutil import iter_modules

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
    self._skills = skills
  

  def register_skill(self, skill, phrases):
    """Registers a skill to the skill list. 

    Arguments: 
    skill -- class to run when skill is chosen. Should take phrase matched as a parameter.
                    Ex.  -- phrase: "say cookies" results in
                      skill.run_skill("say cookies)
    phrases -- string[]. A list of phrases that will be exactly matched to call function.
    """
    # DM: phrases should probably be converted to lowercase
    # DM: also, consider using a set rather than a list for its O(1) look up time.
    # DM:   Note: might not be worthwhile if number of phrases is low
    skill = {"skill": skill, "phrases": phrases}
    self._skills.append(skill)
      

  def choose_skill(self, command):
    """ Makes a best guess at which skill a command corresponds to (a.k.a. 'intent parsing')
    
    Arguments:
    command -- string. What the user wants.
    """
    top_skill = ''
    
    # choose the skill (skill is a class)
    # DM: O(n*m) where n==number of skills, m is number of phrases
    for skill in self._skills:
      for phrase in skill.phrases:
        if phrase == command:
          top_skill = skill["skill"]

    # run the skill
    # top_skill.function()
    top_skill.run_skill()

  def say(self, text):
    # send audio to google
    google_audio = gTTS(text)

    # save audio
    filename = "speech.mp3"
    google_audio.save(filename)

    # play speech
    playsound(filename)


if __name__ == "__main__":
  # ###############################
  # Start
  alfred_instance = AlfredProtocol()
  
  # Register skills - runs through the skills_repository folder and tries to load each module in it and call create_skill to register it
  for filepath in os.listdir(os.path.abspath("skills_repository")):  # go through each module in the directory
    module = importlib.import_module("skills_repository." + filepath.strip(".py"))
    try:
      skill = module.register_skill(alfred_instance.register_skill)
      print('Loaded skill')
    except : # TODO: Fix trying to load alfred_skill base class and __pycache__
      print("Skipping invalid skill, ", module)

  # just clear the terminal a bit    
  print("\n\n\n")

  # try to run a skill to test!
  alfred_instance.choose_skill("hello")