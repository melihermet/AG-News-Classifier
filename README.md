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

3. **Representación TF-IDF:** transformación de los textos procesados en matrices numéricas. Se utilizó TF-IDF (*Term Frequency–Inverse Document Frequency*) para representar la importancia relativa de los términos en cada documento, considerando tanto su frecuencia en el texto como su distribución en el corpus.

4. **Selección del clasificador:** se utilizó LinearSVC (Support Vector Classifier), un clasificador lineal basado en máquinas de soporte vectorial. Esta elección resulta adecuada para tareas de clasificación de textos, ya que permite trabajar eficientemente con representaciones TF-IDF, caracterizadas por tener una elevada dimensionalidad y una estructura dispersa (*sparse*).

5. **Experimentación con TF-IDF:** se evaluaron tres configuraciones, modificando dos parámetros del vectorizador:

   - `max_features`: establece el número máximo de características (términos) consideradas en la representación. Se compararon valores de 5.000 y 10.000 para analizar el efecto del tamaño del vocabulario sobre el desempeño del clasificador.
   - `ngram_range`: define la longitud de las secuencias de términos consideradas. Se probaron `(1,1)`, que utiliza unigramas (palabras individuales), y `(1,2)`, que incorpora unigramas y bigramas (pares de palabras consecutivas). La inclusión de bigramas permite capturar información contextual que puede perderse al considerar únicamente palabras individuales.

6. **Evaluación:** se compararon las configuraciones mediante accuracy, precision, recall, F1-score y matrices de confusión. Se seleccionó la configuración con mejor desempeño general entre las evaluadas.

Para evitar la filtración de información (*data leakage*), cada vectorizador se ajustó exclusivamente con los datos de entrenamiento (`fit_transform`) y luego se aplicó al conjunto de prueba (`transform`).


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
