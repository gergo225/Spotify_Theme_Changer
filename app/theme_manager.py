""" Manage themes """


class ThemeManager:
    """ Manage theme names and images """

    def __init__(self):
        self.__theme_names = [
            "Adapta Nokto",
            "Arc Dark",
            "Arc Green",
            "Aritim Dark",
            "BIB Green",
            "Bittersweet",
            "Black",
            "Black - Purple",
            "Bloody",
            "BreezeLight",
            "Burnt Sienna",
            "Challenger Deep",
            "Cherry Blossom",
            "Cherry Blossom - Coral",
            "DanDrumStone",
            "DanDrumStoneNew",
            "Dark",
            "Deep Coral",
            "Dobbo",
            "Dracula",
            "Dribbblish",
            "Dribbblish - White",
            "Dribbblish - Dark",
            "Dribbblish - Dracula",
            "Dribbblish - Gruvbox",
            "Dribbblish - Nord Dark",
            "Dribbblish - Nord Light",
            "Dribbblish - Horizon",
            "Dribbblish - Samourai",
            "Dribbblish - Purple",
            "Elementary",
            "Elementary - Blue Contrast",
            "Flatten",
            "Gradianto",
            "Gruvbox Gold",
            "Honne",
            "Jarvis Bot",
            "Kaapi",
            "Kaapi - Gruvbox",
            "Lovelace",
            "Material Ocean",
            "Midnight Light",
            "Moon Child",
            "Night Owl",
            "Night",
            "Night Moon",
            "No Sleep",
            "Nord",
            "One Darkish",
            "Onepunch",
            "Otto",
            "Outrun Dark",
            "Outrun Dark - Dark",
            "Phosphoria",
            "Pop Dark",
            "Shadow Custom",
            "Solarized Dark",
            "Spicy",
            "Sweet",
            "Treky Goldenrod",
            "Twasi",
            "Tycho Awake",
            "VPFut",
            "Vaporwave - New Retro",
            "Vaporwave - Sea Punk",
            "Wintergatan Blueprint",
            "YouTube Dark",
        ]

    @property
    def theme_names(self):
        """ The names of all themes, including the subthemes of each (read-only) """
        return self.__theme_names

    @staticmethod
    def get_theme_code(theme_name):
        """Get the code to apply to spicetify when calling 'current_theme {code}'

        Params
        ------
        theme_name : str
            The name of the theme for which to get the code

        Returns
        -------
        str
            The code to apply to spicetify 'current_theme' attribute
        """
        code = theme_name.replace(" ", "")

        dash_index = code.find("-")
        if dash_index != -1:
            return code[:dash_index]

        return code

    @staticmethod
    def get_color_scheme_code(theme_name):
        """Get the code for the color scheme for this 'theme_name'

        For theme's without multiple color schemes, the code is always 'base'

        Params
        ------
        theme_name : str
            The name of the theme for which to get the color scheme

        Returns
        -------
        str
            The code to apply to spicetify 'color_scheme' attribute
        """
        code = theme_name.replace(" ", "")

        dash_index = code.find("-")
        if dash_index != -1:
            return code[dash_index + 1 :]

        return "base"
