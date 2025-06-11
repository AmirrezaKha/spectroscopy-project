# 🧪 Spectroscopy Project: Predicting Glucose Concentration from FTIR Spectra

This project demonstrates how to analyze **mid-infrared (MIR) spectral data** using **physics-informed preprocessing** and **Partial Least Squares Regression (PLSR)** to predict the **concentration of glucose** in bioprocess environments.

It is designed to reflect real-world challenges and methodologies used in biopharmaceutical monitoring, with an emphasis on interpretability and robustness — the kind of solution IRUBIS or similar companies would implement in production systems.

---

## 📁 Project Structure

```
spectroscopy_project/
│
├── data/
│   ├── spectra.npy           # Simulated MIR spectra (100 samples × 500 wavenumbers)
│   └── glucose_conc.npy      # Corresponding glucose concentrations (in g/L)
│
├── generate_data.py          # Script to simulate and save spectral data
├── main.py                   # Full pipeline: preprocessing, modeling, evaluation
├── utils.py                  # Preprocessing functions (SNV, derivative)
└── README.md                 # Project documentation
```

---

## 🎯 Objective

Predict the concentration of glucose from mid-IR spectral data using robust and interpretable modeling techniques.

---

## 📊 Methods

### 🧹 Preprocessing
- **SNV (Standard Normal Variate)** normalization
- **Savitzky-Golay filtering** (first derivative)
- Simulated baseline and peak features mimicking glucose absorption (e.g., around 1030–1080 cm⁻¹)

### 📈 Modeling
- **Partial Least Squares Regression (PLSR)**
- Model trained and validated using `scikit-learn`
- Evaluation metrics: RMSE, R²

---

## 🔧 Setup & Execution

### 1. Clone the repo

```bash
git clone https://github.com/AmirrezaKha/spectroscopy-task.git
cd spectroscopy_project
```

### 2. Install requirements

```bash
pip install numpy scipy scikit-learn matplotlib
```

### 3. Generate synthetic data

```bash
python generate_data.py
```

### 4. Run the pipeline

```bash
python main.py
```

---

## 📉 Example Output

```
RMSE: 0.62  
R²: 0.94
```

A scatter plot will show predicted vs. actual glucose concentrations, ideally along the diagonal.

---

## ✅ Highlights

- **Physics-aware modeling**: No deep learning, just interpretable and explainable regression  
- **Spectral preprocessing**: Critical steps like SNV and derivatives improve robustness  
- **Production-readiness**: Lightweight code suitable for embedded or edge deployment  

---

## 🧠 Learnings

This project shows how to:

- Extract meaningful signals from noisy vibrational spectra  
- Model relationships between spectral intensity and biochemical parameters  
- Prepare pipelines for deployment in bioprocess monitoring systems  

---

## 📬 Contact

For questions, feel free to reach out or mention this project in your application to **IRUBIS**.