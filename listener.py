import mygptkey
import speech_recognition as sr
import openai
import os
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# 1. The listing needs to start and never stop.
# 2. Once the wakeup word is said, the conversation starts and is not stopped.
# 3. After the response is given, the program needs to wait for new query.
# 4. The "conversation end" keyword put the computer back in listening mode.  

# Here we need a method to record and write and transcribe the wav file
messages = [{"role": "system", "content": 'You are my assistant. Answer in 25 words or less.'}]

def record(recog, source):
    text = ''

    print("Step 3: Record inquery")
    try:
        audio = recog.listen(source, timeout=10, phrase_time_limit = 15)
        print("Step 4: Write file")
        # Save voice recording to a WAV file
        with open("recording.wav", "wb") as f:
            f.write(audio.get_wav_data())

        # Transcribe audio to text
        with sr.AudioFile("recording.wav") as source:
            audio = r.record(source)
            text = r.recognize_google(audio)
            print("Step 5: Transcribed text: " + text)
    except:
        pass
    
    return text

# Method to start the conversation returning the response as text.
def conversation(text):
    # Send text to ChatGPT using the OpenAI API
    global messages

    messages.append({"role": "user", "content": text})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    # Define the input text to be spoken
    response_text = response['choices'][0]['message']
    messages.append(response_text)
    print(messages)

    mytts(response_text['content'])

    return response_text

def mytts(input):
    tts = gTTS(text=input, lang='en-us')
    tts.save("output.mp3")

    # Play the MP3 file
    os.system("afplay output.mp3")

# Define the keyword to listen for
keyphrase = "computer"

# Set up the recognizer object which recognizes the voice.
# r = sr.Recognizer()

# Load the sound file
beep_path = os.path.join(os.getcwd(), "beep.wav")
sound = AudioSegment.from_wav(beep_path)

# Get OpenAI API credentials from another file where i store my key.
openai.api_key = mygptkey.return_key

# Start listening for audio input
with sr.Microphone() as source:
    while True:
        # Set up the recognizer object which recognizes the voice.
        r = sr.Recognizer()
        audio = r.listen(source)
        # Try to recognize the keyword
        try:
            # get the sound input as text from the recognizer.
            text = r.recognize_google(audio)
            print("Step 1: the key word is " + text) 

            # Once the key word is recognized, 
            if text.lower() == keyphrase:
                # Play the sound prompt. 
                print("Step 2: We have said the key word")
                play(sound)
    
                # The conversation with ChatGPT needs to happen here.
                while True:
                    
                    input_text = record(r, source)
                
                    print('The text is ' + input_text)

                    if input_text.lower() == "conversation end":
                        mytts("ending conversation")
                        break
                    else:
                        # Call method to
                    
                        conversation(input_text)
                    
                    print("Continue conversation:")  

                # Check for end conversation
                #print("End Converation?")
                #audio2 = r.listen(source)
                #text2 = r.recognize_google(audio2)
                #if text2.lower() == "end":
                #    print("Ending Converation")


            elif text.lower() == "program end":
                mytts("ending progamm")
                print("Ending Programm")
                break

        except sr.UnknownValueError:
            pass

        #resetting the recognizer         
        r = ''
#        mytts('You can ask me anything by using the keyword computer')
    
