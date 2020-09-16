""" All Spicetify related stuff """
import subprocess


class SpicetifyClient:
    """ A class that handles Spicetify functionality """

    def __init__(self):
        if not self.spicetify_is_installed():
            self.install_spicetify()

    def spicetify_is_installed(self):
        """Checks if Spicetify is already installed or not and
        returns a boolean value"""
        output = subprocess.run( # pylint: disable=subprocess-run-check
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
