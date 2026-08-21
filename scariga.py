import os
import yt_dlp

# Trova la cartella corrente in cui gira lo script
current_dir = os.path.dirname(os.path.abspath(__file__))
cookie_path = os.path.join(current_dir, 'youtube-cookies.txt')

ydl_opts = {
    'cookiefile': cookie_path,
    'noplaylist': True,
    # Specifica dove salvare il video sul server (es. nella cartella corrente)
    'outtmpl': os.path.join(current_dir, '%(title)s.%(ext)s'), 
}

url = "https://youtube.com"

print("Avvio il download su PythonAnywhere...")
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
print("Download completato!")
