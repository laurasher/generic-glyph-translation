import os
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# moth_file = "audio/19700101_000042.wav"
# moth_file_2 = "audio/19700102_191533.wav"
moth_file = "audio/19700115_163910_trim.wav"

# load audio files with librosa
moth, sr = librosa.load(moth_file)
# moth2, _ = librosa.load(moth_file_2)

#Extracting Short-Time Fourier Transform
FRAME_SIZE = 2048
HOP_SIZE = 512

S_moth = librosa.stft(moth, n_fft=FRAME_SIZE, hop_length=HOP_SIZE)
# S_moth_2 = librosa.stft(moth2, n_fft=FRAME_SIZE, hop_length=HOP_SIZE)

print(S_moth.shape)
# print(S_moth_2.shape)

# Calculate spectrogram
Y_moth = np.abs(S_moth) ** 2
# Y_moth_2 = np.abs(S_moth_2) ** 2

def plot_spectrogram(Y, sr, hop_length, file_append, y_axis="linear"):
    plt.figure(figsize=(25, 10))
    librosa.display.specshow(Y, 
                             sr=sr, 
                             hop_length=hop_length, 
                             x_axis="time", 
                             y_axis=y_axis)
    plt.colorbar(format="%+2.f")
    plt.savefig(f'19700115_163910_trim.png')
    plt.savefig(f'19700115_163910_trim.svg')

# Visualizing the spectrogram
plot_spectrogram(Y_moth, sr, HOP_SIZE, 0)

# Log Amplitude spectrogram
Y_log_moth = librosa.power_to_db(Y_moth)
plot_spectrogram(Y_log_moth, sr, HOP_SIZE, 1)
# Y_log_moth_2 = librosa.power_to_db(Y_moth_2)
# plot_spectrogram(Y_log_moth_2, sr, HOP_SIZE, 2)