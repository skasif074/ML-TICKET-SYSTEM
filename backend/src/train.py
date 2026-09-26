
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)
import joblib

from preprocessing import clean_dataframe_column

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "tickets.csv")
MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "model")
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")
SCREENSHOTS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "screenshots")


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"Loaded dataset: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


def clean_missing_and_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    print("\nMissing values before cleaning:")
    print(df.isnull().sum())

    df = df.dropna(subset=["ticket_description", "category"]).copy()

    df["priority"] = df["priority"].fillna("Medium")
    df["status"] = df["status"].fillna("Open")

    before = len(df)
    df = df.drop_duplicates(subset=["ticket_description"], keep="first")
    after = len(df)
    print(f"\nRemoved {before - after} duplicate rows based on ticket_description")

    return df.reset_index(drop=True)


def plot_confusion_matrix(y_test, y_pred, labels, save_path):
    cm = confusion_matrix(y_test, y_pred, labels=labels)

    plt.figure(figsize=(7, 6))
    sns.heatmap(
        cm, annot=True, fmt="d", cmap="Blues",
        xticklabels=labels, yticklabels=labels,
        cbar=True, linewidths=0.5, linecolor="gray"
    )
    plt.title("Confusion Matrix - Ticket Category Classification", fontsize=13)
    plt.xlabel("Predicted Category")
    plt.ylabel("Actual Category")
    plt.xticks(rotation=30, ha="right")
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"\nConfusion matrix chart saved to {save_path}")


def train_model():
    df = load_data(DATA_PATH)
    df = clean_missing_and_duplicates(df)
    df = clean_dataframe_column(df, column="ticket_description")

    X = df["clean_description"]
    y = df["category"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    vectorizer = TfidfVectorizer(max_features=3000, ngram_range=(1, 2))
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vec, y_train)

    y_pred = model.predict(X_test_vec)

    print("\n--- Evaluation on Test Set ---")
    print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred, average='weighted'):.4f}")
    print(f"Recall:    {recall_score(y_test, y_pred, average='weighted'):.4f}")
    print(f"F1 Score:  {f1_score(y_test, y_pred, average='weighted'):.4f}")

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred, labels=model.classes_))

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
    cm_path = os.path.join(SCREENSHOTS_DIR, "confusion_matrix.png")
    plot_confusion_matrix(y_test, y_pred, model.classes_, cm_path)

    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)
    print(f"\nModel saved to {MODEL_PATH}")
    print(f"Vectorizer saved to {VECTORIZER_PATH}")


if __name__ == "__main__":
    train_model()