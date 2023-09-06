from sys import argv
import colorama


class Ls:
    """
    A complete reproduction of the ls library.
    It is built in a way that is cross-platform
    """

    def __init__(self, enable_colours: bool = True) -> None:
        # ---- The colours ----
        self.colours = self.colors = {
            "default": "",
            "white": "\x1b[01;37m",
            "gray": "\x1b[00;37m",
            "purple": "\x1b[00;35m",
            "cyan": "\x1b[01;36m",
            "green": "\x1b[01;32m",
            "red": "\x1b[01;05;37;41m"
        }
        # ---- user entry ----
        self.usr_entry = ""
        # ---- Toggle options ----
        self.enable_colours = enable_colours
        self.selected_options = {
            "1": False,  # One column output
            "a": False,  # Include names starting with .
            "-A": False,  # Like -a, but exclude . and ..
            "-x": False,  # List by lines
            "-d": False,  # List directory names, not contents
            "-L": False,  # Follow symlinks
            "-H": False,  # Follow symlinks on command line
            "-R": False,  # Recurse
            "-p": False,  # Append / to directory names
            "-F": False,  # Append indicator (one of */=@|) to names
            "-l": False,  # Long format
            "-i": False,  # List inode numbers
            "-n": False,  # List numeric UIDs and GIDs instead of names
            "-s": False,  # List allocated blocks
            "-lc": False,  # List ctime
            "-lu": False,  # List atime
            "--full-time": False,  # List full date/time
            "-h": False,  # Human readable sizes (1K 243M 2G)
            "--group-directories-first": False,
            "-S": False,  # Sort by size
            "-X": False,  # Sort by extension
            "-v": False,  # Sort by version
            "-t": False,  # Sort by mtime
            "-tc": False,  # Sort by ctime
            "-tu": False,  # Sort by atime
            "-r": False,  # Reverse sort order
            "-w": False,          # N    Format N columns wide
        }
