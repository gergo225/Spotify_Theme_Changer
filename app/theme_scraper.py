""" Scraper for the Spicetify Themes from GitHub """
import os
import requests
from bs4 import BeautifulSoup
from app.spicetify_utils import SpicetifyUtils

THEMES_REPO = "https://github.com/morpheusthewhite/spicetify-themes/tree/master/"


class ThemeScraper:
    """ Handles scraping the spicetify themes from GitHub """

    def __init__(self):
        themes_html = requests.get(THEMES_REPO).text
        soup = BeautifulSoup(themes_html, "html.parser")
        theme_html = soup.find_all(role="row")

        del theme_html[0]  # deletes the first item, which is not a theme
        # this deletes the last 4 items which are files, not theme folders
        del theme_html[-4:]

        self.__theme_names = [theme.find("a").text for theme in theme_html]

        self.get_theme_files()

    def get_theme_files(self):
        r"""Downloads the user.css and color.ini files for all themes.
        All themes are in their own separate folders.

        The download directory is '{userprofile}\\\.spicetify\\Themes' (Windows)

        If theme folders already exist, don't install them"""
        themes_path = SpicetifyUtils.themes_folder()
        if not os.listdir(themes_path):
            for theme in self.theme_names:
                theme_dir = os.path.join(themes_path, theme)
                os.mkdir(theme_dir)
                self.download_github_theme_file(theme=theme, file_name="user.css")
                self.download_github_theme_file(theme=theme, file_name="color.ini")
        else:
            print("Themes are already installed")

    def download_github_theme_file(self, theme, file_name):
        """Save a theme file from it's GitHub directory to the corresponding local
        theme folder in the spicetify themes

        Theme files are: user.css, color.ini

        Params
        ------
        theme : str
            The name of the theme for which to download a file.
            This is also the name of the folder in the 'Themes' folder in which
            the downloaded file will be saved.

        file : str
            Name of the file which to download.
            Main files are 'user.css' and 'color.ini'
        """
        github_path = (
            "https://raw.githubusercontent.com/morpheusthewhite"
            f"/spicetify-themes/master/{theme}/{file_name}"
        )
        file_html = requests.get(github_path).text
        soup = BeautifulSoup(file_html, "html.parser")

        theme_dir = os.path.join(SpicetifyUtils.themes_folder(), theme)
        file_path = os.path.join(theme_dir, file_name)

        if soup.text != "404: Not Found":
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(soup.text)

    @property
    def theme_names(self):
        """ The names of the themes (read-only) """
        return self.__theme_names
