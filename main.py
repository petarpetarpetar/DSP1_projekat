from matplotlib import pyplot as plt
import numpy as np
from scipy.io import wavfile
from plotting import plot_steps, plot_notch_frequency_response
from filter_functions import apply_lowpass_filter, apply_bandstop_filter, save_to_file, apply_notch_filter


def read_audio(file_path, combine_channels=False):
    """Reads a WAV file and returns the sampling rate and data."""
    fs, data = wavfile.read(file_path)
    
    if combine_channels and data.ndim > 1:
        data = np.mean(data, axis=1)

    return fs, data


def main():
    input_file = "./sources/12.wav"
    output_dir = "./results/audio/"

    # Čita WAV fajl bez kombinovanja kanala
    fs, data = read_audio(input_file, combine_channels=True)

    # Primenjuje niskopropusni filter
    filtered_data_lp = apply_lowpass_filter(data, fs, cutoff_frequency=300, order=8)
    save_to_file(f"{output_dir}filtered_signal_lp.wav", fs, filtered_data_lp)

    # Primenjuje band-stop filter
    filtered_data_bs = apply_bandstop_filter(data, fs, stop_frequency=300)
    combined_signal_bs = apply_bandstop_filter(filtered_data_lp, fs, stop_frequency=300)
    save_to_file(f"{output_dir}filtered_signal_bs.wav", fs, filtered_data_bs)
    save_to_file(f"{output_dir}combined_signal_bs.wav", fs, combined_signal_bs)

    # Primenjuje notch filter
    f_notch = 300  # Notch frequency in Hz
    r = 0.90  # Vary this parameter
    filtered_data_notch, b_notch, a_notch = apply_notch_filter(data, fs, f_notch, r)
    save_to_file(f"{output_dir}filtered_signal_notch.wav", fs, filtered_data_notch)
    
    filtered_data_notch_4, _, _ = apply_notch_filter(filtered_data_notch, fs, f_notch, r)
    save_to_file(f"{output_dir}filtered_signal_notch_4.wav", fs, filtered_data_notch_4)

    filtered_data_notch_6, _, _ = apply_notch_filter(filtered_data_notch_4, fs, f_notch, r)
    save_to_file(f"{output_dir}filtered_signal_notch_6.wav", fs, filtered_data_notch_6)
    

    # Output notch filter coefficients
    print(f"Notch Filter Coefficients (b, a): {b_notch}, {a_notch}")

   # Prikazuje samo freq odziv filtera
    _, axs = plt.subplots(1, 1, figsize=(18, 18))
    plot_notch_frequency_response(axs, fs, f_notch, Q=30)

    plot_steps(fs, (data, "original"), (filtered_data_lp, "low pass"), (filtered_data_notch_6, "notch_6"))
    plot_steps(fs, (data, "original"), (filtered_data_notch, "notch 2nd order"), (filtered_data_notch_4, "notch 4th order"))

if __name__ == "__main__":
    main()