# audor

## Description
Assisted audio censoring tool, designed to make censoring audio for podcasts, videos, etc easier.

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

# Compile the C file
On Linux: gcc -shared -o censor.so -fPIC censor.c
On Windows: gcc -shared -o censor.dll censor.c
On Mac: gcc -shared -o censor.dylib -fPIC censor.c

```

## Usage
Run the program:
```bash
# Run gui_main.py in audor/audor
./gui_main.py
```
Select a video file using the GUI. Next, select the model size (small, medium, or large). 
Run times are lower on smaller models, but their accuracy is worse.

A .json file will be created with the timestamps of profanity.
