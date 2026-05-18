# 📊 Resumen — Carga, Exploración y Preparación de Datos
### Proyecto: [California Housing Prices](https://www.kaggle.com/datasets/camnugent/california-housing-prices)

---

## 1. 🖥️ Google Colab — Tu laboratorio en la nube

> **En simple:** Es como tener Python instalado en la nube, sin configurar nada en tu computadora.

| Característica | Detalle |
|---|---|
| Plataforma | Navegador web — sin instalación |
| Tipo de archivo | Notebook `.ipynb` (celdas de código + texto) |
| Librerías preinstaladas | `pandas`, `numpy`, `TensorFlow`, `PyTorch` |
| Recursos gratuitos | GPU y TPU en la nube |

### 📋 Tipos de celdas:

| Celda | ¿Para qué? |
|---|---|
| **Código** | Instrucciones Python ejecutables, probar ideas, depurar paso a paso |
| **Texto** | Explicaciones en Markdown, títulos, fórmulas LaTeX |

> **💡 Regla de oro:** Alterna celdas de texto y código — tu notebook debe poder leerlo alguien que no sabe nada del tema.

### ✍️ Markdown útil en Colab:

| Uso | Sintaxis | Ejemplo |
|---|---|---|
| Título | `# Título` | `# Análisis de Datos` |
| Subtítulo | `## Subtítulo` | `## Limpieza` |
| Negrita | `**texto**` | `**importante**` |
| Cursiva | `*texto*` | `*nota*` |
| Código inline | `` `codigo` `` | `` `df.head()` `` |
| Fórmula inline | `$formula$` | `$y = mx + b$` |
| Fórmula bloque | `$$formula$$` | `$$RMSE = ...$$` |
| Lista | `- item` | `- pandas` |
| Enlace | `[texto](url)` | `[Kaggle](https://kaggle.com)` |

---

## 2. 🐼 Pandas vs ⚡ Polars — ¿Cuál usar?

> **En simple:** Pandas es el clásico confiable. Polars es el deportivo nuevo — más rápido pero más estricto.

| Característica | Pandas | Polars |
|---|---|---|
| Lenguaje base | Python | Rust |
| Velocidad | Media | Muy alta |
| Uso de memoria | Alto | Bajo |
| Paralelismo | Limitado | Nativo |
| Mutabilidad | Sí | No |
| Lazy execution | No | Sí |
| API | Muy flexible | Más estricta |
| Dataset grande | Se degrada | Escala mejor |
| Integración ML | Excelente | En crecimiento |
| Curva de aprendizaje | Baja | Media |
| Estado del ecosistema | Madurísimo | En expansión |

### 🧠 ¿Cuándo usar cada uno?

```
¿Tu dataset es pequeño o mediano? (< 1 millón de filas)
    └── Pandas ✅ — más integración con sklearn y más documentación

¿Tu dataset es enorme o necesitas máxima velocidad?
    └── Polars ✅ — más eficiente en memoria y procesamiento paralelo
```

> **Para este curso:** usamos **Pandas** — mejor integración con scikit-learn y más fácil de aprender.

---

## 3. 📥 Carga del Dataset

```python
# Opción 1 — Desde Kaggle (dataset descargado)
import pandas as pd

df = pd.read_csv("data/housing.csv")
print(df.shape)   # (20640, 10)
df.head()
```

```python
# Opción 2 — Descarga automática desde GitHub (método del curso)
from pathlib import Path
import pandas as pd
import tarfile, urllib.request

url = "https://github.com/ageron/data/raw/main/housing.tgz"

def load_housing_data():
    datasets_dir = Path("datasets")
    tarball_path = datasets_dir / "housing.tgz"
    csv_path     = datasets_dir / "housing" / "housing.csv"

    if not tarball_path.exists():
        datasets_dir.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as tar:
            tar.extractall(path=datasets_dir, filter="data")

    return pd.read_csv(csv_path)

df = load_housing_data()
```

---

## 4. % Percentiles (Cuartiles) — Entendiendo la distribución

> **En simple:** Los percentiles te dicen "¿dónde está parado un valor dentro de todos los datos?"

```
Imagina que ordenamos de menor a mayor los 20,640 precios de casas:

[precio más barato] ──────────────────────── [precio más caro]
        │              │              │              │
       Min            Q1            Q2             Q3            Max
                      25%           50%            75%
```

| Cuartil | Porcentaje | Significado |
|---|---|---|
| **Q1** — Primer cuartil | 25% | El 25% de los datos está por debajo de este valor |
| **Q2** — Mediana | 50% | La mitad exacta de los datos |
| **Q3** — Tercer cuartil | 75% | Solo el 25% superior está por encima |

### 🔢 Ejemplo con datos reales:

```
Datos: 2, 4, 6, 8, 10, 12, 14, 16

Q1 = 6   → el 25% de valores está por debajo de 6
Q2 = 9   → la mitad está por debajo de 9  (mediana)
Q3 = 14  → el 75% está por debajo de 14
```

### 🏠 Aplicado a California Housing:

```
median_house_value:

Q1 = $119,600  → barrios económicos
Q2 = $179,700  → precio típico del mercado
Q3 = $264,725  → barrios caros

Una casa en $800,000 está muy por encima del Q3 → posible outlier ⚠️
```

### ✅ ¿Para qué sirven los percentiles?

**Uso 1 — Detectar outliers:**
```
Precio muy por encima del Q3 → outlier → puede inflar el RMSE
```

**Uso 2 — Evitar que el promedio mienta:**
```
Salarios: [1M, 1.2M, 1.3M, 1.4M, 20M]

❌ Promedio = 5M  → engañoso, el 20M lo jala hacia arriba
✅ Mediana  = 1.3M → representativo, ignora el outlier
```

> **Regla clave:** Cuando haya outliers, confía en la **mediana**, no en el **promedio**.

---

## 5. 📐 Desviación Estándar — ¿Qué tan dispersos están los datos?

> **En simple:** Mide si los datos están juntos (similares entre sí) o esparcidos (muy diferentes).

```
Desviación estándar PEQUEÑA → datos concentrados → fácil de predecir
Desviación estándar GRANDE  → datos dispersos    → difícil de predecir
```

### 🏠 Ejemplo con barrios:

| | Barrio "normal" | Barrio "loco" |
|---|---|---|
| Precios | 100k, 105k, 98k, 102k, 110k | 50k, 80k, 100k, 200k, 500k |
| Promedio | ~103k | ~186k |
| Desviación | **BAJA** ✅ | **ALTA** ⚠️ |
| Interpretación | Predecible, homogéneo | Impredecible, muy desigual |

### 🤖 Desviación estándar en ML — Estandarización:

**El problema:**
```
total_rooms:  50, 80, 120, 300   ← números grandes
households:    1,  2,   3,   4   ← números pequeños

El modelo le da más importancia a total_rooms solo por ser números más grandes
→ SESGO por escala ❌
```

**La solución — Estandarización (StandardScaler):**

$$z = \frac{valor - promedio}{desviación\_estándar}$$

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Resultado:
# → Promedio de cada columna = 0
# → Mayoría de valores entre -1 y 1
# → Todas las features tienen igual peso inicial ✅
```

**Beneficios:**

```
✅ Modelos aprenden más rápido    → gradiente converge eficientemente
✅ No se sesgan por números grandes → todas las features parten igual
✅ Predicen mejor                  → mejora la precisión del modelo
```

---

## 6. 📊 Histograma — Ver la distribución visualmente

> **En simple:** Es una foto de cómo se distribuyen tus datos — te dice dónde están concentrados y dónde hay valores raros.

```
Eje X (horizontal) → valores de la variable (ej: precios de casas)
Eje Y (vertical)   → cuántos datos caen en ese rango
Cada barra         → un rango de valores (bin)
```

### 🔍 Qué puedes detectar con un histograma:

| Señal | Qué significa |
|---|---|
| Barra muy alta y solitaria al final | Posible límite artificial o outlier |
| Datos concentrados a la izquierda | Distribución sesgada — considerar log transform |
| Distribución simétrica en campana | Datos normales — ideal para ML |
| Barras dispersas sin patrón | Alta variabilidad — revisar calidad de datos |

```python
# Graficar histograma en pandas
import matplotlib.pyplot as plt

df.hist(figsize=(15, 10), bins=50)
plt.tight_layout()
plt.show()
```

> **💡 Regla de oro del EDA:** Antes de entrenar cualquier modelo, grafica los histogramas de todas tus features. Los datos te hablan — solo tienes que escucharlos.

---

## 🗺️ Mapa mental del capítulo

```
CURSO ML 2026 #4
│
├── 🖥️ GOOGLE COLAB
│   ├── Notebook = celdas de código + texto Markdown
│   └── GPU/TPU gratuitos en la nube
│
├── 🐼 PANDAS vs ⚡ POLARS
│   ├── Pandas  → clásico, flexible, ideal para ML con sklearn
│   └── Polars  → rápido, eficiente, ideal para Big Data
│
├── 📥 CARGA DE DATOS
│   └── pd.read_csv() → DataFrame listo para explorar
│
├── % PERCENTILES
│   ├── Q1 (25%) → valor mínimo "normal"
│   ├── Q2 (50%) → mediana, más robusta que el promedio
│   └── Q3 (75%) → umbral de valores altos
│
├── 📐 DESVIACIÓN ESTÁNDAR
│   ├── Pequeña → datos homogéneos, fácil de predecir
│   ├── Grande  → datos dispersos, difícil de predecir
│   └── Estandarización → (valor - media) / std → escala uniforme
│
└── 📊 HISTOGRAMA
    ├── Visualiza la distribución de cada variable
    └── Detecta outliers, sesgos y límites artificiales
```

---

## 📚 Libro Recomendado para Estadística

### "Estadística Práctica para Ciencia de Datos con R y Python"
**Autores:** Peter Bruce, Andrew Bruce & Peter Gedeck

> **¿Por qué este libro?**

| Característica | Detalle |
|---|---|
| 📖 Nivel | Principiante — sin fórmulas intimidantes |
| 🎯 Enfoque | 100% aplicado a Data Science y ML |
| 🐍 Lenguaje | Ejemplos en Python y R |
| 📊 Temas | Distribuciones, percentiles, correlación, muestreo, regresión |
| ✅ Ideal para | Personas que aprenden haciendo, no leyendo teoría pura |

```
Capítulos más relevantes para tu proyecto California Housing:

Cap 1 → Estadística exploratoria (describe(), histogramas)
Cap 2 → Distribuciones de datos (percentiles, desviación estándar)
Cap 3 → Distribución estadística (normal, sesgada)
Cap 4 → Regresión y predicción (directamente aplicable a tu modelo)
```

> **Alternativa más corta:** "Naked Statistics" de Charles Wheelan — sin código, pero explica la intuición estadística de forma muy entretenida y con ejemplos del mundo real. Ideal si quieres entender el "por qué" antes del "cómo".

---
