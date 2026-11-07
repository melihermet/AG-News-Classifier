# ============================================
# MÓDULO DE CLASIFICACIÓN DE TEXTOS
# ============================================

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, confusion_matrix


def vectorize_tfidf(
    train_texts,
    test_texts,
    max_features=5000,
    ngram_range=(1, 1)
):
    """
    Vectoriza los textos mediante TF-IDF.

    El vectorizador se ajusta exclusivamente con los datos
    de entrenamiento para evitar data leakage.
    """

    vectorizer = TfidfVectorizer(
        max_features=max_features,
        ngram_range=ngram_range
    )

    X_train = vectorizer.fit_transform(train_texts)
    X_test = vectorizer.transform(test_texts)

    return vectorizer, X_train, X_test


def train_linear_svc(X_train, y_train, random_state=42):
    """
    Entrena un clasificador LinearSVC.
    """

    model = LinearSVC(random_state=random_state)
    model.fit(X_train, y_train)

    return model


def evaluate_classifier(model, X_test, y_test):
    """
    Genera predicciones, informe de clasificación
    y matriz de confusión.
    """

    y_pred = model.predict(X_test)

    report = classification_report(
        y_test,
        y_pred,
        digits=4
    )

    cm = confusion_matrix(y_test, y_pred)

    return y_pred, report, cm