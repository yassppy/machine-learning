# Creación entorno virtual

## Crear un proyecto nuevo
```
uv init california-housing
```

```
cd california-housing
```

```
uv venv
```

## Activar el entorno virtual
```
.venv\Scripts\activate

```

## Agregar dependencias

```
uv add pandas numpy matplotlib seaborn scikit-learn
```

## Ver las dependencias instaladas
```
uv pip list
```

## Correr tu script
```
uv run main.py
```
