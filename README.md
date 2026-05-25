# Exercice central — Audit Trail, Logging et Traçabilité des prédictions

## Objectif

L’objectif de cet exercice est de transformer un simple modèle scikit-learn en un mini système MLOps traçable capable de :

* servir des prédictions via une API
* enregistrer des audit logs structurés
* pseudonymiser les utilisateurs
* relier une prédiction au pipeline d’entraînement
* reconstituer l’historique complet d’une décision

L’exercice s’inspire directement des notions vues dans le chapitre :

* audit trail
* logging structuré
* traçabilité
* RGPD
* AI Act

---

# Ce que vous allez construire

À la fin de l’exercice, vous disposerez :

* d’une API FastAPI
* d’un système de logs JSONL
* d’une pseudonymisation HMAC
* d’un tracking MLflow
* d’un script d’audit trail
* d’une Model Card reliée au pipeline ML

---

# Architecture du projet

```text
exercice/
│
├── app/
│   └── main.py
│
├── model_artifacts/
│   ├── model.pkl
│   ├── run_id.txt
│   └── model_metadata.pkl
│
├── logs/
│   └── audit.jsonl
│
│
├── docs/
│   └── audit_trail.md
│
├── train.py
├── audit_query.py
├── model_card.md
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
│
├── .env
├── .gitignore
│
├── pyproject.toml
└── uv.lock
```

---

# Technologies utilisées

| Outil        | Rôle                         |
| ------------ | ---------------------------- |
| FastAPI      | API d’inférence              |
| structlog    | logs JSON structurés         |
| MLflow       | tracking entraînement        |
| Docker       | conteneurisation             |
| uv           | gestion environnement Python |
| scikit-learn | modèle ML                    |

---

# Étape 1 — Cloner le repository

Clonez le repository de départ.

```bash
git clone <REPO_URL>

cd exercice
```

---

# Étape 2 — Initialiser l’environnement Python

Nous utiliserons uv afin de reproduire exactement le même environnement Python.

## Initialiser le projet

```bash
uv init
```

## Installer les dépendances

```bash
uv add -r requirements.txt
```

---

# Étape 3 — Lancer MLflow

Le projet contient déjà un fichier :

```text
docker-compose.yml
```

Lancez uniquement le serveur MLflow :

```bash
docker compose up mlflow
```

MLflow sera accessible sur :

```text
http://localhost:5000
```

---

# Étape 4 — Entraîner le modèle

Le fichier :

```text
train.py
```

permet de :

* entraîner un modèle RandomForestClassifier
* logger les métriques dans MLflow
* récupérer le git SHA
* récupérer le MLflow Run ID
* sauvegarder les métadonnées du modèle

Exécutez le script :

```bash
uv run train.py
```

Après exécution, vous devriez obtenir :

```text
model_artifacts/
├── model.pkl
├── run_id.txt
└── model_metadata.pkl
```

---

# Étape 5 — Compléter la Model Card

Le repository contient un fichier :

```text
model_card.md
```

Complétez votre propre Model Card avec :

* le nom du modèle
* le dataset utilisé
* les métriques
* les limitations
* les usages prévus
* le git SHA
* le MLflow Run ID

L’objectif est de relier la documentation :

* au modèle
* au code
* au pipeline d’entraînement

---

# Étape 6 — Générer une clé HMAC

Ouvrez un terminal Python :

```bash
python
```

Puis :

```python
import secrets

secrets.token_hex(32)
```

Exemple :

```text
7f9c2d91a84be63f5c7d2e1ab49f0c8d
```

Créez ensuite un fichier :

```text
.env
```

Ajoutez :

```env
AUDIT_HMAC_KEY=7f9c2d91a84be63f5c7d2e1ab49f0c8d
```

Ajoutez également `.env` dans `.gitignore`.

---

# Étape 7 — Construire l’API FastAPI

Créez le fichier :

```text
app/main.py
```

L’API devra :

* charger le modèle
* charger les métadonnées MLflow
* servir les prédictions
* pseudonymiser les utilisateurs
* mesurer la latence
* générer des audit logs JSON

Les logs devront notamment contenir :

* request_id
* model_version
* git_sha
* mlflow_run_id
* prediction
* confidence
* latency_ms
* user_id_pseudo

---

# Étape 8 — Construire le script d’audit

Créez :

```text
audit_query.py
```

Le script devra permettre de reconstruire l’historique d’une prédiction à partir d’un :

```text
request_id
```

Exemple :

```bash
uv run audit_query.py --request_id <REQUEST_ID>
```

Le script devra afficher :

* la prédiction
* le score de confiance
* le modèle utilisé
* le git SHA
* le MLflow Run ID
* la Model Card associée

---

# Étape 9 — Dockeriser l’API

Le projet contient déjà :

```text
Dockerfile
```

et :

```text
docker-compose.yml
```

Lancez toute la stack :

```bash
docker compose up --build
```

Cette commande va :

* lancer MLflow
* construire l’image Docker
* lancer l’API FastAPI

---

# Étape 10 — Tester l’API

Ouvrez :

```text
http://localhost:8000/docs
```

Vous devriez voir la documentation Swagger.

---

# Endpoint /predict

Exemple de payload :

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2,
  "user_id": "12345"
}
```

Réponse attendue :

```json
{
  "request_id": "...",
  "prediction": 0,
  "confidence": 0.98
}
```

---

# Étape 11 — Observer les audit logs

Ouvrez :

```text
logs/audit.jsonl
```

Exemple :

```json
{
  "request_id": "...",
  "model_version": "iris-v1",
  "git_sha": "a74f21d",
  "mlflow_run_id": "3e91ab2",
  "prediction": 0,
  "confidence": 0.98,
  "latency_ms": 12,
  "user_id_pseudo": "8f3a9ab2..."
}
```

Chaque prédiction devient donc traçable.

---


# Résultat final

À la fin de cet exercice, vous avez construit une première version d’un système ML capable de :

* exposer un modèle via une API
* tracer chaque prédiction
* pseudonymiser les utilisateurs
* relier une prédiction au pipeline ML
* reconstruire un historique complet via un audit trail

Même si cette architecture reste volontairement simplifiée, elle reprend déjà plusieurs principes fondamentaux des systèmes MLOps modernes :

* observabilité
* auditabilité
* reproductibilité
* gouvernance des modèles
* traçabilité

---

