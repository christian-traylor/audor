# audor

## Description
Assisted audio censoring tool, designed to make censoring audio for podcasts, videos, etc easier.

## Table of Contents
- [System Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Requirements
[OpenAI Whisper](https://github.com/openai/whisper#setup) should be installed. For Whisper, ffmpeg is required and sometimes a Rust install is required.

System requirements:
For system capabilities, a minimum of 2GB of VRAM is required. As always, a more powerful computer will enhance your experience significantly. Substantial improvements to performance can be seen with GPU acceleration.



## Installation
Step-by-step instructions on how to install and set up the project.

```bash
# Clone the repository
git clone https://github.com/christian-traylor/audor

# Install dependencies for Python
pip install -r requirements.txt

# Compile the C file in audor/audor
On Linux: gcc -shared -o censor_audio.so -fPIC censor_audio.c
On Windows: gcc -shared -o censor_audio.dll censor_audio.c
On Mac: gcc -shared -o censor_audio.dylib -fPIC censor_audio.c

```

## Usage
Run the program:
```bash
# Run gui_main.py in audor/audor
./gui_main.py
```
Select a video file using the GUI. Next, select the model size (small, medium, or large). 
Run times are lower on smaller models, but their accuracy is worse.

A .json file will be created with the timestamps of profanity and a new audio file without profanity will be created
