#!/bin/python3

import ctypes
import sys
import os.path
import platform
import shutil
from urllib.request import Request, urlopen

wallURL = "https://www.prewired.org/assets/images/prewired-wallpaper_01.jpg"
dir = os.path.dirname(os.path.abspath(__file__))


class Error(Exception):
    """
    Base class for exceptions in this module.
    """
    pass


class UnknownOSError(Error):
    """
    Raised when an unknown or unsupported operating system
    is detected
    """

    def __init__(self, message):
        self.message = message


try:

    hdr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    req = Request(wallURL)
    req.add_header(
        'Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    req.add_header('User-Agent', 'Prewired Startup Utility')

    print("psu > Downloading wallpaper from " + wallURL + "... ", end="")
    wallpaper = urlopen(req)
    with open('prewired-wallpaper.jpg', 'wb') as output:
        output.write(wallpaper.read())
    print(" done!")

    print("psu > Detecting OS... ", end="")

    if platform.system() == "Linux":
        """ Linux """

        print("Linux detected")
        print("psu > Detecting distro... ", end="")
        platTokens = platform.platform().split("-")

        for t in platTokens:
            if(t.lower() == "ubuntu"):
                print("Ubuntu, assuming Gnome")
                print("psu > Setting wallpaper... ", end="")
                exec('gsettings set org.gnome.desktop.background picture-uri "' +
                     dir + '/prewired-wallpaper.jpg"')
                print("done")
                print("Clearing Mozilla data... ", end="")
                if(os.path.isdir("/home/prewired/.mozilla")):
                    shutil.rmtree("/home/prewired/.mozilla")
                print("done")
                sys.exit(0)

            if(t.lower() == "fedora"):
                print("Fedora")
                print("psu > Cannot set wallpaper")

        raise UnknownOSError(platform.platform())

    elif platform.system() == "Windows":
        """ Windows """

        print(" Windows detected")
        print("psu > Setting wallpaper... ", end="")
        ctypes.windll.user32.SystemParametersInfoW(
            20, 0, dir+'\\prewired-wallpaper.jpg', 0)
        print("done")

        print("psu > Clearing Mozilla data... ", end="")
        if(os.path.isdir("C:\\Users\\prewired-attendee\\AppData\\Roaming\\Mozilla\\Firefox")):
            shutil.rmtree("C:\\Users\\prewired-attendee\\AppData\\Roaming\\Mozilla\\Firefox")
        print("done")

        print("psu > Clearing Chrome data... ", end="")
        if(os.path.isdir("C:\\Users\\prewired-attendee\\AppData\\Local\\Google\\Chrome\\User Data")):
            shutil.rmtree("C:\\Users\\prewired-attendee\\AppData\\Local\\Google\\Chrome\\User Data")
        print("done")

        sys.exit(0)

    elif platform.system() == "Darwin" or platform.system() == "OS X":
        """ OS X """
        raise UnknownOSError(platform.system())

    else:
        """ Unknown OS """
        raise UnknownOSError(platform.system())

except UnknownOSError as e:
    print("Unsupported OS detected!")
    print(e)
    sys.exit(1)
    raise

finally:
    print("psu > Exiting")
