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
        ├─ init.py
```

All skills should inherit from the `Skills` class. _Check out the example skill, `hello world` for more details._ 
``` py
from skills_repository.alfred_skill import AlfredSkill

# Your skill class
class HelloWorld(AlfredSkill):
    name = "Hello World"
    phrases = ["hello", "hello world"]

    def __init__(self):
        AlfredSkill.__init__(self)
        self.name = "Hello World"

    def run_skill(phrase):
        print("hello world!")

# AlfredProtocol will call create_skill to create the skill. 
# It should register an instance of your skill, like shown.
def register_skill(skill_register_func):
    skill = HelloWorld()
    skill_register_func(skill, skill.phrases)

```

# Rules
- Document! More > less. Better > more. 📚
- Test carefully! 🥇
- Be creative! 💡

## Contributors
- [aamott](https://github.com/aamott)
