from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from services.transform_dataset import TranformIBMRH
from sklearn.metrics import f1_score
import pandas as pd


def train(retorno =False):
    scaler = StandardScaler()
    transf = TranformIBMRH()

    df = pd.read_csv('../data/WA_Fn-UseC_-HR-Employee-Attrition.csv')
    deletar = ['Over18', 'EmployeeNumber', 'EmployeeCount', 'StandardHours']
    df = df.reset_index().drop(['index'] + deletar, axis=1)
    df['Attrition'] = df['Attrition'].map({'No': 0, 'Yes': 1})
    data = transf.transform(df)

    clf = LogisticRegression(max_iter=500,
                             penalty='none',
                             solver='lbfgs')

    X, y = data.drop(['Attrition'], axis=1), data['Attrition']

    X_norm = scaler.fit_transform(X)

    clf.fit(X_norm, y)
    y_pred = clf.predict(X_norm)
    eval = f1_score(y, y_pred, average='macro')

    if retorno:
        return clf, transf, scaler
    else:
        pass



