# Modelos y evaluación matemática

- Lo más importante son los datos.

Recomendaciones para realizar proyectos:
- No generar datos ficticios no va a encontrar patrones reales.
- Plataforma: kaggle, UCI machine learning repository, openML, Data.World / World Bank Open Data, https://datos.gob.cl/dataset/, https://www.datosabiertos.gob.pe/, https://data.gov/, https://aws.amazon.com/es/opendata/

## California Housting

# 🏠 Resumen — Modelado y Evaluación Matemática
### Proyecto que se va a realizar: [California Housing Prices](https://www.kaggle.com/datasets/camnugent/california-housing-prices)

---

## 🧠 Técnica Feynman: ¿Cómo explicarías esto a alguien que no sabe nada de ML?

> **Principio clave:** Si no puedes explicarlo de forma simple, es que aún no lo entiendes del todo.

---

## 1. 📦 ¿Por qué los Datos son lo más importante?

Imagina que quieres aprender a cocinar, pero alguien te da ingredientes podridos. No importa qué tan buena sea tu receta — el resultado será malo.

En Machine Learning pasa exactamente lo mismo:

| Problema con los datos | Consecuencia |
|---|---|
| Datos autogenerados / falsos | El modelo aprende patrones que no existen en la realidad |
| Datos de baja calidad | La hipótesis del modelo se aleja de la realidad |
| Mejorar el algoritmo sin buenos datos | Es inútil — primero mejora la ingesta de datos |

> **💡 Regla de oro:** Mejorar el algoritmo = Mejorar la ingesta de datos.

---

## 2. 🌐 ¿Dónde conseguir datos reales?

Para aprender ML necesitas datos reales. Por suerte, hay muchos repositorios abiertos:

| Repositorio | Tipo de datos | Ideal para... |
|---|---|---|
| **Kaggle Datasets** | Imagen, texto, tabular, series temporales | Comenzar proyectos con notebooks de ejemplo |
| **UCI ML Repository** | Tabular, clasificación, regresión | ML clásico y algoritmos tradicionales |
| **OpenML** | Tabular, imagen, texto | Benchmarking con metadatos listos |
| **Papers with Code** | Imagen, texto, tabular | Investigación y tareas de NLP/visión |
| **Google Dataset Search** | Varios | Búsqueda amplia entre múltiples fuentes |
| **AWS / GCP Open Data** | Gran escala, cloud-ready | Big Data y análisis avanzado |
| **Data.gov** | Economía, salud, educación, clima | Datos gubernamentales de EE. UU. |
| **World Bank Open Data** | Socioeconómicos | Análisis económico o social |

---

## 3. 🏡 El Dataset: California Housing Prices

**¿Qué es esto en palabras simples?**
Es una fotografía del censo de California en 1990. Cada fila del dataset no es una casa — es un **barrio entero** (llamado *block group*).

### 📌 Origen
- Datos del **censo de EE. UU. de 1990**
- Cada fila = un **census block group** (barrio con ~600–3,000 personas)
- Fuente original: **StatLib Repository**

### 📊 Dimensiones del dataset

| Estadístico | Valor |
|---|---|
| Total de muestras | **20,640** |
| Features de entrada | **8** |
| Variable objetivo | Precio medio de casas (USD) |
| Año del censo | 1990 |

El target es lo que quieres predecir. Para encontrarlo hazte esta pregunta:
- "¿Qué quiero que mi modelo me diga dado unos datos de entrada?"

X = Features → Las pistas/características que le das al modelo
y = Target   → La pregunta que quieres que responda

### 🔑 Las 8 Features (variables de entrada)

| Feature | Descripción en simple |
|---|---|
| `MedInc` | ¿Cuánto gana la gente del barrio en promedio? |
| `HouseAge` | ¿Qué tan viejas son las casas? |
| `AveRooms` | ¿Cuántas habitaciones tiene cada casa en promedio? |
| `AveBedrms` | ¿Cuántos dormitorios tiene cada casa en promedio? |
| `Population` | ¿Cuánta gente vive en ese barrio? |
| `AveOccup` | ¿Cuántas personas viven por casa? |
| `Latitude` | Ubicación norte-sur del barrio |
| `Longitude` | Ubicación este-oeste del barrio |

> **🎯 Variable objetivo (target):** `MedHouseVal` — El **precio medio de las casas en USD** del barrio.

### 💻 Cómo cargar el dataset en Python

```python
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing(as_frame=True)
X, y = data.data, data.target  # X = features, y = precio medio
```

---

## 4. 🔧 ¿Qué es Scikit-learn?

Es como una caja de herramientas para Machine Learning en Python. No tienes que construir los algoritmos desde cero — ya están listos para usar.

| Módulo | ¿Para qué sirve? |
|---|---|
| **Preprocesamiento** | Escalar datos, normalizar, codificar variables categóricas |
| **Selección de Features** | Identificar qué variables realmente importan |
| **Entrenamiento** | Algoritmos listos: regresión, clasificación, clustering, etc. |
| **Evaluación** | Calcular métricas como RMSE, MAE, accuracy, F1-score |

---

## 5. 📋 ML Project Checklist — La hoja de ruta completa

Antes de tocar código, sigue este checklist. Es tu guía de principio a fin:

```
✅ 1. Frame the Problem    → ¿Qué problema quiero resolver y por qué?
✅ 2. Get the Data         → ¿De dónde vienen los datos?
✅ 3. Explore the Data     → ¿Qué hay dentro? EDA (Exploratory Data Analysis)
✅ 4. Prepare the Data     → Limpieza, transformación, ingeniería de features
✅ 5. Select & Train       → Elegir y entrenar modelos candidatos
✅ 6. Fine-Tune Models     → Ajustar hiperparámetros del mejor modelo
✅ 7. Present Solution     → Comunicar resultados con claridad
✅ 8. Launch & Monitor     → Desplegar y monitorear en producción
```

---

## 6. 🎯 Paso 1 — Frame the Problem (Definir el Problema)

**¿Por qué esto es tan importante?** Porque construir un modelo sin entender el problema es como conducir sin saber a dónde vas.

### Preguntas que debes responder ANTES de programar:

| Pregunta | En nuestro proyecto |
|---|---|
| ¿Cuál es el objetivo de negocio? | Predecir el precio medio de viviendas por barrio |
| ¿Qué soluciones existen hoy? | Tasaciones manuales, reglas en Excel, expertos inmobiliarios |
| ¿Supervisado o no supervisado? | **Supervisado** — tenemos el precio real como etiqueta |
| ¿Cómo medimos el rendimiento? | Con RMSE o MAE |

### 🔗 El modelo en contexto real:
```
Datos del censo → [MODELO ML] → Precio estimado → Otro sistema → Decisión de inversión
```
La salida del modelo NO es la decisión final — es una señal más dentro de un proceso mayor.

---

## 7. 📐 Tipo de Problema: Aprendizaje Supervisado · Regresión

**¿Por qué "supervisado"?**
Porque tenemos los datos etiquetados — sabemos el precio real de cada barrio.

**¿Por qué "regresión"?**
Porque queremos predecir un **valor numérico continuo** (el precio), no una categoría.

```
Regresión → Tipo de PROBLEMA
Regresión Lineal, XGBoost, Random Forest → MODELOS que lo resuelven

⚠️ No confundir los niveles. Primero clasifica el problema, después elige el algoritmo.
```

| Característica | Nuestro caso |
|---|---|
| Tipo de aprendizaje | Supervisado |
| Tipo de tarea | Regresión |
| Número de outputs | 1 (univariada) |
| Número de features | 8 (múltiple) |

---

## 8. 📏 Métricas de Evaluación

### ¿Qué es una métrica?
Es el número que te dice qué tan bien (o mal) está funcionando tu modelo. **"Funciona bien" no es una sensación — es un número.**

---

### 📉 RMSE — Root Mean Squared Error

**En simple:** ¿Cuánto se equivoca tu modelo en promedio, pero castigando más los errores grandes?

$$RMSE = \sqrt{\frac{1}{m} \sum_{i=1}^{m}(h(x^i) - y^i)^2}$$

**Ejemplo paso a paso (predicción de temperatura):**

| Día | Real (y) | Predicción h(x) | Error |
|---|---|---|---|
| 1 | 20 | 18 | -2 |
| 2 | 25 | 30 | +5 |
| 3 | 30 | 28 | -2 |

```
1. Errores al cuadrado: 4, 25, 4
2. Promedio:           (4 + 25 + 4) / 3 = 11
3. Raíz cuadrada:      √11 ≈ 3.3

→ RMSE ≈ 3.3 grados
```

---

### 📉 MAE — Mean Absolute Error

**En simple:** ¿Cuánto se equivoca tu modelo en promedio, de forma honesta y sin exagerar?

$$MAE = \frac{1}{m} \sum_{i=1}^{m}|h(x^i) - y^i|$$

**Mismo ejemplo:**

```
1. Errores absolutos:  |-2| = 2, |5| = 5, |-2| = 2
2. Promedio:           (2 + 5 + 2) / 3 = 3

→ MAE = 3 grados
```

---

### ⚔️ RMSE vs MAE — ¿Cuál usar?

| Característica | RMSE | MAE |
|---|---|---|
| Fórmula del error | (error)² | \|error\| |
| Sensible a outliers | **Sí — los penaliza más** | No — los trata igual |
| Interpretación | Más técnica | Más intuitiva |
| Úsalo cuando... | Errores grandes son **muy costosos** | Quieres una visión **honesta** del error promedio |

### 🚀 Guía rápida por industria:

| Aplicación | Métrica | Motivo |
|---|---|---|
| Precios de casas / autos | **MAE** | Outliers normales, error promedio importa |
| Logística / ETA | **MAE** | Error promedio importa |
| Forecast de ventas | **MAE** | Datos ruidosos |
| Sensores industriales | **RMSE** | Errores grandes = peligro |
| Finanzas | **RMSE** | Riesgo extremo |
| Medicina | **RMSE** | Seguridad crítica |

> **💡 Regla de oro:** La métrica depende del **contexto** y las **consecuencias** de los errores.  
> Para nuestro proyecto de **California Housing** → usaremos **MAE** (outliers normales, error promedio importa).

---

## 🗺️ Mapa mental del capítulo

```
CURSO ML 2026 #3
│
├── 📦 DATOS
│   ├── Son lo más importante (y costoso)
│   └── Fuentes: Kaggle, UCI, OpenML, etc.
│
├── 🏠 DATASET: California Housing Prices
│   ├── 20,640 muestras · 8 features · target = precio USD
│   └── Cada fila = un barrio (block group), no una casa
│
├── 📋 ML PROJECT CHECKLIST (8 pasos)
│
├── 🎯 FRAME THE PROBLEM
│   ├── Objetivo de negocio → Predecir precio por barrio
│   ├── Supervisado · Regresión múltiple univariada
│   └── Comparar contra soluciones actuales
│
└── 📏 MÉTRICAS
    ├── RMSE → castiga errores grandes (finanzas, medicina)
    └── MAE  → error promedio honesto (precios, logística)
```
---
