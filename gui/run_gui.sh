#!/bin/bash
gcc -o gui gui.c `pkg-config --cflags --libs gtk+-3.0`
GSETTINGS_BACKEND=memory ./gui