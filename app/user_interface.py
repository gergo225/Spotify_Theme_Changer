""" All UI related stuff """
import wx


class MainFrame(wx.Frame):
    """ The main window of the app """

    def __init__(self):
        super().__init__(parent=None, title="Spotify Theme Changer")
        panel = wx.Panel(self)
        self.Show()


class UserInterface:
    """ The UI part of the app """

    def __init__(self):
        app = wx.App()
        frame = MainFrame()
        app.MainLoop()
