""" All Spicetify related stuff """
import subprocess
import os
import zipfile
from app.theme_manager import ThemeManager


class SpicetifyClient:
    """ A class that handles Spicetify functionality """

    def __init__(self):
        if not self.spicetify_is_installed():
            self.install_spicetify()
        if not os.listdir(
            os.path.join(os.getenv("USERPROFILE"), ".spicetify", "Themes")
        ):
            self.install_themes()

    def spicetify_is_installed(self):
        """Checks if Spicetify is already installed or not and
        returns a boolean value"""
        output = subprocess.run(  # pylint: disable=subprocess-run-check
            ["powershell", "spicetify", "--help"], capture_output=True
        )
        return not output.returncode

    def install_spicetify(self):
        """Installs Spicetify using PowerShell (Windows).

        This is called when Spicetify is not already installed"""
        subprocess.run(
            [
                "powershell",
                "Invoke-WebRequest",
                "-UseBasicParsing",
                "https://raw.githubusercontent.com/khanhas/spicetify-cli/master/install.ps1",
                "|",
                "Invoke-Expression",
            ],
            check=True,
        )
        subprocess.run(["spicetify"], check=True)
        subprocess.run(["spicetify", "backup", "apply"], check=True)
        # Only for developers
        # subprocess.run(["spicetify", "enable-devtool"], check=True)

    def install_themes(self):
        """Extracts the themes.zip containing all themes to the 'Themes'
        directory in the installed spicetify folder"""
        themes_zip = os.path.join(os.getcwd(), "app", "Themes.zip")

        user_profile = os.getenv("USERPROFILE")
        spicetify_themes_folder = os.path.join(user_profile, ".spicetify", "Themes")

        with zipfile.ZipFile(themes_zip, "r") as zip_file:
            zip_file.extractall(spicetify_themes_folder)

    def apply_theme(self, theme_name):
        """Apply the theme named 'theme_name'. This must be
        from the theme names list (in ThemeManager)"""
        theme = ThemeManager.get_theme_code(theme_name)
        color_scheme = ThemeManager.get_color_scheme_code(theme_name)

        subprocess.run(
            [
                "spicetify",
                "config",
                "current_theme",
                theme,
                "color_scheme",
                color_scheme,
            ],
            check=True,
        )
        subprocess.run(["spicetify", "apply"], check=True)
