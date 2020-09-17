""" A file for spicetify utilities """
import os


class SpicetifyUtils:
    """A class which provides utilities related to spicetify

    Does NOT communicate with the spicetify command"""

    @staticmethod
    def themes_folder():
        """ The path of the spicetify 'Themes' folder (read-only) """
        return os.path.join(os.environ["USERPROFILE"], ".spicetify", "Themes")
