# ¿Qué es machine learning?

Es una rama de la IA, se enfoca de aprender patrones mediante modelo matemático a partir de datos y no necesitan ser programadas explicitamente (Es decir que no necesita que un programador escriba las instruciones), mientras más datos mejor se vuelve prediciendo.

## Conceptos que se menciona en el curso

- Los experiencia de datos se le conoce como *conjunto de entrenamiento*.
- Aprender de datos y realizar predicciones se le llama *modelo*.

## Ejemplo el lo realiza con SPAM
- Proceso tradicional, el programador escribe un algoritmo con gran cantidad de reglas para saber si es spam o no.
- Machine learning, Se obtiene los datos y respuestas que bienen siendo las etiquetas si ese correo es spam o no, el modelo entrega de entregarme las reglas de negocio ya aprendidas.

![spam](../assets/spam.png)

## Ejercicio con Netflix

Ejemplo: Un sistema de Netflix que recomienda películas según lo que has visto anteriormente

- 📚 Experiencia E: Películas que ya he visto en Netflix.
- 🎯 Tarea T: Predecir otras peliculas nuevas que me pueden gustar.
- 📊 Rendimiento P (Se le conoce como Precisión): Si el modelo acerto su recomendación o no.

## Las ramas de la IA

![ramas](../assets/ramas.png)

## Cuándo usar machine learning

1. *Reglas dificiles de definir* como detección de spam, reconocimiento de imagenes, análisis de sentimiento, sistema de recomendación.
2. Necesitas aprender nuevos pratenes no tan evidentes para un humano como detección de fraude financiero, predicción de churn, diagnóstico médico asistido, análisis de comportamiento.
3. Las reglas cambian con el tiempo.
4. Cuando tienes muchos datos historicos pero igual se puede seguir alimientado el modelo si cuentas con pocos datos.
5. Cuando necesitas utilizar probabilidades en vez de intuición, aprender bien en base a nuevos datos.
6. Cuando el coste del error es tolerable ya que machine learning se equivoca no es perfecto.

## Cuándo no utilizar machine learning

- Si puedo resolverlo con reglas simples.
- Con consultas en sql es suficiente.
- Si es solo una validación del negocio.
- No utilizar machine learning para problemas simples.

## Tipos de sistemas de machine learning

### Aprendizaje según tipo de supervisión

- Aprendizaje supervizado: El modelo se entrena con *datos etiquetados*. Cada entrada tiene una salida conocida. Además es costoso necesitas un profesional que vaya a etiquetar como el proceso de radiografias.
- Aprendizaje no supervizado: El modelo trabaja con datos sin etiqueta, solamente busca patrones para agruparlos.
- Aprendizaje semisupervizado: Es una combinación de ambos, combina una pequeña cantidad de datos etiquetados con un gran cantidad de datos sin etiquetar. Es usado cuando etiquetar es costoso.
- Aprendizaje por refuerzo: aprende en base al entorno y el mismo toma decisiones que puede recibir recompesas o castigo. Por ejemplo, el caso del robot que esta aprendiendo a caminar, si se cae castigo y ante diferentes situaciones no se cae premio.

  - Por ejemplo: Como entrenar a un perro
  - ✅ Hace algo bien → Premio
  - ❌ Hace algo mal → Castigo
  - Con el tiempo aprende solo qué decisiones toma

### Aprendizaje según como apreden con el tiempo

- Aprendizaje por lotes: Se entrena usando todo el dataset, una vez entrenado ya no aprende nuevos datos a menos que se reentrene. Se utiliza datos historicos.
- Aprendizaje en línea: El modelo se actualiza de forma continua a medida que lleguen nuevos datos como en streaming.

### Aprendizaje según la forma de generalización
Es la capacidad de un modelo para funcionar bien con datos nuevos y no vistos, no solo con los datos con los que fue entrenado.

- Basado en instancias: Un modelo basado en ejemplos va a memorizar todo los ejemplo que le hayas pasado, va a comprar datos nuevos para clasificar con datos exitentes,*no va a aprender de patrones si no guarda datos de entrenamiento y lo usa con las nuevas instancias, se basa en los vecinos más cercanos*. Esto es costoso a nivel de memoria si hay mucha información ya que los datos de entrenamiento tienen que estar cargado en memoria.

![aprendizaje por instancia](../assets/aprendizaje_por_instancia.png)

- Basado en modelos: El sistema aprende de un modelo general a partir de los datos y luego lo usa para realizar predicciones. 
  - Como funciona:
  1. Analiza todos los datos de entrenamiento.
  2. Crea una representación matemática.
  3. El trabajo pesado ocurre en entrenamiento puede ser costoso.
  4. No necesita datos originales para predecir.
