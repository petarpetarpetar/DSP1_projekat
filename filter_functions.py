# filter_functions.py

import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, lfilter, iirnotch, iirfilter


def apply_lowpass_filter(data, fs, cutoff_frequency=650, order=8):
    """Applies a low-pass filter to an audio signal."""
    nyquist = 0.5 * fs
    normal_cutoff = cutoff_frequency / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    filtered_data = lfilter(b, a, data)
    return filtered_data


def apply_bandstop_filter(data, fs, stop_frequency=300, Q=30):
    """Applies a band-stop filter to an audio signal."""
    nyquist = 0.5 * fs
    notch_frequency = stop_frequency / nyquist
    b, a = iirnotch(notch_frequency, Q)
    filtered_data = lfilter(b, a, data)
    return filtered_data


def design_notch_filter(fs, f_notch, r):
    """Designs a notch filter with the given parameters."""
    f_notch /= fs / 2  # Normalize the notch frequency
    b, a = iirfilter(2, [f_notch - 0.01, f_notch + 0.01], rp=5, rs=60, btype='bandstop', analog=False, ftype='butter')

    return b, a

def apply_notch_filter(data, fs, f_notch, r):
    """Applies the designed notch filter to the input signal."""
    b, a = design_notch_filter(fs, f_notch, r)
    filtered_data = lfilter(b, a, data)
    return filtered_data, b, a


def save_to_file(file_path, fs, data):
    """Saves an audio signal to a WAV file."""
    wavfile.write(file_path, fs, data.astype(np.int16))
