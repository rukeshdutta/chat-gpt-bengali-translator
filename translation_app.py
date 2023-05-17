import openai
from gtts import gTTS
from playsound import playsound
import os 
import subprocess
import sys
sys.stdout.reconfigure(encoding='utf-8')

current_file_location = os.path.dirname(os.path.abspath(__file__))
api_file_path = os.path.join(current_file_location,'api_key.txt')
with open(api_file_path, 'r') as file:
    api_key = file.read().strip()


# Configure OpenAI API credentials
openai.api_key = api_key


# Function to translate English sentences to bengali using OpenAI's API
def translate_text(text):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"Translate the following English sentence to Bengali: '{text}'\nEnglish:",
        max_tokens=1000,
        temperature=0.3,
        n=1,
        stop=None,
        logprobs=0
    )
    if response.choices:
        translation = response.choices[0].text.strip()
        return translation
    else:
        return None

# Function to convert text to speech and save it as an audio file
def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='bn')
    tts.save(filename)

# Function to play the audio file
def play_audio(filename):
    subprocess.call(['start', '', filename], shell=True)

# Main function
def main():
    # Input English sentence
    english_sentence = input("Enter an English sentence: ")

    # Translate the English sentence to bengali
    bengali_translation = translate_text(english_sentence)

    if bengali_translation:
        # Output the translated bengali sentence
        print("bengali Translation:", bengali_translation)

        # Save the translated text to a file
        file_path = os.path.join(current_file_location, 'translation.txt')
        with open(file_path, 'w',encoding='utf-8') as file:
            file.write(bengali_translation)
        print("Translation saved to:", file_path)

        # Convert the translated bengali sentence to speech and save it as an audio file
        audio_filename =os.path.join(current_file_location, 'translated_audio.mp3') 
        text_to_speech(bengali_translation, audio_filename)

        # Play the audio file
        play_audio(audio_filename)
    else:
        print("Translation not available.")

if __name__ == '__main__':
    main()

