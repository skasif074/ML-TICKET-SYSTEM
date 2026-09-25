# preprocessing.py
# Purpose: Shared text-cleaning logic used by both training (train.py) and
# inference (predict.py / app.py), so the exact same cleaning is applied
# to historical training data and to new user-submitted tickets at prediction time.

import re
import string


def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""

    text = text.lower()

    text = re.sub(r"http\S+|www\S+", " ", text)

    text = text.translate(str.maketrans("", "", string.punctuation))

    text = re.sub(r"\d+", " ", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text


def clean_dataframe_column(df, column: str, new_column: str = "clean_description"):
    df[new_column] = df[column].apply(clean_text)
    return df