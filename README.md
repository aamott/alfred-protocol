# alfred-protocol
A voice assistant built as an educational project with the [Society of Artificial Intelligence](https://sai-byui.github.io/) at BYU - Idaho with a focus on clarity, simplicity, and extensibility.

# Install
### Unix/Linux/macOS
1. Make sure [Python 3.7](https://www.python.org/) or above is installed
2. In a terminal, run `python -m pip install -r requirements.txt`

### Windows
1. Make sure [Python 3.7](https://www.python.org/) or above is installed
2. In PowerShell, run `py -m pip install -r requirements.txt`
3. To start, run `python alfred_protocol.py`

# Contribute
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
    
    def __init__(self, alfred_core):
        """Initialize the Hello World skill class.
            All skills should have an init method which receives
            an instance of AlfredCore. To find out more about 
            AlfredCore, read its class file.  

        Args:
            alfred_core (class): Class holding essential tools, including say(phrase) and listen()
        """
        AlfredSkill.__init__(self)
        self._alfred_core = alfred_core


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
        self._alfred_core.say("hello world!")



def create_skill(alfred_core):
    """ Skill creator function. Creates an instance of your skill to return. 

    Args:
        alfred_core (AlfredCore): class instance with essential Alfred tools

    Returns:
        HelloWorld: An instance of the HelloWorld skill
    """
    skill_instance =  HelloWorld(alfred_core)
    return skill_instance
```

# To-Do
- [ ] Add wakeword activation 🎙️
- [ ] Add more skills!
- [X] Find a way to pass tool functions (speak(), listen(), etc.) to skills
- [ ] Upgrade intent matcher from phrase matching to regex then intent matching
- [X] Make skills use classes

# Rules
- Document! More > less. Better > more. 📚
- Test carefully! 🥇
- Be creative! 💡

## Contributors
- [aamott](https://github.com/aamott)
