# import pyjokes

# print("Printing Jokes")
# joke = pyjokes.get_joke()
# print(joke)

# 🐍 Python Modules Installation Commands (pip ke through)
# 1️⃣ math

# Note: Ye built-in module hai, install karne ki zarurat nahi

# 2️⃣ random

# Built-in, install ki zarurat nahi

# 3️⃣ datetime

# Built-in, install ki zarurat nahi

# 4️⃣ os

# Built-in, install ki zarurat nahi

# 5️⃣ sys

# Built-in, install ki zarurat nahi

# 6️⃣ time

# Built-in, install ki zarurat nahi

# 7️⃣ json

# Built-in, install ki zarurat nahi

# 8️⃣ csv

# Built-in, install ki zarurat nahi

# 9️⃣ re

# Built-in, install ki zarurat nahi

# 🔟 requests
# pip install requests

# 1️⃣1️⃣ pyjokes
# pip install pyjokes

# 1️⃣2️⃣ flask
# pip install flask

# 1️⃣3️⃣ pandas
# pip install pandas

# 1️⃣4️⃣ numpy
# pip install numpy

# 1️⃣5️⃣ matplotlib
# pip install matplotlib

# 1️⃣6️⃣ beautifulsoup4
# pip install beautifulsoup4

# 1️⃣7️⃣ pygame
# pip install pygame

# pyttsx3
# pip install pyttsx3

# SpeechRecognition 3.14.4
# pip install SpeechRecognition

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("""Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the traveler in the dark
# Thanks you for your tiny spark,
# How could he see where to go,
# If you did not twinkle so?

# In the dark blue sky you keep,
# Often through my curtains peep
# For you never shut your eye,
# Till the sun is in the sky.

# As your bright and tiny spark
# Lights the traveler in the dark,
# Though I know not what you are,
# Twinkle, twinkle, little star.
# """)
# engine.runAndWait()




import os

# specify the directory you want to list
directory_path = "C:/Users/Wajiz.pk/OneDrive/Desktop/Python-course"

# get list of all files and folders
contents = os.listdir(directory_path)

# print each item
for item in contents:
    print(item)
