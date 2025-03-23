
import wx
from utils.gui import YouTubeDownloaderApp

def main():
    app = wx.App(False)
    frame = YouTubeDownloaderApp(None)
    frame.Show(True)
    app.MainLoop()

if __name__ == "__main__":
    main()