import pyttsx3
import os
engine = pyttsx3.init() 
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                        #printing current volume level
engine.setProperty('volume',1.0) 
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 70) 




engine.say("One lawada is at your doorstep")
engine.runAndWait()


