import pickle
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from services.transform_dataset import TranformIBMRH

import json

class PredictRH:
    def __init__(self):
        with open('models/variveis_modelo.pkl', 'rb') as f:
            self.scaler, self.ohe, self.model = pickle.load(f)

    def teste(self, X):
        t = pd.read_json(X)
        return t

    def _transform(self, X):
        df = pd.json_normalize(X)
        df = TranformIBMRH().transform(df, fit_ohe=self.ohe)
        df_norm = self.scaler.transform(df)
        return df_norm

    def predict(self, X):
        x = self._transform(X)
        y = self.model.predict(x)
        return y[0]


