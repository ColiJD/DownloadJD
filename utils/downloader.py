import yt_dlp
import urllib.parse
import re
import wx
import os
import pandas as pd

# Definir la ruta base y las subcarpetas
DOWNLOAD_FOLDER = r"C:\AYVdownload"  # Ruta absoluta en Windows
VIDEOS_FOLDER = os.path.join(DOWNLOAD_FOLDER, "videos")  # Subcarpeta para videos
AUDIOS_FOLDER = os.path.join(DOWNLOAD_FOLDER, "audios")  # Subcarpeta para audios

# Crear las carpetas si no existen
os.makedirs(VIDEOS_FOLDER, exist_ok=True)
os.makedirs(AUDIOS_FOLDER, exist_ok=True)

# Crear las carpetas si no existen
os.makedirs(VIDEOS_FOLDER, exist_ok=True)
os.makedirs(AUDIOS_FOLDER, exist_ok=True)


class YouTubeDownloader:
    def __init__(self, log_text, progress_bar):
        self.log_text = log_text
        self.progress_bar = progress_bar

    def clean_url(self, link):
        parsed_url = urllib.parse.urlparse(link)
        clean_url = parsed_url._replace(query='').geturl()
        return clean_url

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            percent_str = re.sub(r'\x1b\[[0-9;]*m', '', d['_percent_str'])
            progress = float(percent_str.strip('%'))
            wx.CallAfter(self.progress_bar.SetValue, int(progress))
        elif d['status'] == 'finished':
            wx.CallAfter(self.progress_bar.SetValue, 100)

    def download_video(self, link, download_type):
        if download_type == 'video':
            ydl_opts = {
                'format': "bestvideo[ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                'outtmpl': os.path.join(VIDEOS_FOLDER, '%(title)s.%(ext)s'),
                'progress_hooks': [lambda d: self.progress_hook(d)],
            }
        elif download_type == 'audio':
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(AUDIOS_FOLDER, '%(title)s.%(ext)s'),  # Guardar en la carpeta de audios
                'extractaudio': True,
                'audioformat': 'mp3',
                'progress_hooks': [lambda d: self.progress_hook(d)],
            }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            wx.CallAfter(self.log_text.AppendText, f"Descarga completada: {link}\n")
        except Exception as e:
            wx.CallAfter(self.log_text.AppendText, f"Error durante la descarga de {link}: {str(e)}\n")

    def download_single_video(self, link, download_type):
        clean_link = self.clean_url(link)
        self.download_video(clean_link, download_type)

    def download_multiple_videos_from_excel(self, file_path, download_type):
        try:
            df = pd.read_excel(file_path)
            links = df.iloc[:, 0].dropna().tolist()
            for link in links:
                clean_link = self.clean_url(link)
                wx.CallAfter(self.log_text.AppendText, f"Descargando: {clean_link}\n")
                self.download_video(clean_link, download_type)
        except Exception as e:
            wx.CallAfter(self.log_text.AppendText, f"Error al procesar el archivo de Excel: {str(e)}\n")