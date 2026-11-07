# Clasificación supervisada de noticias – AG News

## 1. Descripción del proyecto

Este proyecto desarrolla un sistema de clasificación supervisada de noticias utilizando el conjunto de datos **AG News**. El objetivo es clasificar automáticamente los textos en cuatro categorías:

- **World:** noticias internacionales.
- **Sports:** deportes.
- **Business:** economía y negocios.
- **Sci_Tech:** ciencia y tecnología.

Se utiliza una representación numérica de los textos mediante **TF-IDF** y un clasificador **LinearSVC** (Support Vector Classifier).

El trabajo incluye el análisis exploratorio del corpus, el preprocesamiento de los textos, la experimentación con distintas configuraciones de TF-IDF y la evaluación comparativa de los modelos.

## 2. Estructura del proyecto

La carpeta del proyecto está organizada de la siguiente manera:

```text
AG-News-Classifier/
│
├── data/
│   ├── ag_news_train.csv
│   └── ag_news_test.csv
│
├── preprocessing.py
├── classification.py
├── requirements.txt
├── EDA_NLP_HermetMelisa.ipynb
└── README.md
```

**Descripción de los archivos:**

- `data/`: contiene los conjuntos de entrenamiento y prueba utilizados en el análisis.
- `preprocessing.py`: contiene las funciones de preprocesamiento y limpieza de textos.
- `classification.py`: reúne funciones para la vectorización TF-IDF, el entrenamiento de LinearSVC y la evaluación del clasificador.
- `requirements.txt`: especifica las bibliotecas y versiones necesarias para ejecutar el proyecto.
- `EDA_NLP_HermetMelisa.ipynb`: notebook principal, donde se desarrolla el análisis exploratorio, el preprocesamiento y la clasificación supervisada.
- `README.md`: documento descriptivo del proyecto e instrucciones de ejecución.

**Nota:** Los módulos `preprocessing.py` y `classification.py` contienen implementaciones modulares de los procedimientos principales. La notebook presenta el desarrollo paso a paso mediante sus propias celdas de código.

## 3. Requisitos y dependencias

El proyecto fue desarrollado en Python 3.13.18.

Las principales bibliotecas utilizadas son:

| Biblioteca | Aplicación |
|---|---|
| pandas | Manipulación y análisis de datos. |
| NumPy | Operaciones numéricas. |
| spaCy | Procesamiento del lenguaje natural, lematización y eliminación de stop-words. |
| Scikit-learn | Vectorización TF-IDF, entrenamiento y evaluación del clasificador. |
| Matplotlib | Visualización de resultados. |
| Seaborn | Generación de matrices de confusión. |

Las versiones utilizadas se encuentran especificadas en `requirements.txt`.

## 4. Instalación y configuración del entorno

Desde la carpeta principal del proyecto, ejecutar los siguientes comandos:

```bash
pip install -r requirements.txt
```

Además, es necesario descargar el modelo de inglés de spaCy utilizado durante el preprocesamiento:

```bash
python -m spacy download en_core_web_sm
```

## 5. Ejecución del proyecto

Una vez instaladas las dependencias y descargado el modelo de spaCy:

1. Verificar que los archivos `ag_news_train.csv` y `ag_news_test.csv` se encuentren dentro de la carpeta `data/`.
2. Abrir la notebook `EDA_NLP_HermetMelisa.ipynb` en Jupyter Notebook, JupyterLab o Google Colab.
3. Ejecutar las celdas en orden, desde el inicio hasta el final.

La notebook carga los conjuntos de datos desde la carpeta `data/`, realiza el preprocesamiento de los textos y desarrolla las distintas etapas de clasificación y evaluación.

## 6. Metodología

El desarrollo se organizó en las siguientes etapas:

1. **Exploración de los datos:** inspección de dimensiones, columnas, distribución de categorías y características generales del corpus.
2. **Preprocesamiento:** normalización y limpieza de textos, tratamiento de entidades HTML, lematización y eliminación de stop-words mediante spaCy.
3. **Representación TF-IDF:** transformación de los textos procesados en matrices numéricas.
4. **Entrenamiento:** implementación del clasificador LinearSVC.
5. **Experimentación:** evaluación de tres configuraciones de TF-IDF, modificando el número máximo de características y el rango de n-gramas.
6. **Evaluación:** comparación de los modelos mediante accuracy, precision, recall, F1-score y matrices de confusión.

Para evitar la filtración de información (*data leakage*), los vectorizadores se ajustaron exclusivamente con los datos de entrenamiento y luego se aplicaron al conjunto de prueba.

## 7. Resultados principales

Se evaluaron tres configuraciones:

| Modelo | max_features | ngram_range | Accuracy | F1-score macro |
|---|---:|---|---:|---:|
| Modelo 1 | 5.000 | (1,1) | 0,8825 | 0,8824 |
| Modelo 2 | 5.000 | (1,2) | 0,8875 | 0,8875 |
| Modelo 3 | 10.000 | (1,2) | 0,8940 | 0,8940 |

La tercera configuración obtuvo el mejor desempeño general, con un accuracy del **89,4 %** y un F1-score macro de **0,8940**.

## 8. Consideraciones y limitaciones

La selección de la configuración final se realizó comparando las métricas obtenidas sobre el conjunto de prueba. Si bien el ajuste de los vectorizadores se realizó exclusivamente con los datos de entrenamiento, una estrategia metodológica más rigurosa consistiría en utilizar un conjunto de validación para seleccionar los hiperparámetros y reservar el conjunto de prueba únicamente para la evaluación final.

Las conclusiones, el análisis detallado de los resultados y las limitaciones del modelo se desarrollan en la notebook principal.
