def censor_audio(path, time_range):
    print(path)
    print(time_range)

if __name__ == '__main__':
    censor_audio("extracted_audio.wav", [0.0, 9.0, 51.0, 53.0, 53.0, 54.0, 54.0, 56.0, 80.0, 81.0, 83.0, 84.0, 86.0, 87.0, 96.0, 98.0, 98.0, 99.0, 99.0, 100.0, 100.0, 101.0, 102.0, 103.0])