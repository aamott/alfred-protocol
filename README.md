# alfred-protocol
A voice assistant built as an educational project with the [Society of Artificial Intelligence](https://sai-byui.github.io/) at BYU - Idaho with a focus on clarity, simplicity, and extensibility.

# Installation
### Requirements
- Python >3.7. Currently tested up to 3.9.
 
### Unix/Linux/macOS
1. Make sure [Python 3.7](https://www.python.org/) or above is installed (currently tested up to 3.9)
2. In a terminal, run `python -m pip install -r requirements.txt`
3. Start with `python alfred_protocol.py`

### Windows
1. Make sure [Python 3.7](https://www.python.org/) or above is installed
2. In PowerShell, run `py -m pip install -r requirements.txt`
3. If you get an error while installing `pyaudio`, run `pipwin install pyaudio`. pipwin will already be installed from the requirements.
4. To start, run `python alfred_protocol.py`

# Contributing
## Creating a Skill
All skills are stored in the `skills-repository` folder. To make a new skill, create a folder inside the `skills-repository` folder and add a file named `init.py` or give it the same name as your folder. As an example, look at the depiction below. 
```
alfred-protocol
├─ skills_repository
    ├─ your_skill
    │  ├─ your_skill.py
    ├─ your_other_skill
    │   ├─ __init__.py
    ├─ your_single_file_skill.py
```

All skills should inherit from the `AlfredSkill` class. _Check out the example skill, `hello world` for more details._ 
``` py
from skills_repository.alfred_skill import AlfredSkill

class HelloWorld(AlfredSkill):
    name="Hello World"
    
    def __init__(self, alfred_utils):
        """Initialize the Hello World skill class.
            All skills should have an init method which receives
            an instance of AlfredUtils. To find out more about 
            AlfredUtils, read its class file.  

        Args:
            alfred_utils (class): Class holding essential tools, including say(phrase) and listen()
        """
        AlfredSkill.__init__(self)
        self._alfred_utils = alfred_utils


    def initialize_intents(self, register_intent):
        """ registers intents to AlfredProtocol

        Receives: a reference to AlfredProtocol's intent register function
        """
        register_intent(self.handle_say_hello, ["hello", "hello world"], self)

    
    def handle_say_hello(self, phrase):
        """ Makes Alfred Protocol say, "hello world"
        
        Args:
            phrase (string): The phrase said that resulted in this function being called
        """
        self._alfred_utils.say("hello world!")



def create_skill(alfred_utils):
    """ Skill creator function. Creates an instance of your skill to return. 

    Args:
        alfred_utils (AlfredUtils): class instance with essential Alfred tools

    Returns:
        HelloWorld: An instance of the HelloWorld skill
    """
    skill_instance =  HelloWorld(alfred_utils)
    return skill_instance
```

# Backlog
- [ ] Add wakeword activation 🎙️
- [ ] Upgrade intent chooser to intent classification
- [ ] Add skills
- [ ] More voices 🔉
- [ ] More Speech Recognition engines
- [ ] Skills Repository
- [X] Make skills use classes
- [X] Find a way to pass tool functions (speak(), listen(), etc.) to skills

# Recommendations
- Document! More > less. Better > more. 📚
- Test carefully! 🥇
- Be creative! 💡

## Contributors
- [aamott](https://github.com/aamott)
