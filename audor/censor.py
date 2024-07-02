def censor_audio(path, time_range):
    print(path)
    print(time_range)

if __name__ == '__main__':
    censor_audio("extracted_audio.wav", [3.16, 3.8, 38.3, 38.6, 52.1, 52.36, 54.56, 54.86, 55.58, 
                                         55.78, 80.2, 80.64, 82.76, 83.06, 84.28, 84.8, 84.8, 85.72,
                                           97.34, 98.18, 98.36, 98.8, 99.5, 99.94, 102.32, 102.54])