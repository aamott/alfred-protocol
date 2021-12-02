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
  

  def register_skill(self, function, phrases):
    """Registers a skill to the skill list. 

    Arguments: 
    function -- Function to run when skill is chosen. Should take phrase matched as a parameter.
                    Ex.  -- phrase: "say cookies" results in
                      function("say cookies)
    phrases -- string[]. A list of phrases that will be exactly matched to call function.
    """
    # DM: phrases should probably be converted to lowercase
    # DM: also, consider using a set rather than a list for its O(1) look up time.
    # DM:   Note: might not be worthwhile if number of phrases is low
    skill = {"function": function, "phrases": phrases}
    self._skills.append(skill)
      

  def choose_skill(self, command):
    """ Makes a best guess at which skill a command corresponds to (a.k.a. 'intent parsing')
    
    Arguments:
    command -- string. What the user wants.
    """
    top_skill = ''
    
    # choose the skill
    # DM: O(n*m) where n==number of skills, m is number of phrases
    for skill in self._skills:
    #   for phrase in skill.phrases:
      for phrase in skill['phrases']:
        if phrase == command:
          top_skill = skill

    # run the skill
    # top_skill.function()
    top_skill['function']()

  def say(self, text):
    # send audio to google
    google_audio = gTTS(text)

    # save audio
    filename = "speech.mp3"
    google_audio.save(filename)

    # play speech
    playsound(filename)


# ###############################
# Start
alfred_instance = AlfredProtocol()
alfred_instance.register_skill(print,["print"])
alfred_instance.choose_skill('print')
alfred_instance.say("hello friends")

# Register any skills
