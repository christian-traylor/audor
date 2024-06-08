# audor

## Description
Assisted audio censoring tool, designed to make video editor lives easier

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation
Step-by-step instructions on how to install and set up the project.

```bash
# Clone the repository
git clone https://github.com/christian-traylor/audor

# Install dependencies for Python
pip install -r requirements.txt

# Install GTK+ 3.0
This project requires GTK+ 3.0 to be installed. Please ensure that you have GTK+ 3.0 development libraries installed on your system.

Linux: Ensure gtk+-3.0 development libraries are installed via your package manager.
macOS: Install gtk+3 using Homebrew.
Windows: Install GTK+ 3.0 development libraries using MSYS2.

```

## Usage
Compile the program:
```bash
gcc `pkg-config --cflags gtk+-3.0` -o gui gui.c `pkg-config --libs gtk+-3.0`
```
Run the program:
```bash
./gui
```
Select an audio or video file using the GUI. A .json file will be created with the timestamps of profanity.
