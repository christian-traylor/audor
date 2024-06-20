import moviepy.editor as mp
import whisper
from better_profanity import profanity
import os
import sys
import json


def convert_seconds_to_minutes_seconds(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return minutes, seconds

def extract_audio_from_video(video_path, output_audio_path):
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(output_audio_path)

def transcribe_audio(audio_path, model_type="base"):
    model = whisper.load_model(model_type)
    result = model.transcribe(audio_path)
    return result

def scan_for_swear_words(transcription_result):
    segments = transcription_result['segments']
    swear_word_timestamps = []
    for segment in segments:
        text = segment['text']
        start_time = segment['start']
        if profanity.contains_profanity(text):
            swear_word_timestamps.append({
                'start': start_time,
                'text': text
            })
    return swear_word_timestamps

def main(video_path):
    audio_path = "extracted_audio.wav"
    extract_audio_from_video(video_path, audio_path)
    transcription_result = transcribe_audio(audio_path)
    swear_word_timestamps = scan_for_swear_words(transcription_result)

    swear_words = []
    for item in swear_word_timestamps:
        minutes, seconds = convert_seconds_to_minutes_seconds(item['start'])
        converted_time = f"{minutes:02d}:{seconds:02d}"
        swear_words.append({converted_time: item['text']}) 

    with open('swear_words.json', 'w') as f:
        json.dump(swear_words, f, indent=4)

    os.remove(audio_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 detect.py <file_path>")
        sys.exit(1)
    video_path = sys.argv[1]
    main(video_path)