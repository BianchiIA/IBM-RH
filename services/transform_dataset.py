from sklearn.preprocessing import OneHotEncoder
import pandas as pd


class TranformIBMRH:
    def __init__(self):
        self.columns_obj = ['BusinessTravel','Gender','OverTime']
        self.dict_map_obj = [{'Travel_Rarely':3,'Travel_Frequently':2,'Non-Travel':1}, {'Female':0, 'Male':1},{'Yes':1, 'No':0}]
        self.columns_label = ['Gender', 'OverTime', 'BusinessTravel']
        self.columns_ohe = ['Department', 'EducationField', 'JobRole', 'MaritalStatus']
        self.ohe = OneHotEncoder(sparse=False)

    def transform(self, df:pd.DataFrame, fit_ohe = None):
        # Mapeamendo de Variáveis categoricas Ordinais
        X = df.copy()
        for col,maps in zip(self.columns_obj, self.dict_map_obj):
            X['{}'.format(col)] = X['{}'.format(col)].map(maps)
        X_num = X.select_dtypes(exclude='object')

        if fit_ohe is None:
            self.ohe.fit(X[self.columns_ohe])
            X_cat = self.ohe.transform(X[self.columns_ohe])
            X_concat = pd.concat([pd.DataFrame(X_num),pd.DataFrame(X_cat)], axis=1)
            return X_concat, self.ohe
        else:
            X_cat = fit_ohe.transform(X[self.columns_ohe])
            X_concat = pd.concat([pd.DataFrame(X_num),pd.DataFrame(X_cat)], axis=1)
            return X_concat

