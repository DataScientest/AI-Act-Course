from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import pickle
import os

# Chargement des données
iris = load_iris()
X, y = iris.data, iris.target

# Séparation train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Entraînement
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Évaluation
y_pred = model.predict(X_test)
print("=== Métriques d'évaluation ===")
print(f"Accuracy : {accuracy_score(y_test, y_pred):.4f}")
print("\nClassification Report :")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
print(f"\nTaille du jeu d'entraînement : {len(X_train)} exemples")
print(f"Taille du jeu de test        : {len(X_test)} exemples")

# Sauvegarde du modèle
os.makedirs("models", exist_ok=True)
with open("models/iris_classifier.pkl", "wb") as f:
    pickle.dump(model, f)

print("\nModèle sauvegardé dans models/iris_classifier.pkl")