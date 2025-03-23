import wx
from utils.constants import COLOR_BACKGROUND,COLOR_ERROR,COLOR_PRIMARY,COLOR_SECONDARY,COLOR_SUCCESS,COLOR_TEXT
from utils.downloader import YouTubeDownloader
import os
from threading import Thread

class YouTubeDownloaderApp(wx.Frame):
    def __init__(self, *args, **kw):
        super(YouTubeDownloaderApp, self).__init__(*args, **kw)

        self.InitUI()
        self.SetSize((700, 500))
        self.SetTitle("Descargador de YouTube")
        self.SetBackgroundColour(COLOR_BACKGROUND)
        self.Centre()

    def InitUI(self):
        panel = wx.Panel(self)
        panel.SetBackgroundColour(COLOR_BACKGROUND)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Título de la aplicación
        title = wx.StaticText(panel, label="Descargador de YouTube", style=wx.ALIGN_CENTER)
        title.SetFont(wx.Font(20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        title.SetForegroundColour(COLOR_TEXT)
        vbox.Add(title, flag=wx.ALIGN_CENTER | wx.TOP, border=25)
        vbox.Add(wx.StaticText(panel, label="Los archivos se guardarán en C:\\AYVdownload"), flag=wx.LEFT | wx.TOP, border=25)

        # Tipo de descarga (Video o Audio)
        self.download_type = wx.RadioBox(panel, label="Tipo de descarga", choices=["Audio","Video"], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.download_type.SetBackgroundColour(COLOR_BACKGROUND)
        self.download_type.SetForegroundColour(COLOR_TEXT)
        vbox.Add(self.download_type, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=25)

        # Campo para ingresar un enlace manualmente
        vbox.Add(wx.StaticText(panel, label="Ingrese el link del video de YouTube:"), flag=wx.LEFT| wx.TOP, border=25)
        self.manual_link = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        self.manual_link.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.manual_link.SetForegroundColour(COLOR_TEXT)
        vbox.Add(self.manual_link, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=25)

        # Botón para descargar manualmente
        btn_download_manual = wx.Button(panel, label="Descargar manualmente")
        btn_download_manual.SetBackgroundColour(COLOR_PRIMARY)
        btn_download_manual.SetForegroundColour(wx.Colour(0, 0, 0))
        btn_download_manual.Bind(wx.EVT_BUTTON, self.OnDownloadManual)
        vbox.Add(btn_download_manual, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=25)

        # Campo para cargar un archivo de Excel
        vbox.Add(wx.StaticText(panel, label="Cargue un archivo de Excel con enlaces de YouTube:"), flag=wx.LEFT | wx.TOP, border=25)
        self.file_picker = wx.FilePickerCtrl(panel, message="Seleccione un archivo de Excel", wildcard="Excel files (*.xlsx;*.xls)|*.xlsx;*.xls")
        self.file_picker.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.file_picker.SetForegroundColour(COLOR_TEXT)
        vbox.Add(self.file_picker, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=25)

        # Botón para descargar desde Excel
        btn_download_excel = wx.Button(panel, label="Descargar desde Excel")
        btn_download_excel.SetBackgroundColour(COLOR_PRIMARY)
        btn_download_excel.SetForegroundColour(wx.Colour(0,0,0))
        btn_download_excel.Bind(wx.EVT_BUTTON, self.OnDownloadExcel)
        vbox.Add(btn_download_excel, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=25)

        # Barra de progreso
        self.progress_bar = wx.Gauge(panel, range=100)
        self.progress_bar.SetBackgroundColour(COLOR_BACKGROUND)
        self.progress_bar.SetForegroundColour(COLOR_PRIMARY)
        vbox.Add(self.progress_bar, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=25)

        # Área de registro
        self.log_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.log_text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.log_text.SetForegroundColour(COLOR_TEXT)
        vbox.Add(self.log_text, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=25)

        panel.SetSizer(vbox)

        self.downloader = YouTubeDownloader(self.log_text, self.progress_bar)
        

    def OnDownloadManual(self, event):
        link = self.manual_link.GetValue()
        if link:
            download_type = "video" if self.download_type.GetSelection() == 1 else "audio"
            self.log_text.AppendText(f"Descargando: {link}\n")
            Thread(target=self.downloader.download_single_video, args=(link, download_type)).start()
        else:
            wx.MessageBox("Por favor, ingrese un link válido.", "Error", wx.OK | wx.ICON_ERROR)

    def OnDownloadExcel(self, event):
        file_path = self.file_picker.GetPath()
        if os.path.exists(file_path):
            download_type = "video" if self.download_type.GetSelection() == 1 else "audio"
            self.log_text.AppendText(f"Procesando archivo: {file_path}\n")
            Thread(target=self.downloader.download_multiple_videos_from_excel, args=(file_path, download_type)).start()
        else:
            wx.MessageBox("Por favor, seleccione un archivo válido.", "Error", wx.OK | wx.ICON_ERROR)