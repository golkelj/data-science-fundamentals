### Precison and Recall

Where:
- **TP**: True Positives
- **FP**: False Positives

## Interpretation

- **High precision** means that when the model predicts something as positive, it's usually correct.
- Precision is especially important when **false positives are costly**, such as in:
  - Spam detection
  - Medical diagnosis

## Precision vs. Recall

| Metric      | Formula             | Focus                            |
|-------------|---------------------|----------------------------------|
| Precision   | TP / (TP + FP)      | Accuracy of positive predictions |
| Recall      | TP / (TP + FN)      | Coverage of actual positives     |

To balance precision and recall, we use the **F1 Score**:

F1 Score = 2 * (Precision * Recall) / (Precision + Recall)

