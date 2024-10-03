import os
import webbrowser
import datetime


class CommandHandler:
    def open_website(self, query):
        sites = {
            "youtube": "https://www.youtube.com",
            "wikipedia": "https://www.wikipedia.com",
            "google": "https://www.google.com",
            "linkedin": "https://www.linkedin.com/feed/"
        }
        for site in sites:
            if f"open {site}" in query.lower():
                webbrowser.open(sites[site])
                return f"Opening {site} sir."
        return "Error while opening vs code"

    def play_music(self):
        music_path = r"C:\Users\Lenovo\Downloads\RAM SIYA RAM I Adipurush.mp3"  # Adjust the path
        os.startfile(music_path)

    def tell_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M")
        return f"Sir, the time is {current_time}."

    def open_vscode(self):
        vscode_path = r"D:\Microsoft VS Code\Code.exe"  # Adjust the path
        os.startfile(vscode_path)
