# Orange Pi Compute Module 4 NAS Double Deck Fan Script

This script is designed to run the cooling fan on a [Waveshare NAS All-In-One Mini-Computer](https://www.waveshare.com/cm4-nas-double-deck-c4a.htm) when running [Orange Pi Compute Module 4](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-CM4-1.html)

## Prerequisites

This script need [WiringOp](https://github.com/orangepi-xunlong/wiringOP) & [WiringOp-Python](https://github.com/orangepi-xunlong/wiringOP-Python) to be installed. See `Orange Pi CM4` [user manual](https://drive.google.com/drive/folders/1f_XwACtcFUyP_dyhmUTRuH9v4X_jJk5I) for installation instructions (chapter 3.15, 3.17).

## Run

```shell
python3 main.py
```

## Autostart

Edit file `/etc/rc.local`. Add before line with `exit 0`command:

```shell
python3 /home/orangepi/fan/main.py
```

Change `/home/orangepi/fan/main.py` to actual absolute path to file `main.py`

