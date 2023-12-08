# plotting.py

from matplotlib import pyplot as plt
import numpy as np
from scipy.signal import butter, iirnotch, freqz


def plot_steps(fs, *signals):
    """Displays each signal, its spectrogram, and frequency analysis side by side."""
    num_signals = len(signals)
    
    plt.figure(figsize=(20, 5 * num_signals))

    for i, signal in enumerate(signals, start=1):
        # Plot the signal itself
        plt.subplot(num_signals, 3, i)
        plt.plot(signal[0])
        plt.title(f'{i}. Signal {signal[1]}')
        plt.xlabel('Sample')
        plt.ylabel('Amplitude')

        # Plot the spectrogram of the signal
        plt.subplot(num_signals, 3, i + num_signals)
        plt.specgram(signal[0], Fs=fs, cmap='viridis', NFFT=1024)
        plt.title(f'{i}. Spectrogram ')
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency (Hz)')
        plt.colorbar()

        # Plot the frequency analysis of the signal
        plt.subplot(num_signals, 3, i + 2 * num_signals)
        n = len(signal[0])
        k = np.arange(n)
        T = n / fs
        frq = k / T
        frq = frq[:n // 2]
        Y = np.fft.fft(signal[0]) / n
        Y = Y[:n // 2]

        # Limit X-axis to 5000 Hz
        plt.plot(frq[frq <= 5000], np.abs(Y[frq <= 5000]))
        
        plt.title(f'{i}. Frequency Analysis (up to 5000 Hz)')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Amplitude')

    plt.tight_layout()
    plt.show()


def plot_notch_frequency_response(ax, fs, notch_frequency, Q=30):
    """Displays the frequency response of a notch filter."""
    notch_frequency /= fs / 2  # Normalizes the frequency
    b, a = iirnotch(notch_frequency, Q)
    w, h = freqz(b, a, worN=8000)

    # Limit X-axis to 2500 Hz
    ax.plot(0.5 * fs * w / np.pi, np.abs(h), 'b')
    
    ax.set_xlim([0, 2500])  # Set X-axis limit to 5000 Hz
    ax.set_title('Frequency Response of Notch Filter (up to 5000 Hz)')
    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('Gain')


def plot_lowpass_frequency_response(ax, fs, cutoff_frequency, order=4):
    """Displays the frequency response of a low-pass filter."""
    nyquist = 0.5 * fs
    normal_cutoff = cutoff_frequency / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    w, h = freqz(b, a, worN=8000)

    # Limit X-axis to 5000 Hz
    ax.plot(0.5 * fs * w / np.pi, np.abs(h), 'b')
    
    ax.set_title('Frequency Response of Low-pass Filter (up to 5000 Hz)')
    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('Gain')
