import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from utils import snv, first_derivative

class PLSRGlucoseModel:
    def __init__(self, spectra_path, glucose_path, n_components=10, test_size=0.2, random_state=42):
        self.spectra_path = spectra_path
        self.glucose_path = glucose_path
        self.n_components = n_components
        self.test_size = test_size
        self.random_state = random_state
        self.model = PLSRegression(n_components=self.n_components)

    def load_data(self):
        self.X = np.load(self.spectra_path)
        self.y = np.load(self.glucose_path)
        self.wavenumbers = np.linspace(800, 1800, self.X.shape[1])
        print("Data loaded.")

    def preprocess(self):
        self.X_prep = snv(self.X)
        self.X_prep = first_derivative(self.X_prep)
        print("Preprocessing complete.")

    def split_data(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X_prep, self.y, test_size=self.test_size, random_state=self.random_state
        )
        print("Data split into training and testing sets.")

    def train(self):
        self.model.fit(self.X_train, self.y_train)
        print("Model training complete.")

    def predict(self):
        self.y_pred = self.model.predict(self.X_test).ravel()
        print("Prediction complete.")

    def evaluate(self):
        rmse = np.sqrt(mean_squared_error(self.y_test, self.y_pred))
        r2 = r2_score(self.y_test, self.y_pred)
        print(f"RMSE: {rmse:.4f}")
        print(f"R²: {r2:.4f}")
        return rmse, r2

    def plot_results(self):
        plt.figure(figsize=(6, 5))
        plt.scatter(self.y_test, self.y_pred, c='blue')
        plt.plot([0, 10], [0, 10], 'k--')
        plt.xlabel("Actual Glucose (g/L)")
        plt.ylabel("Predicted Glucose (g/L)")
        plt.title("PLSR Prediction on MIR Spectra")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def run(self):
        self.load_data()
        self.preprocess()
        self.split_data()
        self.train()
        self.predict()
        self.evaluate()
        self.plot_results()

if __name__ == "__main__":
    model = PLSRGlucoseModel(
        spectra_path="data/spectra.npy",
        glucose_path="data/glucose_conc.npy",
        n_components=10
    )
    model.run()
