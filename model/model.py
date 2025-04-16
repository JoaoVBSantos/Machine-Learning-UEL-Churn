import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib 

# Importando base de dados
df = pd.read_csv("C:/Users/Jão/Downloads/churn.csv", delimiter=",")
df = df.drop(columns=["customerID", "TotalCharges"], errors='ignore')
df

# Separar features (X) e target (y)
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Avaliar o modelo
y_pred = model.predict(X_test)

#print("Accuracy:", accuracy_score(y_test, y_pred))
#print("\nClassification Report:\n", classification_report(y_test, y_pred))

joblib.dump(model, "chur.sav")

