import asyncio
from avi_ai import AviAI
from speech_recognition import Recognizer, Microphone
from commands import CommandHandler
from light import light_on, light_off


class SpeechRecognizer:
    def __init__(self):
        self.recognizer = Recognizer()

    def recognize_speech(self):
        with Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                print("Recognizing....")
                query = self.recognizer.recognize_google(audio, language="en-IN")
                print(f"User said: {query}")
                return query
            except Exception as e:
                print("Could not understand audio")
                return None


async def main():
    ai = AviAI()
    recognizer = SpeechRecognizer()
    command_handler = CommandHandler()

    while True:
        query = recognizer.recognize_speech()
        if query is None:
            continue

        if "exit" in query.lower():
            await ai.speak("Goodbye!")
            break

        if "vs code" in query.lower():
            command_handler.open_vscode()
            await ai.speak("Opening VS Code.")
        elif "open" in query.lower():
            open_response = command_handler.open_website(query)
            await ai.speak(open_response)
        elif "play music" in query.lower():
            command_handler.play_music()
            await ai.speak("Playing music.")
        elif "the time" in query.lower():
            time_response = command_handler.tell_time()
            await ai.speak(time_response)
        elif "light on" in query.lower() or "turn on light" in query.lower():
            if light_on():
                await ai.speak("Light is on.")
            else:
                await ai.speak("Light is not connected.")
        elif "light off" in query.lower() or "turn off light" in query.lower():
            if light_off():
                await ai.speak("Light is off.")
            else:
                await ai.speak("Light is not connected.")
        else:
            response = ai.get_response(query)
            print(f"AI: {response}")
            await ai.speak(response)


if __name__ == "__main__":
    asyncio.run(main())
