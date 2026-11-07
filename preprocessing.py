# ============================================
# MÓDULO DE PREPROCESAMIENTO DE TEXTO
# ============================================

import re
import html
import spacy


# Cargar el modelo de inglés de spaCy
nlp = spacy.load("en_core_web_sm")


def preprocess_text(text, remove_stopwords=True):

    # 1. NORMALIZACIÓN
    text = text.lower()

    # 2. LIMPIEZA DE ENTIDADES HTML
    text = html.unescape(text)

    # Recuperar apóstrofes codificados en el dataset
    text = re.sub(r'#39;', "'", text)

    # Corregir espacios antes de los apóstrofes
    text = re.sub(r"\s+'", "'", text)

    # Eliminar residuos de entidades de comillas
    text = re.sub(r'\bquot(?:;|\b)', ' ', text)

    # 3. NORMALIZACIÓN DE ABREVIATURAS

    # Preservar el nombre propio U.S. Open
    text = re.sub(r'\bu\.s\.\s*open\b', 'usopen', text)

    # Reemplazar otras apariciones de U.S. por United States
    text = re.sub(r'\bu\.s\.(?![a-z])', 'united states', text)

    # 4. LIMPIEZA CON EXPRESIONES REGULARES

    # Eliminar URLs
    text = re.sub(r'https?://\S+|www\.\S+', ' ', text)

    # Eliminar dominios web
    text = re.sub(r'\b(?:[a-z0-9-]+\.)+[a-z]{2,}\b', ' ', text)

    # Eliminar metadatos financieros de Reuters
    text = re.sub(
        r'\bquote\s*,?\s*profile\s*,?\s*research\b',
        ' ',
        text
    )

    # Eliminar etiquetas HTML
    text = re.sub(r'<[^>]*>', ' ', text)

    # Conservar letras, espacios y apóstrofes
    text = re.sub(r"[^a-z\s']", ' ', text)

    # Eliminar espacios repetidos
    text = re.sub(r'\s+', ' ', text).strip()

    # 5. LEMATIZACIÓN CON SPACY
    doc = nlp(text)

    tokens = []

    for token in doc:

        # Ignorar puntuación y espacios
        if token.is_punct or token.is_space:
            continue

        # Eliminar el posesivo 's
        if token.text == "'s":
            continue

        # Obtener el lema del token
        lema = token.lemma_.lower()

        # Eliminar stop-words antes y después de la lematización
        if remove_stopwords and (
            token.is_stop or nlp.vocab[lema].is_stop
        ):
            continue

        tokens.append(lema)

    return ' '.join(tokens)