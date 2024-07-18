import numpy as np
import librosa
import matplotlib.pyplot as plt
import soundfile as sf
import scipy.fftpack as fft
from scipy.signal import medfilt

y, sr = librosa.load('street-noise.mp3', sr=None)

S_full, phase = librosa.magphase(librosa.stft(y))

noise_power = np.mean(S_full[:, :int(sr*0.1)], axis=1)

mask = S_full > noise_power[:, None]

mask = mask.astype(float)

mask = medfilt(mask, kernel_size=(1,5))

S_clean = S_full * mask

y_clean = librosa.istft(S_clean * phase)

sf.write('clean-street-noise.mp3', y_clean, sr)

# visualization
n = len(y)
yf = fft.fft(y)
yf_clean = fft.fft(y_clean)
xf = np.linspace(0.0, sr / 2.0, n//2)

difference = np.abs(yf[:n // 2]) - np.abs(yf_clean[:n // 2])

plt.figure(figsize=(12,15))

plt.subplot(3, 1, 1)
plt.plot(xf, 2.0 / n * np.abs(yf[:n // 2]))
plt.title('FFT of Original Audio')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(xf, 2.0 / n * np.abs(yf_clean[:n // 2]))
plt.title('FFT of Cleaned Audio')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(xf, 2.0 / n * difference, color='red')
plt.title('Difference Between Original and Cleaned Audio')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude Difference')
plt.grid()

plt.show()