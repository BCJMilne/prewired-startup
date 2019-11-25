#!/bin/python3

import ctypes
import sys
import os.path
import platform
from urllib.request import Request, urlopen

wallURL = "https://www.prewired.org/assets/images/prewired-wallpaper_01.jpg"
dir = os.path.dirname(os.path.abspath(__file__))


class Error(Exception):
    """
    Base class for exceptions in this module.
    """
    pass


class OSError(Error):
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

    print("p-startup > Downloading wallpaper from " + wallURL + "... ", end="")
    wallpaper = urlopen(req)
    with open('prewired-wallpaper.jpg', 'wb') as output:
        output.write(wallpaper.read())
    print(" done!")

    print("p-startup > Detecting OS... ", end="")

    if platform.system() == "Linux":
        """ Linux """
        print("Linux detected")
        print("p-startup > Detecting distro... ", end="")
        platTokens = platform.platform().split("-")

        for t in platTokens:
            if(t.lower() == "ubuntu"):
                print("Ubuntu")
                print("p-startup > YET TO IMPLEMENT")
                print("p-startup > Done")
                sys.exit(0)

        raise OSError(platform.platform())

    elif platform.system() == "Windows":
        """ Windows """
        print(" Windows detected")
        print("p-startup > Setting wallpaper... ", end="")
        print(dir + "\\prewired-wallpaper.jpg")
        ctypes.windll.user32.SystemParametersInfoW(
            20, 0, dir+'\\prewired-wallpaper.jpg', 0)
        print("p-startup > Done")
        sys.exit(0)

    elif platform.system() == "Darwin" or platform.system() == "OS X":
        """ OS X """
        raise OSError(platform.system())

    else:
        """ Unknown OS """
        raise OSError(platform.system())

except OSError as e:
    print(" Unsupported OS detected!")
    print(e)
    sys.exit(1)
    raise

finally:
    print("p-startup > Exiting")
