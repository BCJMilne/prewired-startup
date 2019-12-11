# prewired-startup
Cross-platform script to set the wallpaper and clear browser data on Prewired attendee devices

## Setup

### Ubuntu

The `prewired-startup.py` script is placed in `/opt` using admin privileges so that it can only be read by the normal user.

The `prewired-startup.service` entry is placed in `/etc/systemd/system/`.

### Windows

`C:\prewired\prewired-startup` is executed by a scheduled task only visible from the `prewired-admin` user. 
