# Importing the required module for text
# to speech

# First istalled gTTS using Pip install gTTS 
# in the terminal

from gtts import gTTS
import os

# The text that you is going to be converted to speech
myText = 'Hello, I am a robot.'

# Choose the language to convert to
lanaguage = 'en'

# 
myObject = gTTS(text=myText, lang=lanaguage, slow=False)

# This saves the converted audio in a mp3 file
myObject.save("robotgreeting.mp3")

# Playing the converted file using os
os.system("mpg321 robotgreeting.mp3")


