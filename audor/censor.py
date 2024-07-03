import ctypes
import numpy as np
import os
import platform
import sys

def censor_audio(path, time_range):
    os_name = os.name
    platform_system = platform.system()

    if os_name == 'nt':
         lib = ctypes.CDLL('./censor_audio.dll')
    elif os_name == 'posix':
        if platform_system == 'Linux':
            lib = ctypes.CDLL('./censor_audio.so')
        elif platform_system == 'Darwin':
            lib = ctypes.CDLL('./censor_audio.dylib')
        else:
            sys.exit(1)
    else:
        sys.exit(1)

    lib.censor.argtypes = (
        ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)
    )

    lib.censor.restype = ctypes.c_int

    time_stamps = np.array(time_range, dtype=np.float64)
    time_stamps = time_stamps.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    
    input_file = path
    output_file = "censored_audio.wav"

    result = lib.censor_audio(
        input_file.encode('utf-8'),
        output_file.encode('utf-8'),
        time_stamps
    )


if __name__ == '__main__':
    censor_audio("extracted_audio.wav", [3.16, 3.8, 38.3, 38.6, 52.1, 52.36, 54.56, 54.86, 55.58, 
                                         55.78, 80.2, 80.64, 82.76, 83.06, 84.28, 84.8, 84.8, 85.72,
                                           97.34, 98.18, 98.36, 98.8, 99.5, 99.94, 102.32, 102.54])