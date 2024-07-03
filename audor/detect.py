import moviepy.editor as mp
import whisper
from better_profanity import profanity
import sys
import json
import re
import torch
import wave
from censor import censor_audio

video_extensions = ['mp4', 'avi', 'mkv', 'mov', 'flv', 'wmv', '.ogv']
audio_extensions = ['mp3', 'wav', 'flac']
file_type_regex = re.compile(r'.*\.(?P<extension>[a-zA-Z0-9]+)$')

def is_video(filename):
    match = file_type_regex.match(filename)
    if match:
        extension = match.group('extension').lower()
        if extension in video_extensions:
            return True
        elif extension in audio_extensions:
            return False
    raise ValueError("File selected does not have a valid audio or video file type. ")

def convert_seconds_to_minutes_and_seconds(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return minutes, seconds

def extract_audio_from_video(video_path, output_audio_path):
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(output_audio_path)

def transcribe_audio(audio_path, model_type):
    model = whisper.load_model(model_type, device="cuda" if torch.cuda.is_available() else "cpu")
    result = model.transcribe(audio_path, word_timestamps=True)
    return result

def scan_for_swear_words(transcription_result):
    segments = transcription_result['segments']
    swear_word_timestamps = []
    time_range = []
    for segment in segments:
        segment_included = False
        for word in segment["words"]:
            text = word['word']
            start_time = word['start']
            end_time = word['end']
            if profanity.contains_profanity(text):
                time_range.append(start_time)
                time_range.append(end_time)
                if not segment_included:
                    swear_word_timestamps.append({
                        'start': start_time,
                        'text': segment['text']
                    })
                    segment_included = True
    return swear_word_timestamps, time_range

def dump_timestamps(swear_word_timestamps):
    filename = 'swear_words.json'
    swear_words = []
    for item in swear_word_timestamps:
        minutes, seconds = convert_seconds_to_minutes_and_seconds(item['start'])
        converted_time = f"{minutes:02d}:{seconds:02d}"
        swear_words.append({converted_time: item['text']}) 

    with open(filename, 'w') as f:
        json.dump(swear_words, f, indent=4)

def create_blank_wav_file():
    n_channels = 1        # mono
    sampwidth = 2         # sample width in bytes
    framerate = 44100     # frame rate (samples per second)
    n_frames = 0          # number of frames (0 for an empty file)

    # Create an empty WAV file  
    output_file = 'censored_audio.wav'
    with wave.open(output_file, 'w') as wav_file:
        wav_file.setnchannels(n_channels)
        wav_file.setsampwidth(sampwidth)
        wav_file.setframerate(framerate)
        wav_file.setnframes(n_frames)


def main(video_or_audio_path, selected_model):
    is_video_file = is_video(video_or_audio_path)
    audio_path = "extracted_audio.wav" if is_video_file else video_or_audio_path
    if is_video_file:
        extract_audio_from_video(video_or_audio_path, audio_path)
    transcription_result = transcribe_audio(audio_path, selected_model)
    swear_word_timestamps, time_range = scan_for_swear_words(transcription_result)
    dump_timestamps(swear_word_timestamps)
    
    create_blank_wav_file()

    result = censor_audio(audio_path, time_range)
    

if __name__ == "__main__":
    create_blank_wav_file()
    if len(sys.argv) != 3:
        print("Usage: python3 detect.py <file_path> <model_type>")
        sys.exit(1)

    video_or_audio_path = sys.argv[1]
    selected_model = sys.argv[2]

    main(video_or_audio_path, selected_model)