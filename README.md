# Dask y PySpark

## Dask

### Setup

Instalar Graphviz para visualizar el grafo de tareas:

Ubuntu:
```bash
sudo apt install graphviz
```
MacOS:
```bash
brew install graphviz
```

Instalar dependencias:
```bash
python -m venv /path/to/virtualenv
source /path/to/virtualenv/bin/activate
pip install -r requirements.txt
```

Traer datos de taxis:
```bash
python get_taxis_data.py
```

### Correr Jupyter notebook

```bash
jupyter notebook
```

## PySpark

### Correr container de Docker
    
```bash
docker run -it --rm -p 8889:8888 -p 4040:4040 -v $(pwd):/home/jovyan/ jupyter/pyspark-notebook
```