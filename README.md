# DT_VoiceChat

## Purpose
Inspired by Star Trek and a YouTube Video by Part Time Larry (https://www.youtube.com/watch?v=Si0vFx_dJ5Y&list=WL&index=18) I create a short python file which adds a voice frontend to ChatGPT.

## Usage
With the activation-word "Computer" the progamm listens to your voice. Then you can interact with ChatGPT. If your want to finish the conversation, say "conversation end". The programm is then again waiting for the activation-word. To end the program you can then say "program end".

## Installation
1. Just clone the repo onto your computer. 

2. Before you can execute look into the import and download the modules with PIP. I might add a requirement.txt later, but until then you might be required to google the dependencies if some module is missing for you.

3. Create a file mygptkey.py with the following content:
'''
def return_key():
    mykey = 'YOUR_KEY'
    return mykey
'''
    Your ChatGPT key you need to get from the openai website. 

4. Execute the listener python file with "python3 listener.py".


I have tested the file only on MAC. I have not tried to use it on some other device.

Enjoy
