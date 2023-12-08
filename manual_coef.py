import numpy as np
from scipy.signal import tf2zpk

def design_notch_filter(fs, f_notch, r):
    # Normalize frequencies
    notch_frequency = f_notch / (fs / 2)
    
    # Calculate Q factor
    Q = 1 / (2 * r - 1)

    # Numerator coefficients (b)
    b = [1, -2 * np.cos(2 * np.pi * notch_frequency), 1]

    # Denominator coefficients (a)
    a = [1, -2 * r * np.cos(2 * np.pi * notch_frequency), r**2]

    return b, a

# Example usage
fs = 1000  # Sample rate
f_notch = 300  # Notch frequency in Hz
r = 0.95  # Adjust as needed

b_notch, a_notch = design_notch_filter(fs, f_notch, r)

# Calculate poles and zeros
zeros, poles, gain = tf2zpk(b_notch, a_notch)

print("Zeros:", zeros)
print("Poles:", poles)
print("Gain:", gain)