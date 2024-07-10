#include <stdio.h>
#include <stdlib.h>

// Below is for .wav files, future implementations will include more support
#define SAMPLE_RATE 44100
#define BITS_PER_SAMPLE 16 
#define CHANNELS 1 // Mono audio

void remove_audio_segment(FILE *input_file, FILE *output_file, double start_time, double end_time) {

    int bytes_per_sample = BITS_PER_SAMPLE / 8;
    int frame_size = bytes_per_sample * CHANNELS;

    long start_frame = (long)(start_time * SAMPLE_RATE);
    long end_frame = (long)(end_time * SAMPLE_RATE);

    unsigned char buffer[1024];
    long frame_count = 0;

    while (!feof(input_file)) {
        size_t read_size = fread(buffer, 1, sizeof(buffer), input_file);
        size_t samples = read_size / frame_size;

        for (size_t i = 0; i < samples; ++i) {
            if (frame_count < start_frame || frame_count >= end_frame) {
                fwrite(buffer + (i * frame_size), frame_size, 1, output_file);
            }
            frame_count++;
        }
    }

    fclose(input_file);
    fclose(output_file);
}

int main(const char *input_file, const char *output_file, double *time_stamps) {

    FILE *in_fp = fopen(input_file, "rb");
    if (in_fp == NULL) {
        perror("Error opening input file");
        return 1;
    }

    FILE *out_fp = fopen(output_file, "wb");
    if (out_fp == NULL) {
        perror("Error opening output file");
        fclose(in_fp);
        return 1;
    }

    int length = sizeof(time_stamps)/sizeof(time_stamps[0]);
    for(int i = 0; i < length; i+=2) {
        remove_audio_segment(in_fp, out_fp, time_stamps[i], time_stamps[i+1]);
    }

    return 0;
}