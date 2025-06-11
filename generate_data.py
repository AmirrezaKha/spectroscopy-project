# script: generate_data.py
import numpy as np

np.random.seed(42)

n_samples = 100
n_wavenumbers = 500
wavenumbers = np.linspace(800, 1800, n_wavenumbers)  # in cm^-1, MIR region

# Base spectrum: random smooth baseline
spectra = np.random.normal(0, 0.02, (n_samples, n_wavenumbers)) + \
          np.exp(-0.001 * (wavenumbers - 1200) ** 2)  # background

# Simulate glucose peak between 1030–1080 cm^-1
for i in range(n_samples):
    glucose = np.random.uniform(0, 10)  # in g/L
    spectra[i] += glucose * np.exp(-0.5 * ((wavenumbers - 1050) / 10) ** 2)
    if i == 0:
        glucose_conc = np.array([glucose])
    else:
        glucose_conc = np.append(glucose_conc, glucose)

# Save
np.save("data/spectra.npy", spectra)
np.save("data/glucose_conc.npy", glucose_conc)
