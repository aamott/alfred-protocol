# Developing Skills
Skills are intended to be an easy way to add functionality. Each skill allows an Assistant to perform a few (or many) related actions, obeying your _intents_. Each action performed is an intent.  

## What is an intent?
This is a concept that loses a lot of people. Basically, an intent is an action you want to perform, and based on data you have already given, the system (or person) decides what they should do - hopefully what you intended.   
Take for example a DJ. You say, "Hey DJ, play something Jazzy!" Your _intent_ is to play Jazz music. He understands this and puts on "Fly Me To The Moon."

### Technical Example
Okay, now that you understand what an _intent_ is in our context, let's look at a pretend skill, `music_player`. Some of its _intent functions_ are `play_song(title)`, `play_by_genre(genre)`, `play_by_artist(name)`, `pause()`, and `resume()`.  
You say, "Hey Alfred, play Moonlight Sonata." It runs your request, "play Moonlight Sonata" through the intent matcher and finds that the closest intent is the one tied to `play_song(title)`. It then calls that function passing in some type of data.  
You then want to pause it, so you say, "Alfred, pause." Your _intent_ is now to stop the music. It matches that to `pause()` and calls it. 

## Hello World
The `hello_world` skill serves as an example skill. It's a good one to copy while you are implementing a new skill. It includes examples of many of the basics. 