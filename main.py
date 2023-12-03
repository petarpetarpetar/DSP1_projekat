import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, lfilter, iirnotch, firwin

from plotting import plot_steps, display_frequency_responses

def read_audio(file_path, combine_channels=False):
    """Čita WAV fajl i vraća stopu uzorkovanja i podatke."""
    fs, data = wavfile.read(file_path)
    
    if combine_channels and data.ndim > 1:
        # Ako je postavljena oznaka i postoje više kanala, kombinujte ih uzimajući srednju vrednost
        data = np.mean(data, axis=1)

    return fs, data

def apply_lowpass_filter(data, fs, cutoff_frequency=650, order=8):
    """Primenjuje niskopropusni filter na audio signal."""
    nyquist = 0.5 * fs
    normal_cutoff = cutoff_frequency / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    filtered_data = lfilter(b, a, data)
    return filtered_data


def apply_bandstop_filter(data, fs, stop_frequency=300, Q=30):
    """Primenjuje band-stop filter na audio signal."""
    nyquist = 0.5 * fs
    notch_frequency = stop_frequency / nyquist
    b, a = iirnotch(notch_frequency, Q)
    filtered_data = lfilter(b, a, data)
    return filtered_data

def save_to_file(file_path, fs, data):
    """Čuva audio signal u WAV fajlu."""
    wavfile.write(file_path, fs, data.astype(np.int16))


def main():
    input_file = "./sources/12.wav"
    output_dir = "./results/audio/"

    # Čita WAV fajl bez kombinovanja kanala
    fs, data = read_audio(input_file, combine_channels=True)

    # Primenjuje niskopropusni filter
    filtered_data_lp = apply_lowpass_filter(data, fs, cutoff_frequency = 300, order= 8)

    # Primenjuje band-stop filter
    
    filtered_data_bs = apply_bandstop_filter(data, fs, stop_frequency = 300)

    combined_signal = apply_bandstop_filter(filtered_data_lp, fs, stop_frequency = 300)

    save_to_file(f"{output_dir}filtered_signal_lp.wav", fs, filtered_data_lp)
    save_to_file(f"{output_dir}filtered_signal_bs.wav", fs, filtered_data_bs)
    save_to_file(f"{output_dir}combined_signal.wav", fs, combined_signal)

    plot_steps(fs, data, filtered_data_lp, filtered_data_bs, combined_signal)

    # Prikazuje samo freq odziv filtera
    display_frequency_responses(fs, cutoff_frequency_lp=650, notch_frequency=300)

if __name__ == "__main__":
    main()
