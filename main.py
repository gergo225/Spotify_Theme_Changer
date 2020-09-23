""" Main file """
from app.user_interface import UserInterface
from app.spicetify_client import SpicetifyClient

if __name__ == "__main__":
    spicetify = SpicetifyClient()
    ui = UserInterface()
