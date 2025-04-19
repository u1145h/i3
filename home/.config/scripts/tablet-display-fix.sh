#!/bin/bash

# Set custom 1440x900 resolution for VNC display
xrandr --newmode "1440x900_60.00" 106.50 1440 1520 1672 1904 900 903 909 934 -hsync +vsync
xrandr --addmode VNC-0 "1440x900_60.00"
xrandr --output VNC-0 --mode "1440x900_60.00"

