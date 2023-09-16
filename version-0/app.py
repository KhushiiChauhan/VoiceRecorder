import sounddevice as sd
import numpy as np
import sys
import os
import soundfile as sf
fs = 44100
recorded_data = []
def audio_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    recorded_data.append(indata.copy())
with sd.InputStream(callback=audio_callback, channels=2, samplerate=fs):
    print("Recording Started")
    input("Press Enter to stop recording...")
    print("Recording Stopped")
if input("Do you want to save this file (Y/N)? ").strip().lower() == 'y':
    admin_pass = input("Enter Admin Pass: ")
    if    admin_pass == "12345678":
        wav_filename = input("Enter File Name: ") + '.mp3'  # Change the file extension to .wav if not working
        recorded_data = np.concatenate(recorded_data)
        sf.write(wav_filename,recorded_data, fs)
        print(f"Audio saved as {wav_filename}")
    else:
        print("You don't have this privilege. You can only play your recorded file.")
        ch1 = input("Would you like to play it (Y/N)? ").strip().lower()
        if ch1 == 'y':
            sd.play(np.concatenate(recorded_data), fs)
            sd.wait()
        else:
            exit(0)
