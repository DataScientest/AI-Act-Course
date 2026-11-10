---
license: mit
language:
- en
datasets:
- iris
metrics:
- accuracy
- f1
pipeline_tag: tabular-classification
---

## Model Details
- **Model name:** Iris Classifier
- **Author:** anamvg
- **Date:** November 10, 2026
- **Version:** 1.0
- **Model type:** RandomForestClassifier (scikit-learn)
- **License:** MIT

## Intended Use

### Intended Use Cases
This model is intended for educational and demonstration purposes to classify Iris flower species based on sepal and petal measurements. It is designed for students, developers, and researchers learning about model cards and basic tabular classification pipelines.

### Out-of-scope Use
This model is not suitable for production deployment or commercial use. It is strictly inappropriate for high-stakes decision-making, agricultural management, or any safety-critical application.

## Factors (Facteurs)

The performance of this tabular model can be influenced by several domain and data factors:
- **Feature Distribution:** Variations or extreme values in input measurements (sepal length, sepal width, petal length, and petal width) outside the typical ranges of the training data may degrade classification performance.
- **Class Balance:** The Iris dataset has a balanced distribution across the three flower classes (Setosa, Versicolor, and Virginica). Any shift or imbalance in input data distribution during evaluation or deployment can impact predictive precision across specific classes.

## Metrics (Métriques)

The model's performance is evaluated using standard classification metrics suitable for a balanced multi-class problem:

- **Accuracy:** Measures the overall proportion of correctly classified iris flowers across all three classes.
- **Precision:** Evaluates the proportion of true positive predictions relative to total predicted positives for each species (*setosa*, *versicolor*, *virginica*).
- **Recall (Sensibilidad):** Measures the proportion of actual positive instances correctly identified for each class.
- **F1-Score:** Provides the harmonic mean of precision and recall, balancing both metrics, especially useful to ensure reliable performance across all three target categories.

## Training Data (Données d'entraînement)

- **Dataset name:** Iris flower dataset
- **Source:** `sklearn.datasets.load_iris`
- **Size:** 120 samples (80% of the total dataset used for training)
- **Features (Input variables):**
  - Sepal length (cm)
  - Sepal width (cm)
  - Petal length (cm)
  - Petal width (cm)
- **Target (Classes to predict):**
  - `setosa`
  - `versicolor`
  - `virginica`

## Evaluation Data (Données d'évaluation)

- **Source:** Same dataset as training (Iris flower dataset), held-out test split.
- **Size:** 30 samples (20% of the total dataset).
- **Split method:** `train_test_split` with a test ratio of `0.2` (20%) and a `random_state` of `42`.
- **Preprocessing:** No specific preprocessing applied.

## Quantitative Analyses (Analyses quantitatives)

The model achieves an overall **Accuracy of 1.00** (100%) on the test set (30 examples). The disaggregated performance metrics by class are homogeneous and perfect:

- **Setosa:** Precision: 1.00 | Recall: 1.00 | F1-score: 1.00 (Support: 10)
- **Versicolor:** Precision: 1.00 | Recall: 1.00 | F1-score: 1.00 (Support: 9)
- **Virginica:** Precision: 1.00 | Recall: 1.00 | F1-score: 1.00 (Support: 11)

**Summary:** The model exhibits exceptional and homogeneous performance across all three classes, with no poorly classified categories on the current evaluation split.

## Ethical Considerations (Considérations éthiques)

- **Usage risks:** Although the ethical risks for botanical classification are very low, misusing this model in critical automated agricultural systems could lead to improper crop handling. It is strictly designed for educational purposes and should not be used in high-stakes operational settings.
- **Potential biases:** The Iris dataset contains only 150 samples across 3 specific flower species collected in a specific geographical context. It is not representative of all global flora or other subspecies, meaning performance will degrade significantly on unseen plant varieties.

## Caveats and Recommendations (Limites et recommandations)

- **Very small dataset (150 observations):** We recommend not generalizing the model's predictions to broader or unknown botanical contexts without further validation and dataset expansion.
- **Data not representative of the real world:** We recommend testing the model on data collected under varied environmental and real-world conditions before any consideration of use.
- **Limited evaluation setup:** We recommend implementing a more robust evaluation strategy, such as cross-validation, prior to any deployment.

## Reproductibility
<!-- Complete after section B.10 -->
