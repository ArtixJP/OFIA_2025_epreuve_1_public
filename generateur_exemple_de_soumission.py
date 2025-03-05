import pandas as pd

# Chargement des données 

X_train = pd.read_csv("X_train.csv")
y_train = pd.read_csv("y_train.csv")

X_test = pd.read_csv("X_test.csv")

y_test = pd.DataFrame(columns=["id", "probabilite_toxique"])

for i in range(len(X_test)):
    # prédit une probabilité de 0.5 pour tous les échantillons de test
    y_test.loc[i] = [str(X_test.loc[i]["id"]), 0.5]

y_test.to_csv("y_test.csv", index=False)
