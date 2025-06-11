# script: utils.py
import numpy as np
from scipy.signal import savgol_filter

def snv(X):
    """Standard Normal Variate (row-wise)."""
    return (X - np.mean(X, axis=1, keepdims=True)) / np.std(X, axis=1, keepdims=True)

def first_derivative(X, window=11, polyorder=2):
    """Savitzky-Golay first derivative."""
    return savgol_filter(X, window_length=window, polyorder=polyorder, deriv=1, axis=1)
