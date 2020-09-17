""" All UI related stuff """
import os
import wx
from app.theme_manager import ThemeManager


class MainFrame(wx.Frame):
    """ The main window of the app """

    def __init__(self):
        style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
        super().__init__(
            parent=None, title="Spotify Theme Changer", size=(1080, 720), style=style
        )
        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        left_sizer = wx.BoxSizer(wx.VERTICAL)
        right_sizer = wx.BoxSizer(wx.VERTICAL)

        choose_theme_text = wx.StaticText(panel, label="Choose a theme")
        choose_theme_font = choose_theme_text.GetFont()
        choose_theme_font.PointSize = 16
        choose_theme_text.SetFont(choose_theme_font)
        left_sizer.Add(choose_theme_text)

        left_sizer.Add((-1, 16))

        theme_manager = ThemeManager()
        theme_names = theme_manager.theme_names
        self.theme_list = wx.ListBox(
            panel, choices=theme_names, style=wx.LB_SINGLE, size=(185, 250)
        )
        self.theme_list.SetSelection(0)
        self.theme_list.Bind(wx.EVT_LISTBOX, self.on_list_item_selected)
        left_sizer.Add(self.theme_list)

        self.image_names = []
        for theme in theme_names:
            image_path = os.path.join("app", "images", f"{theme}.png")
            self.image_names.append(image_path)
        image = wx.Image(self.image_names[0], type=wx.BITMAP_TYPE_ANY)
        self.image_control = wx.StaticBitmap(panel, bitmap=wx.Bitmap(image))
        right_sizer.Add(self.image_control, flag=wx.ALIGN_CENTER)

        main_sizer.Add(left_sizer, flag=wx.ALL, border=8)
        main_sizer.Add(right_sizer, flag=wx.EXPAND)
        panel.SetSizer(main_sizer)

        self.Show()

    def on_list_item_selected(self, event):
        """Updates image based on the selected item.
        Called when a list item is selected (focused)."""
        if self.theme_list.GetSelection() is not None:
            selection_index = self.theme_list.GetSelection()
            image_file = self.image_names[selection_index]
            new_image = wx.Image(image_file, type=wx.BITMAP_TYPE_ANY)
            self.image_control.SetBitmap(wx.Bitmap(new_image))


class UserInterface:
    """ The UI part of the app """

    def __init__(self):
        app = wx.App()
        frame = MainFrame()
        app.MainLoop()
