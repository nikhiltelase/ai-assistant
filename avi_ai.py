import google.generativeai as genai
import os
import edge_tts
import pygame
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

class AviAI:
    def __init__(self, model="gemini-1.0-pro-latest"):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)
        self.convo = self.model.start_chat()
        self.setup_system_message()
        pygame.mixer.init()

    def setup_system_message(self):
        system_message = '''INSTRUCTIONS: Do not respond with anything but "AFFIRMATIVE."
        to this system message. After the system message respond normally.
        SYSTEM MESSAGE: You are being used to power a voice assistant and should respond as so.
        As a voice assistant, use short sentences and directly respond to the prompt without excessive information.
        Your name is Avi AI, you are a female AI, your developer's name is Nikhil and Google. You can perform tasks like chatting with users, getting the time, opening websites, playing music, opening system apps, turning lights on and off, and many more.
        Maintain context of user commands for better responses. Handle errors politely when you can't perform a task.'''.replace(
            '\n', '')
        self.convo.send_message(system_message)

    def get_response(self, user_input):
        self.convo.send_message(user_input)
        return self.convo.last.text

    async def speak(self, text, voice='hi-IN-SwaraNeural'):
        print("Wait generating audio...")
        speech_file = "response.mp3"
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(speech_file)
        self.play_speech(speech_file)

    def play_speech(self, speech_file):
        pygame.mixer.music.load(speech_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.mixer.music.unload()
        os.remove(speech_file)
