from alfred_core import AlfredCore

# SETUP

# Artificial Speech to Text and Text to Speech functions (don't want testing wasting our quotas)
def listen():
    print("LISTENING")
    return "testing phrase"

def say(phrase):
    print("SAYING: ", phrase)

alfred_core = AlfredCore(tts = say, stt = listen)


# RUN TESTS
print("\n\n\n")
# say
try:
    alfred_core.say("What a wonderful world!")
except Exception as e:
    print("FAILED")
    print(e)

print("\n")

# listen
try:
    phrase = alfred_core.listen()
    print(phrase)

except Exception as e:
    print("** FAILED: listen **")
    print(e)

print("\n\n")