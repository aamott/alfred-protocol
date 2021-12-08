
import os,sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import basic_functions
def copycat():
    basic_functions.say(basic_functions.transcribe(basic_functions.record(5)))    
if __name__ == '__main__':
    copycat()
