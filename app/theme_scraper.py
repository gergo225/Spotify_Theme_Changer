""" Scraper for the Spicetify Themes from GitHub """
import requests
from bs4 import BeautifulSoup

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

    @property
    def theme_names(self):
        """ The names of the themes (read-only) """
        return self.__theme_names
