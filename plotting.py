from matplotlib import pyplot as plt
import numpy as np
from scipy.signal import butter, iirnotch, freqz


def plot_steps(fs, data, filtered_data_lp, filtered_data_bs, combined_signal):
    """Prikazuje ulazni signal, filtrirani signal niskopropusnim i band-stop filterom,
    zatim spektrograme i analize frekvencija jedan pored drugog.
    Opciono, čuva filtrirane signale u fajlu."""
    plt.figure(figsize=(20, 15))

    # Prikazuje ulazni signal, filtrirani signal niskopropusnim i band-stop filterom
    plt.subplot(3, 4, 1)
    plt.plot(data)
    plt.title('1. Ulazni Signal')
    plt.xlabel('Uzorak')
    plt.ylabel('Amplituda')

    plt.subplot(3, 4, 2)
    plt.plot(filtered_data_lp)
    plt.title('2. Filtrirani Signal (LP)')
    plt.xlabel('Uzorak')
    plt.ylabel('Amplituda')

    plt.subplot(3, 4, 3)
    plt.plot(filtered_data_bs)
    plt.title('3. Filtrirani Signal (BS)')
    plt.xlabel('Uzorak')
    plt.ylabel('Amplituda')

    plt.subplot(3, 4, 4)
    plt.plot(combined_signal)
    plt.title('4. Signal Kombinacije Filtera')
    plt.xlabel('Uzorak')
    plt.ylabel('Amplituda')

    # Prikazuje spektrograme ulaznog, filtriranog signala niskopropusnim i band-stop filterom
    plt.subplot(3, 4, 5)
    plt.specgram(data, Fs=fs, cmap='viridis', NFFT=1024)
    plt.title('5. Spektrogram Ulaznog Signala')
    plt.xlabel('Vreme (s)')
    plt.ylabel('Frekvencija (Hz)')
    plt.colorbar()

    plt.subplot(3, 4, 6)
    plt.specgram(filtered_data_lp, Fs=fs, cmap='viridis', NFFT=1024)
    plt.title('6. Spektrogram Filtriranog Signala (LP)')
    plt.xlabel('Vreme (s)')
    plt.ylabel('Frekvencija (Hz)')
    plt.colorbar()

    plt.subplot(3, 4, 7)
    plt.specgram(filtered_data_bs, Fs=fs, cmap='viridis', NFFT=1024)
    plt.title('7. Spektrogram Filtriranog Signala (BS)')
    plt.xlabel('Vreme (s)')
    plt.ylabel('Frekvencija (Hz)')
    plt.colorbar()

    plt.subplot(3, 4, 8)
    plt.specgram(combined_signal, Fs=fs, cmap='viridis', NFFT=1024)
    plt.title('8. Spektrogram Signala Kombinacije Filtera')
    plt.xlabel('Vreme (s)')
    plt.ylabel('Frekvencija (Hz)')
    plt.colorbar()

    # Prikazuje analize frekvencija ulaznog, filtriranog signala niskopropusnim i band-stop filterom
    plt.subplot(3, 4, 9)
    n = len(data)
    k = np.arange(n)
    T = n / fs
    frq = k / T
    frq = frq[:n // 2]
    Y = np.fft.fft(data) / n
    Y = Y[:n // 2]
    plt.plot(frq, np.abs(Y))
    plt.title('9. Analiza Frekvencija Ulaznog Signala')
    plt.xlabel('Frekvencija (Hz)')
    plt.ylabel('Amplituda')

    plt.subplot(3, 4, 10)
    Y_filtered_lp = np.fft.fft(filtered_data_lp) / n
    Y_filtered_lp = Y_filtered_lp[:n // 2]
    plt.plot(frq, np.abs(Y_filtered_lp))
    plt.title('10. Analiza Frekvencija Filtriranog Signala (LP)')
    plt.xlabel('Frekvencija (Hz)')
    plt.ylabel('Amplituda')
    plt.axvline(x=650, color='red', linestyle='--', linewidth=2)  # Dodaje vertikalnu liniju na 650 Hz

    plt.subplot(3, 4, 11)
    Y_filtered_bs = np.fft.fft(filtered_data_bs) / n
    Y_filtered_bs = Y_filtered_bs[:n // 2]
    plt.plot(frq, np.abs(Y_filtered_bs))
    plt.title('11. Analiza Frekvencija Filtriranog Signala (BS)')
    plt.xlabel('Frekvencija (Hz)')
    plt.ylabel('Amplituda')

    plt.subplot(3, 4, 12)
    Y_combined = np.fft.fft(combined_signal) / n
    Y_combined = Y_combined[:n // 2]
    plt.plot(frq, np.abs(Y_combined))
    plt.title('12. Analiza Frekvencija Signala Kombinacije Filtera')
    plt.xlabel('Frekvencija (Hz)')
    plt.ylabel('Amplituda')

    plt.tight_layout()

    plt.show()


def plot_notch_frequency_response(ax, fs, notch_frequency, Q=30):
    """Prikazuje frekvencijski odziv notch filtera."""
    notch_frequency /= fs / 2  # Normalizuje frekvenciju
    b, a = iirnotch(notch_frequency, Q)
    w, h = freqz(b, a, worN=8000)
    ax.plot(0.5 * fs * w / np.pi, np.abs(h), 'b')
    ax.set_title('Frekvencijski Odziv Notch Filtera')
    ax.set_xlabel('Frekvencija [Hz]')
    ax.set_ylabel('Pojacanje')

def display_frequency_responses(fs, cutoff_frequency_lp, notch_frequency):
    """Prikazuje frekvencijski odziv niskopropusnog i notch filtera."""
    _, axs = plt.subplots(1, 2, figsize=(18, 6))

    # Prikazuje frekvencijski odziv niskopropusnog filtera
    plot_lowpass_frequency_response(axs[0], fs, cutoff_frequency_lp)

    # Prikazuje frekvencijski odziv notch filtera
    plot_notch_frequency_response(axs[1], fs, notch_frequency)

    plt.tight_layout()
    plt.show()


def plot_lowpass_frequency_response(ax, fs, cutoff_frequency, order=4):
    """Prikazuje frekvencijski odziv niskopropusnog filtera."""
    nyquist = 0.5 * fs
    normal_cutoff = cutoff_frequency / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    w, h = freqz(b, a, worN=8000)
    ax.plot(0.5 * fs * w / np.pi, np.abs(h), 'b')
    ax.set_title('Frekvencijski Odziv Niskopropusnog Filtera')
    ax.set_xlabel('Frekvencija [Hz]')
    ax.set_ylabel('Pojacanje')

